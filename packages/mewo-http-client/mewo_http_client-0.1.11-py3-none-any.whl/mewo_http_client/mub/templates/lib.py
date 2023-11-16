from typing import List, Tuple, Optional, Union


def http_error(
    method: str,
    request_url: str,
    status_code: int,
    reason: str,
    retries: Optional[int] = None,
    log_level: str = "error",
    request_id: Optional[str] = "unknown",
) -> Tuple[str, str, List[str]]:
    subj = f"{log_level.capitalize()}: HTTP request failed completely"
    body = (
        f"{method.upper()} {request_url}\n\n"
        f"Reason: `{reason}`\n\n"
        f"Status Code: `{status_code}`\n\n"
        f"Retries: `{retries or '?'}`\n\n"
    )
    if request_id:
        body += f"Request id: {request_id}\n"

    tags = ["log", log_level, "http"]

    return subj, body, tags


def exception(
    exception: str,
    description: Optional[str] = "Unknown Exception.",
    return_code: Optional[Union[str, int]] = "?",
    log_level: str = "error",
) -> Tuple[str, str, List[str]]:
    subj = f"{log_level.capitalize()}: Exception raised"
    body = (
        f"{description}\n\n"
        f"```\n{exception}\n```\n\n"
        f"Return Code: `{return_code}`\n\n"
    )

    tags = ["log", log_level, "exception"]

    return subj, body, tags
