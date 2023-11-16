// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.

use std::cmp::min;
use std::cmp::Ordering;
use std::io;
use std::task::ready;
use std::task::Context;
use std::task::Poll;

use bytes::Buf;
use bytes::BufMut;
use bytes::Bytes;
use futures::StreamExt;

use crate::raw::*;
use crate::Error;
use crate::ErrorKind;
use crate::Result;

/// Body used in async HTTP requests.
#[derive(Default)]
pub enum AsyncBody {
    /// An empty body.
    #[default]
    Empty,
    /// Body with bytes.
    Bytes(Bytes),
    /// Body with chunked bytes.
    ///
    /// This is nearly the same with stream, but we can save an extra box.
    ChunkedBytes(oio::ChunkedBytes),
    /// Body with stream.
    Stream(oio::Streamer),
}

/// IncomingAsyncBody carries the content returned by remote servers.
///
/// # Notes
///
/// Client SHOULD NEVER construct this body.
pub struct IncomingAsyncBody {
    /// # TODO
    ///
    /// hyper returns `impl Stream<Item = crate::Result<Bytes>>` but we can't
    /// write the types in stable. So we will box here.
    ///
    /// After [TAIT](https://rust-lang.github.io/rfcs/2515-type_alias_impl_trait.html)
    /// has been stable, we can change `IncomingAsyncBody` into `IncomingAsyncBody<S>`.
    inner: oio::Streamer,
    size: Option<u64>,
    consumed: u64,
    chunk: Option<Bytes>,
}

impl IncomingAsyncBody {
    /// Construct a new incoming async body
    pub fn new(s: oio::Streamer, size: Option<u64>) -> Self {
        Self {
            inner: s,
            size,
            consumed: 0,
            chunk: None,
        }
    }

    /// Create an empty IncomingAsyncBody.
    pub(crate) fn empty() -> Self {
        Self {
            inner: Box::new(()),
            size: Some(0),
            consumed: 0,
            chunk: None,
        }
    }

    /// Consume the entire body.
    pub async fn consume(mut self) -> Result<()> {
        use oio::ReadExt;

        while let Some(bs) = self.next().await {
            bs.map_err(|err| {
                Error::new(ErrorKind::Unexpected, "fetch bytes from stream")
                    .with_operation("http_util::IncomingAsyncBody::consume")
                    .set_source(err)
            })?;
        }

        Ok(())
    }

    /// Consume the response to bytes.
    ///
    /// This code is Inspired from hyper's [`to_bytes`](https://docs.rs/hyper/latest/hyper/body/fn.to_bytes.html).
    pub async fn bytes(mut self) -> Result<Bytes> {
        use oio::ReadExt;

        // If there's only 1 chunk, we can just return Buf::to_bytes()
        let mut first = if let Some(buf) = self.next().await {
            buf?
        } else {
            return Ok(Bytes::new());
        };

        let second = if let Some(buf) = self.next().await {
            buf?
        } else {
            return Ok(first.copy_to_bytes(first.remaining()));
        };

        // With more than 1 buf, we gotta flatten into a Vec first.
        let cap = first.remaining() + second.remaining() + self.size.unwrap_or_default() as usize;
        let mut vec = Vec::with_capacity(cap);
        vec.put(first);
        vec.put(second);

        while let Some(buf) = self.next().await {
            vec.put(buf?);
        }

        Ok(vec.into())
    }

    #[inline]
    fn check(expect: u64, actual: u64) -> Result<()> {
        match actual.cmp(&expect) {
            Ordering::Equal => Ok(()),
            Ordering::Less => Err(Error::new(
                ErrorKind::ContentIncomplete,
                &format!("reader got too less data, expect: {expect}, actual: {actual}"),
            )
            .set_temporary()),
            Ordering::Greater => Err(Error::new(
                ErrorKind::ContentTruncated,
                &format!("reader got too much data, expect: {expect}, actual: {actual}"),
            )
            .set_temporary()),
        }
    }
}

impl oio::Read for IncomingAsyncBody {
    fn poll_read(&mut self, cx: &mut Context<'_>, mut buf: &mut [u8]) -> Poll<Result<usize>> {
        if buf.is_empty() || self.size == Some(0) {
            return Poll::Ready(Ok(0));
        }

        // We must get a valid bytes from underlying stream
        let mut bs = loop {
            match ready!(self.poll_next(cx)) {
                Some(Ok(bs)) if bs.is_empty() => continue,
                Some(Ok(bs)) => break bs,
                Some(Err(err)) => return Poll::Ready(Err(err)),
                None => return Poll::Ready(Ok(0)),
            }
        };

        let amt = min(bs.len(), buf.len());
        buf.put_slice(&bs[..amt]);
        bs.advance(amt);
        if !bs.is_empty() {
            self.chunk = Some(bs);
        }

        Poll::Ready(Ok(amt))
    }

    fn poll_seek(&mut self, cx: &mut Context<'_>, pos: io::SeekFrom) -> Poll<Result<u64>> {
        let (_, _) = (cx, pos);

        Poll::Ready(Err(Error::new(
            ErrorKind::Unsupported,
            "output reader doesn't support seeking",
        )))
    }

    fn poll_next(&mut self, cx: &mut Context<'_>) -> Poll<Option<Result<Bytes>>> {
        if self.size == Some(0) {
            return Poll::Ready(None);
        }

        if let Some(bs) = self.chunk.take() {
            return Poll::Ready(Some(Ok(bs)));
        }

        let res = match ready!(self.inner.poll_next_unpin(cx)) {
            Some(Ok(bs)) => {
                self.consumed += bs.len() as u64;
                Some(Ok(bs))
            }
            Some(Err(err)) => Some(Err(err)),
            None => {
                if let Some(size) = self.size {
                    Self::check(size, self.consumed)?;
                }

                None
            }
        };

        Poll::Ready(res)
    }
}
