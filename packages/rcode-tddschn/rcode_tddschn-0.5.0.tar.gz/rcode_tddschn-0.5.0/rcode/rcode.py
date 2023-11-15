#!/usr/bin/env python3

import argparse
import os
import subprocess as sp
import time
from distutils.spawn import find_executable
from pathlib import Path
from os.path import expanduser
from typing import Iterable, List, NoReturn, Sequence, Tuple

from sshconf import read_ssh_config  # type: ignore
from rcode.config import vscode_release_channel_to_cli_name, RCODE_HOME

# IPC sockets will be filtered based when they were last accessed
# This gives an upper bound in seconds to the timestamps
DEFAULT_MAX_IDLE_TIME: int = 4 * 60 * 60


def fail(*msgs, retcode: int = 1) -> NoReturn:
    """Prints messages to stdout and exits the script."""
    for msg in msgs:
        print(msg)
    exit(retcode)


def is_socket_open(path: Path) -> bool:
    """Returns True if the UNIX socket exists and is currently listening."""
    try:
        proc = sp.run(
            ["socat", "-u", "OPEN:/dev/null", f"UNIX-CONNECT:{path.resolve()}"],
            stdout=sp.PIPE,
            stderr=sp.PIPE,
        )
        return proc.returncode == 0
    except:
        return False


def sort_by_access_timestamp(paths: Iterable[Path]) -> List[Tuple[float, Path]]:
    """Returns a list of tuples (last_accessed_ts, path) sorted by the former."""
    paths_list = [(p.stat().st_atime, p) for p in paths]
    paths_list = sorted(paths_list, reverse=True)
    return paths_list


def next_open_socket(socks: Sequence[Path]) -> Path:
    """Iterates over the list and returns the first socket that is listening."""
    try:
        return next((sock for sock in socks if is_socket_open(sock)))
    except StopIteration:
        fail(
            "Could not find an open VS Code IPC socket.",
            "",
            "Please make sure to connect to this machine with a standard "
            + "VS Code remote SSH session before using this tool.",
        )


def is_remote_vscode() -> bool:
    code_repos = Path.home().glob(".vscode-server/bin/*")
    return len(list(code_repos)) > 0 and os.getenv("SSH_CLIENT")


IS_REMOTE_VSCODE = is_remote_vscode()


# def get_code_binary() -> Path:
#     """Returns the path to the most recently accessed code executable."""
#
#     # Every entry in ~/.vscode-server/bin corresponds to a commit id
#     # Pick the most recent one
#     code_repos = sort_by_access_timestamp(Path.home().glob(".vscode-server/bin/*"))
#     if len(code_repos) == 0:
#         fail(
#             "No installation of VS Code Server detected!",
#             "",
#             "Please connect to this machine through a remote SSH session and try again.",
#             "Afterwards there should exist a folder under ~/.vscode-server",
#         )
#
#     _, code_repo = code_repos[0]
#     path = code_repo / "bin" / "code"
#     if os.path.exists(path):
#         return path
#     return code_repo / "bin" / "remote-cli" / "code"
#
#
def get_code_binary(release_channel: str) -> Path:
    """Returns the path to the most recently accessed code executable."""
    cli_name = vscode_release_channel_to_cli_name.get(release_channel, "code")

    # Every entry in ~/.vscode-server/bin corresponds to a commit id
    # Pick the most recent one
    code_repos = sort_by_access_timestamp(Path.home().glob(f".vscode-server/bin/*"))
    if len(code_repos) == 0:
        fail(
            f"No installation of VS Code Server detected for {release_channel}!",
            "",
            "Please connect to this machine through a remote SSH session and try again.",
            f"Afterwards there should exist a folder under ~/.vscode-server",
        )

    _, code_repo = code_repos[0]
    path = code_repo / "bin" / cli_name
    if os.path.exists(path):
        return path
    if os.path.exists(code_repo / "bin" / "remote-cli" / cli_name):
        return code_repo / "bin" / "remote-cli" / cli_name
    fail(f"The VS Code {release_channel} binary was not found.")


def get_ipc_socket(max_idle_time: int = DEFAULT_MAX_IDLE_TIME) -> Path:
    """Returns the path to the most recently accessed IPC socket."""

    # List all possible sockets for the current user
    # Some of these are obsolete and not actively listening anymore
    uid = os.getuid()
    socks = sort_by_access_timestamp(
        Path(f"/run/user/{uid}/").glob("vscode-ipc-*.sock")
    )

    # Only consider the ones that were active N seconds ago
    now = time.time()
    sock_list = [sock for ts, sock in socks if now - ts <= max_idle_time]

    # Find the first socket that is open, most recently accessed first
    return next_open_socket(sock_list)


def check_for_binaries() -> None:
    """Verifies that all required binaries are available in $PATH."""
    if not find_executable("socat"):
        fail('"socat" not found in $PATH, but is required for code-connect')


def run_remote(
    dir_name,
    max_idle_time: int = DEFAULT_MAX_IDLE_TIME,
    release_channel: str = "stable",
) -> NoReturn:
    if not dir_name:
        raise Exception("need dir name here")
    # Fetch the path of the "code" executable
    # and determine an active IPC socket to use
    if IS_REMOTE_VSCODE:
        check_for_binaries()
        code_binary = get_code_binary(release_channel=release_channel)
        ipc_socket = get_ipc_socket(max_idle_time)

        args = [str(code_binary)]
        args.append(dir_name)
        os.environ["VSCODE_IPC_HOOK_CLI"] = str(ipc_socket)

        # run the "code" executable with the proper environment variable set
        # stdout/stderr remain connected to the current process
        proc = sp.run(args)
        # return the same exit code as the wrapped process
        exit(proc.returncode)


def run_loacl(
    dir_name,
    remote_name=None,
    is_latest=False,
    shortcut_name=None,
    open_shortcut_name=None,
    release_channel: str = "stable",
):
    # run local to open remote
    rcode_home = Path.home() / ".rcode"
    cli_name = vscode_release_channel_to_cli_name.get(release_channel, "code")
    ssh_remote = "vscode-remote://ssh-remote+{remote_name}{remote_dir}"
    rcode_used_list = []
    if os.path.exists(rcode_home):
        with open(rcode_home) as f:
            rcode_used_list = list(f.read().splitlines())

    if is_latest:
        if rcode_used_list:
            ssh_remote_latest = rcode_used_list[-1].split(",")[-1].strip()
            proc = sp.run([cli_name, "--folder-uri", ssh_remote_latest])
            exit(proc.returncode)
        else:
            print("You haven't used rcode before, please try using it once.")
            return
    if open_shortcut_name and rcode_used_list:
        for l in rcode_used_list:
            name, server = l.split(",")
            if open_shortcut_name.strip() == name.strip():
                proc = sp.run([cli_name, "--folder-uri", server.strip()])
                # then add it to the latest
                with open(rcode_home, "a") as f:
                    f.write(f"latest,{server}{str(os.linesep)}")
                exit(proc.returncode)
        else:
            raise Exception("No shortcut name found in your addition.")

    sshs = read_ssh_config(expanduser("~/.ssh/config"))
    hosts = sshs.hosts()
    remote_name = remote_name
    if remote_name not in hosts:
        raise Exception("Please config your .ssh config to use this")
    dir_name = dir_name
    local_home_dir = expanduser("~")
    if dir_name.startswith(local_home_dir):
        user_name = sshs.host(remote_name).get("user", "root")
        # replace with the remote ~
        dir_name = str(dir_name).replace(local_home_dir, f"/home/{user_name}")
    ssh_remote = ssh_remote.format(remote_name=remote_name, remote_dir=dir_name)
    with open(rcode_home, "a") as f:
        if shortcut_name:
            f.write(f"{shortcut_name},{ssh_remote}{str(os.linesep)}")
        else:
            f.write(f"latest,{ssh_remote}{str(os.linesep)}")

    proc = sp.run([cli_name, "--folder-uri", ssh_remote])
    exit(proc.returncode)


def list_shortcuts(rcode_home: Path) -> None:
    if rcode_home.exists():
        with rcode_home.open() as f:
            for line in f:
                print(line, end="")  # Print each line in the .rcode file
    else:
        print("No shortcuts have been set.")


def delete_shortcut(rcode_home: Path, shortcut_name: str) -> None:
    if not rcode_home.exists():
        print("Shortcut file does not exist.")
        return

    with rcode_home.open("r") as f:
        lines = f.readlines()
    with rcode_home.open("w") as f:
        for line in lines:
            if line.split(",")[0].strip() != shortcut_name.strip():
                f.write(line)
            else:
                print(f"Deleted shortcut: {shortcut_name}")


def delete_all_shortcuts(rcode_home: Path) -> None:
    confirm = input("Are you sure you want to delete all shortcuts? (y/n): ")
    if confirm.lower() == "y":
        rcode_home.unlink()
        print("All shortcuts have been deleted.")
    else:
        print("Deletion cancelled.")


def main():
    parser = argparse.ArgumentParser(
        description="A command line tool to open directories in VSCode remotely or locally."
    )

    parser.add_argument(
        "dir",
        help="The local directory path to open in VSCode or the remote directory path when used with a host.",
        nargs="?",
    )

    parser.add_argument(
        "host",
        help="The SSH hostname as specified in your .ssh/config to open a remote directory in VSCode.",
        nargs="?",
    )
    parser.add_argument(
        "-r",
        "--release",
        dest="release_channel",
        choices=["stable", "insiders"],
        help="VS Code release channel to use (stable or insiders)",
        required=False,
        default="stable",
    )
    parser.add_argument(
        "-l",
        "--latest",
        dest="is_latest",
        action="store_true",
        help="Open the most recently used remote directory.",
    )
    parser.add_argument(
        "-s",
        "-sn",
        "--shortcut_name",
        dest="shortcut_name",
        help=f"rcode host dir -s <shortcut_name> | Add a shortcut name for the remote directory to quickly access it later. | Saved to {RCODE_HOME}",
        type=str,
        required=False,
    )
    parser.add_argument(
        "-o",
        "-os",
        "--open_shortcut",
        dest="open_shortcut",
        type=str,
        required=False,
        help="Open a remote directory quickly using the previously saved shortcut name.",
    )
    parser.add_argument(
        "-L",
        "--list",
        dest="list_shortcuts",
        action="store_true",
        help="List all configured shortcuts",
    )
    parser.add_argument(
        "-d",
        "--delete",
        dest="delete_shortcut",
        help="Delete a shortcut by name",
        type=str,
        required=False,
    )
    parser.add_argument(
        "-D",
        "--delete-all",
        dest="delete_all",
        action="store_true",
        help="Delete all shortcuts after confirmation",
    )
    options = parser.parse_args()
    if options.list_shortcuts:
        list_shortcuts(RCODE_HOME)
    elif options.delete_shortcut:
        delete_shortcut(RCODE_HOME, options.delete_shortcut)
    elif options.delete_all:
        delete_all_shortcuts(RCODE_HOME)
    elif IS_REMOTE_VSCODE:
        run_remote(options.dir, release_channel=options.release_channel)
    else:
        run_loacl(
            options.host,
            options.dir,
            is_latest=options.is_latest,
            shortcut_name=options.shortcut_name,
            open_shortcut_name=options.open_shortcut,
            release_channel=options.release_channel,
        )


if __name__ == "__main__":
    main()
