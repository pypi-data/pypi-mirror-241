import argparse
import json
import sys

from mewo_http_client import lib


def validate_arg_given_once(flag_name, value):
    if len(value) > 1:
        sys.stderr.write(f"Error: '--{flag_name}' was given more than once.\n")
        sys.exit(1)


def get_args():
    parser = argparse.ArgumentParser(
        prog="mewo-http-client-post",
        description="Send a mewo service to service POST request.",
        epilog="",
    )

    parser.add_argument("method")
    parser.add_argument("-u", "--url", required=True, action="append")
    parser.add_argument("-j", "--json", required=False, action="append")
    parser.add_argument("-d", "--data", required=False, action="append")
    parser.add_argument("-r", "--retry", required=False, type=int)
    parser.add_argument("-p", "--sleep", required=False, type=float)
    parser.add_argument("-c", "--factor", required=False, type=float)
    parser.add_argument("-m", "--sleep_max", required=False, type=float)

    args = {}

    for flag_name, value in vars(parser.parse_args()).items():
        if isinstance(value, list):
            validate_arg_given_once(flag_name, value)
            args[flag_name] = value[0]
        else:
            args[flag_name] = value

    positional_args = [args["url"]]

    del args["url"]

    kwargs = {k: v for k, v in args.items() if v}

    if kwargs.get("json"):
        kwargs["json"] = json.loads(kwargs["json"])

    return positional_args, kwargs


def run():
    args, kwargs = get_args()
    print(kwargs)

    method = kwargs["method"]
    del kwargs["method"]

    print(args, kwargs)

    if method == "post":
        r = lib.post(*args, **kwargs)
        for k, v in vars(r).items():
            print(k, v)
