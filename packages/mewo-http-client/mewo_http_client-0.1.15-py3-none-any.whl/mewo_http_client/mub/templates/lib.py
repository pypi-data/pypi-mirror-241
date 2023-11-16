from typing import List, Tuple, Optional, Union


def http_error(
    method: str,
    request_url: str,
    status_code: int,
    reason: str,
    retries: Optional[Union[int, str]] = None,
    log_level: str = "error",
    request_id: Optional[str] = "unknown",
) -> Tuple[str, str, List[str]]:
    subj = f"{log_level.capitalize()}: Request '{request_id}' failed completely"

    # We remove query args from url.
    redacted_url = request_url.split("?")[0]

    if retries is None:
        retries = "?"

    body = (
        f"Request: {method.upper()} {redacted_url}\n\n"
        f"Request id: `{request_id}`\n\n"
        f"Reason: `{reason}`\n\n"
        f"Status Code: `{status_code}`\n\n"
        f"Retries: `{retries}`\n\n"
    )

    tags = ["log", log_level, "http", request_id]

    return subj, body, tags


def exception(
    exception: str,
    exception_id: str = "unknown",
    return_code: Optional[Union[str, int]] = "?",
    log_level: str = "error",
) -> Tuple[str, str, List[str]]:
    subj = f"{log_level.capitalize()}: Exception '{exception_id}' raised"
    body = (
        f"Exception id: `{exception_id}`\n\n"
        f"Return Code: `{return_code}`\n\n"
        f"```\n{exception}\n```\n"
    )

    tags = ["log", log_level, "exception", exception_id]

    return subj, body, tags
