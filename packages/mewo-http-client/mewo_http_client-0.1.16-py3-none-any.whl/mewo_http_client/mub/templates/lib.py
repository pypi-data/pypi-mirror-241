from posixpath import split
import sys
from typing import List, Tuple, Optional, Union

LOG_LEVELS = ["debug", "info", "warn", "error", "critical"]


def validate_log_level(log_level):
    """
    Raise if wrong log level is given.
    """
    if log_level not in LOG_LEVELS:
        sys.stderr.write(
            f"Error: Unknown log_level '{log_level}'. Possible values for log_level: "
            + ",".join(LOG_LEVELS)
        )
        sys.exit(1)


def id_to_subject(id_str: str) -> str:
    """
    Convert an id string into a title string. E.g.:
    `my_log_id` becomes `My Log Id`
    """
    id_str_spaces = (
        id_str.replace("-", " ").replace("_", " ").replace(".", " ").replace(":", " ")
    )
    id_str_spaces_cap = [s.capitalize() for s in id_str_spaces.split(" ")]
    return " ".join(id_str_spaces_cap)


def log_http_error(
    level: str,
    log_id: str,
    method: str,
    request_url: str,
    status_code: int,
    reason: str,
    retries: Optional[Union[int, str]] = None,
    body: Optional[str] = None,
) -> Tuple[str, str, List[str]]:
    """
    Log http error on mub.
    log_level: debug, info, warn, error, critical
    """

    # We remove query args from url.
    redacted_url = request_url.split("?")[0]

    if retries is None:
        retries = "?"

    trace = (
        f"Request: {method.upper()} {redacted_url}\n"
        f"Reason: {reason}\n"
        f"Status Code: {status_code}\n"
        f"Retries: {retries}\n"
    )

    pre_body = f"HTTP request failed after {retries} retries.\n\n{body}\n\n"

    subj, full_body, tags = log(level=level, log_id=log_id, trace=trace, body=pre_body)

    subj_split = subj.split(":")
    full_subj = subj_split[0] + ": Request Failed: " + subj_split[1]

    return full_subj, full_body, [*tags, "http", "request"]


def log(
    level: str,
    log_id: str,
    body: Optional[str] = None,
    trace: Optional[str] = None,
) -> Tuple[str, str, List[str]]:
    """
    Log something on mub.
    log_level: debug, info, warn, error, critical
    """
    validate_log_level(level)

    subj = f"{level.capitalize()}: {id_to_subject(log_id)}"

    full_body = f"Log id: `{log_id}`\n\n"

    if body is not None:
        full_body += f"{body}\n\n"

    if trace is not None:
        full_body += f"```\n{trace}\n```\n"

    tags = ["log", level, log_id]

    return subj, full_body, tags
