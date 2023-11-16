import sys
import requests
from requests import Response
import time
from typing import Callable, List, Dict, Any, Optional, Union, TextIO, BinaryIO

RETRY_HANDLER_ARG_NAMES = [
    "target_status",
    "retry",
    "sleep",
    "factor",
    "sleep_max",
    "stdout",
    "stderr",
    "request_id",
]


unit_devider = {
    "ms": 0.001,
    "s": 1,
    "m": 60,
    "h": 60 * 60,
    "d": 60 * 60 * 24,
}


def calculate_retry_sleep_durations(
    retry=10, sleep=60.0, factor=2.0, sleep_max=300.0, unit="s"
):
    devider = unit_devider[unit]
    sleep_count = sleep
    sleep_total = 0

    for i in range(1, retry):
        # We sleep and later increase.
        sleep_total = sleep_total + sleep_count

        count_for_humans = "{0:.2f}".format(round(sleep_count / devider, 2))
        print(f"Call {i} after {count_for_humans} {unit}")

        sleep_count = sleep_count * factor

        if sleep_max and sleep_count > sleep_max:
            sleep_count = sleep_max

    total_for_humans = "{0:.2f}".format(round(sleep_total / devider, 2))
    print(f"\nTotal: {total_for_humans} {unit}")


def write_to_files(files, msg: str):
    for f in files:
        try:
            f.write(msg)
        except:
            f.write(msg.encode())


def retry_handler(
    call_func: Callable[..., Response],
    call_args,
    call_kwargs,
    target_status: List[int] = list(range(200, 300)),
    retry: int = 0,
    sleep: float = 1,
    factor: float = 2.0,
    sleep_max: float = 0.0,
    stdout: List[Union[TextIO, BinaryIO]] = [sys.stdout],
    stderr: List[Union[TextIO, BinaryIO]] = [sys.stderr],
    request_id: str = "unknown",
) -> Response:
    try:
        # This is the requests function (requests.get, requests.post, ...)
        r: Response = call_func(*call_args, **call_kwargs)

    except requests.exceptions.RequestException as e:
        r = Response()
        r.reason = f"Runtime Exception"
        r._content = f"{e}".encode()
        r.status_code = 1

    if r.status_code not in target_status:
        if retry > 0:
            sleep_duration = round(sleep, 2)

            msg = f"HTTP request failed. Retry in {sleep_duration} seconds\n"
            write_to_files(stdout, msg)

            time.sleep(sleep_duration)

            increased_sleep = sleep * factor
            if sleep_max > 0 and increased_sleep > sleep_max:
                increased_sleep = sleep_max

            r = retry_handler(
                call_func,
                call_args,
                call_kwargs,
                target_status=target_status,
                retry=retry - 1,
                sleep=increased_sleep,
                factor=factor,
                sleep_max=sleep_max,
                stdout=stdout,
                stderr=stderr,
                request_id=request_id,
            )
        else:
            url = call_args[0]
            method = call_func.__name__.upper()

            msg = f"Error: HTTP request with id: '{request_id}' failed after {retry} retries; {method} {url}; "
            msg += (
                f"{r.status_code} {r.reason}; Response: {r.content.decode().strip()}\n"
            )

            write_to_files(stderr, msg)

    return r


# NOTE: put and post are identical here.


# NOTE: put and post are identical here.


class HttpClient:
    def __init__(
        self,
        retry: int = 0,
        sleep: float = 1,
        factor: float = 2.0,
        sleep_max: float = 0.0,
        stdout: List[Union[TextIO, BinaryIO]] = [sys.stdout],
        stderr: List[Union[TextIO, BinaryIO]] = [sys.stderr],
        request_id: str = "unknown",
    ) -> None:
        self.retry = retry
        self.sleep = sleep
        self.factor = factor
        self.sleep_max = sleep_max
        self.stdout = stdout
        self.stderr = stderr
        self.request_id = request_id

    def get_retry_handler_kwargs(self, local_values):
        kwargs = {}
        for k, v in local_values.items():
            if k not in RETRY_HANDLER_ARG_NAMES:
                continue
            if v is None:
                kwargs[k] = getattr(self, k)
        return kwargs

    def get_requests_args(_self, local_values, args_to_get):
        return [local_values[a] for a in args_to_get]

    def get_requests_kwargs(_self, local_values, args_to_get):
        d = {k: v for k, v in local_values.items() if k in args_to_get}
        return {**d, **local_values["requests_kwargs"]}

    def get(
        self,
        url: str,  # requests lib
        target_status: List[int],
        params: Optional[Any] = None,  # requests lib
        retry: Optional[int] = None,
        sleep: Optional[float] = None,
        factor: Optional[float] = None,
        sleep_max: Optional[float] = None,
        stdout: Optional[List[Union[TextIO, BinaryIO]]] = None,
        stderr: Optional[List[Union[TextIO, BinaryIO]]] = None,
        request_id: Optional[str] = None,
        **requests_kwargs,  # requests lib
    ) -> Response:
        """
        This call always returns a `requests.Response`, even if an exception is raised.
        Thses two fields are always set:
        - response.status_code (Contains the HTTP status code or `1` if an exception was raised.)
        - response.reason (Contains the HTTP message or the raised exception message.)
        """
        local_values = locals()
        requests_args = self.get_requests_args(local_values, ["url"])
        requests_kwargs = self.get_requests_kwargs(local_values, ["params"])
        retry_handler_kwargs = self.get_retry_handler_kwargs(local_values)

        return retry_handler(
            requests.get, requests_args, requests_kwargs, **retry_handler_kwargs
        )

    def post(
        self,
        url: str,
        target_status: List[int],
        json: Optional[Dict[str, Any]] = None,
        data: Optional[str] = None,
        params: Optional[Any] = None,  # requests lib
        retry: Optional[int] = None,
        sleep: Optional[float] = None,
        factor: Optional[float] = None,
        sleep_max: Optional[float] = None,
        stdout: Optional[List[Union[TextIO, BinaryIO]]] = None,
        stderr: Optional[List[Union[TextIO, BinaryIO]]] = None,
        request_id: Optional[str] = None,
        **requests_kwargs,  # requests lib
    ) -> Response:
        """
        This call always returns a `requests.Response`, even if an exception is raised.
        Thses two fields are always set:
        - response.status_code (Contains the HTTP status code or `1` if an exception was raised.)
        - response.reason (Contains the HTTP message or the raised exception message.)
        """
        local_values = locals()
        requests_args = self.get_requests_args(local_values, ["url"])
        requests_kwargs = self.get_requests_kwargs(local_values, ["json", "data"])
        retry_handler_kwargs = self.get_retry_handler_kwargs(local_values)

        return retry_handler(
            requests.post, requests_args, requests_kwargs, **retry_handler_kwargs
        )

    def put(
        self,
        url: str,
        target_status: List[int],
        json: Optional[Dict[str, Any]] = None,
        data: Optional[str] = None,
        params: Optional[Any] = None,  # requests lib
        retry: Optional[int] = None,
        sleep: Optional[float] = None,
        factor: Optional[float] = None,
        sleep_max: Optional[float] = None,
        stdout: Optional[List[Union[TextIO, BinaryIO]]] = None,
        stderr: Optional[List[Union[TextIO, BinaryIO]]] = None,
        request_id: Optional[str] = None,
        **requests_kwargs,  # requests lib
    ) -> Response:
        """
        This call always returns a `requests.Response`, even if an exception is raised.
        Thses two fields are always set:
        - response.status_code (Contains the HTTP status code or `1` if an exception was raised.)
        - response.reason (Contains the HTTP message or the raised exception message.)
        """
        local_values = locals()
        requests_args = self.get_requests_args(local_values, ["url"])
        requests_kwargs = self.get_requests_kwargs(local_values, ["json", "data"])
        retry_handler_kwargs = self.get_retry_handler_kwargs(local_values)

        return retry_handler(
            requests.put, requests_args, requests_kwargs, **retry_handler_kwargs
        )


_http_lib = HttpClient()

get = _http_lib.get
post = _http_lib.post
put = _http_lib.put
