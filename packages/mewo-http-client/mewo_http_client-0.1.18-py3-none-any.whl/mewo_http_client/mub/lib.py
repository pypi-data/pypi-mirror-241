from typing import BinaryIO, Optional, List, Union, TextIO, Tuple
from datetime import datetime
import sys

from requests.models import Response

from mewo_http_client.lib import write_to_files, post, Response
from mewo_http_client.mub import templates


class Mub:
    def __init__(
        self,
        mub_url: str = "",
        from_prefix: str = "",
        from_suffix: str = "",
        to_prefix: str = "",
        to_suffix: str = "",
        subj_prefix: str = "",
        subj_suffix: str = "",
        body_prefix: str = "",
        body_suffix: str = "",
        tags_prefix: List[str] = [],
        tags_suffix: List[str] = [],
        retry: int = 10,
        sleep: float = 3.6,
        factor: float = 3.0,
        sleep_max: float = 0.0,
        stdout=[sys.stdout],
        stderr=[sys.stderr],
        default_request_id="unknown",
    ):
        self.mub_url = mub_url
        self.from_prefix = from_prefix
        self.from_suffix = from_suffix
        self.to_prefix = to_prefix
        self.to_sufffix = to_suffix
        self.subj_prefix = subj_prefix
        self.subj_suffix = subj_suffix
        self.body_prefix = body_prefix
        self.body_suffix = body_suffix
        self.tags_prefix = tags_prefix
        self.tags_suffix = tags_suffix
        self.retry = retry
        self.sleep = sleep
        self.factor = factor
        self.sleep_max = sleep_max
        self.stdout = stdout
        self.stderr = stderr
        self.default_request_id = default_request_id

    def send(
        self,
        subj: str = "",
        request_id: Optional[str] = None,
        body: str = "",
        tags: List[str] = [],
        from_: str = "",
        to: str = "",
        mub_url: str = "",
        retry: Optional[int] = None,
        sleep: Optional[float] = None,
        factor: Optional[float] = None,
        sleep_max: Optional[float] = None,
        stdout: List[Union[TextIO, BinaryIO]] = [],
        stderr: List[Union[TextIO, BinaryIO]] = [],
    ) -> Response:
        """
        Class
        """
        subj = self.subj_prefix + subj + self.subj_suffix
        request_id = self.default_request_id if request_id is None else request_id
        body = self.body_prefix + body + self.body_suffix
        tags = self.tags_prefix + tags + self.tags_suffix
        from_ = self.from_prefix + from_ + self.from_suffix
        to = self.to_prefix + to + self.to_sufffix
        mub_url = mub_url if mub_url else self.mub_url
        retry = retry if retry else self.retry
        sleep = sleep if sleep else self.sleep
        factor = factor if factor else self.factor
        sleep_max = sleep_max if sleep_max else self.sleep_max
        stdout = stdout if stdout else self.stdout
        stderr = stderr if stderr else self.stderr

        if not all([from_, subj, body, tags, mub_url]):
            msg = "Error: mub.send() needs at least these args: from, subj, body, tags, url\n"
            write_to_files(stderr, msg)

        data = {
            "from": from_,
            "to": to,
            "subject": subj,
            "body": body,
            "tags": tags,
            "sent": datetime.utcnow().isoformat(),
        }

        r = post(
            mub_url,
            json=data,
            target_status=[200],
            retry=retry,
            sleep=sleep,
            factor=factor,
            sleep_max=sleep_max,
            stdout=stdout,
            stderr=stderr,
            request_id=request_id,
        )

        return r

    def log(
        self,
        level: str,
        log_id: str,
        body: Optional[str] = None,
        trace: Optional[str] = None,
        **send_kwargs,
    ) -> Response:
        subj, full_body, tags, request_id = templates.log(level, log_id, body, trace)
        return self.send(
            subj=subj, body=full_body, tags=tags, request_id=request_id, **send_kwargs
        )

    def log_http_error(
        self,
        level: str,
        log_id: str,
        method: str,
        request_url: str,
        status_code: int,
        reason: str,
        retries: Optional[Union[int, str]] = None,
        body: Optional[str] = None,
        **send_kwargs,
    ) -> Response:
        subj, full_body, tags, request_id = templates.log_http_error(
            level,
            log_id,
            method,
            request_url,
            status_code,
            reason,
            retries,
            body,
        )
        return self.send(
            subj=subj, body=full_body, tags=tags, request_id=request_id, **send_kwargs
        )


_mub_lib = Mub()

send = _mub_lib.send
log = _mub_lib.log
log_http_error = _mub_lib.log_http_error


# def send(
#     subj: str = "",
#     request_id: str = "unknown",
#     body: str = "",
#     tags: List[str] = [],
#     from_: str = "",
#     to: Optional[str] = "",
#     mub_url: str = "",
#     retry: int = 0,
#     sleep: float = 1,
#     factor: float = 2.0,
#     sleep_max: float = 0.0,
#     stdout: List[Union[TextIO, BinaryIO]] = [sys.stdout],
#     stderr: List[Union[TextIO, BinaryIO]] = [sys.stderr],
# ) -> Response:
#     if not all([from_, subj, body, tags, mub_url]):
#         msg = (
#             "Error: mub.send() needs at least these args: from, subj, body, tags, url\n"
#         )
#         write_to_files(stderr, msg)

#     data = {
#         "from": from_,
#         "to": to,
#         "subject": subj,
#         "body": body,
#         "tags": tags,
#         "sent": datetime.utcnow().isoformat(),
#     }

#     r = post(
#         mub_url,
#         json=data,
#         target_status=[200],
#         retry=retry,
#         sleep=sleep,
#         factor=factor,
#         sleep_max=sleep_max,
#         stdout=stdout,
#         stderr=stderr,
#         request_id=request_id,
#     )

#     return r


# def log(
#     level: str,
#     log_id: str,
#     body: Optional[str] = None,
#     trace: Optional[str] = None,
#     **send_kwargs,
# ) -> Response:
#     subj, full_body, tags, request_id = templates.log(level, log_id, body, trace)
#     return send(
#         subj=subj, body=full_body, tags=tags, request_id=request_id, **send_kwargs
#     )


# def log_http_error(
#     level: str,
#     log_id: str,
#     method: str,
#     request_url: str,
#     status_code: int,
#     reason: str,
#     retries: Optional[Union[int, str]] = None,
#     body: Optional[str] = None,
#     **send_kwargs,
# ) -> Response:
#     subj, full_body, tags, request_id = templates.log_http_error(
#         level,
#         log_id,
#         method,
#         request_url,
#         status_code,
#         reason,
#         retries,
#         body,
#     )
#     return send(
#         subj=subj, body=full_body, tags=tags, request_id=request_id, **send_kwargs
#     )
