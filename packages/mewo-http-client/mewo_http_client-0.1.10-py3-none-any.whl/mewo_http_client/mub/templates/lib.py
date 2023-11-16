from typing import List, Tuple, Optional, Union


def http_error(
    method: str,
    request_url: str,
    status_code: int,
    reason: str,
    retries: Optional[int] = None,
    log_level: str = "error",
    note: Optional[str] = None,
) -> Tuple[str, str, List[str]]:
    subj = f"{log_level.capitalize()}: HTTP request failed completely"
    body = (
        f"{method.upper()} {request_url}\n\n"
        f"Retries: `{retries or '?'}`\n\n"
        f"Status Code: `{status_code}`\n\n"
        f"```\n{reason}\n```\n\n"
    )
    if note:
        body += f"{note}\n"

    tags = ["log", log_level, "http"]

    return subj, body, tags


def exception(
    exception: str,
    return_code: Optional[Union[str, int]] = "null",
    log_level: str = "error",
    note: Optional[str] = None,
) -> Tuple[str, str, List[str]]:
    subj = f"{log_level.capitalize()}: Exception raised"
    body = f"Return Code: `{return_code}`\n\n" f"```\n{exception}\n```\n\n"
    if note:
        body += f"{note}\n"

    tags = ["log", log_level, "exception"]

    return subj, body, tags
