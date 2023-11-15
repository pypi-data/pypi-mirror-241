from typing import List, Tuple, Optional, Union


def http_error(
    method: str,
    request_url: str,
    status_code: int,
    reason: str,
    retries: Optional[int] = None,
    note="",
    log_level="error",
) -> Tuple[str, str, List[str]]:
    subj = "HTTP request failed"
    body = (
        f"url: {request_url}\n"
        f"method: {method.capitalize()}\n"
        f"status: {status_code}\n"
        f"reason: {reason}\n"
        f"retries: {retries}\n"
        f"note: {note}\n"
    )
    tags = ["log", log_level, "http"]

    return subj, body, tags


def exception(
    exception: str,
    return_code: Optional[Union[str, int]] = "null",
    note: str = "null",
    log_level: str = "error",
) -> Tuple[str, str, List[str]]:
    subj = "Exception"
    body = (
        f"An exception was raised:\n\n"
        f"{exception}\n\n"
        f"return_code: {return_code}\n\n"
        f"note: {note}"
    )
    tags = ["log", log_level, "exception"]

    return subj, body, tags
