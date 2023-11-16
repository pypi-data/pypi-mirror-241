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
    subj = "HTTP request failed completely"
    body = (
        f"{method.upper()} {request_url}\n\n"
        f"Status: {status_code}\n\n"
        f"Retries: {retries}\n\n"
        f"Reason:\n\n```\n{reason}\n```\n\n"
        f"Note:\n\n{note}\n"
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
