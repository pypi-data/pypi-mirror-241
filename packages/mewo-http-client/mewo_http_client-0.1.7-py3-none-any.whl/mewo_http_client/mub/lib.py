from typing import BinaryIO, Optional, List, Union, TextIO, Tuple
from datetime import datetime
import sys

from requests.models import Response

from mewo_http_client.lib import write_to_files, post, Response


def send(
    mub_url: str = "",
    from_: str = "",
    subj: str = "",
    body: str = "",
    tags: List[str] = [],
    to: Optional[str] = "",
    retry: int = 0,
    sleep: float = 1,
    factor: float = 2.0,
    sleep_max: float = 0.0,
    stdout: List[Union[TextIO, BinaryIO]] = [sys.stdout],
    stderr: List[Union[TextIO, BinaryIO]] = [sys.stderr],
) -> Response:
    if not all([from_, subj, body, tags, mub_url]):
        msg = (
            "Error: mub.send() needs at least these args: from, subj, body, tags, url\n"
        )
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
    )

    return r


def log(
    mub_url: str = "",
    from_: str = "",
    subj: str = "",
    body: str = "",
    tags: List[str] = [],
    to: Optional[str] = "",
    retry: int = 0,
    sleep: float = 1,
    factor: float = 2.0,
    sleep_max: float = 0.0,
    stdout: List[Union[TextIO, BinaryIO]] = [sys.stdout],
    stderr: List[Union[TextIO, BinaryIO]] = [sys.stderr],
) -> Response:
    kwargs = locals()
    kwargs["tags"] = ["log", *kwargs["tags"]]
    return send(**kwargs)
