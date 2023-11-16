import os
import argparse
import pathlib

from . import remote


parser = argparse.ArgumentParser()
parser.add_argument(
    "hostname",
    type=str,
    help="Hostname of computer to grab info from.",
)
username_cli_argname = "--username"
username_env_varname = "NP_MONITOR_USERNAME"
parser.add_argument(
    username_cli_argname,
    default=os.environ.get(username_env_varname),
    type=str,
)
password_cli_argname = "--password"
password_env_varname = "NP_MONITOR_PASSWORD"
parser.add_argument(
    password_cli_argname,
    default=os.environ.get(password_env_varname),
    type=str,
)
parser.add_argument(
    "--output_directory",
    type=pathlib.Path,
    default=pathlib.Path("./"),
    help="Directory to save dxdiag output."
)

args = parser.parse_args()

error_template = "%s must be set via commandline argument: %s or environment variable: %s"
if args.username is None:
    raise RuntimeError(
        error_template % (
            "Remote host username",
            username_cli_argname,
            username_env_varname,
        )
    )

if args.password is None:
    raise RuntimeError(
        error_template % (
            "Remote host password",
            password_cli_argname,
            password_env_varname,
        )
    )

remote.run_get_dxdiag(
    args.hostname,
    args.username,
    args.password,
    args.output_directory,
)