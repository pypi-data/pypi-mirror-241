import argparse
import paramiko
import sys
from rich.console import Console
from rich.panel import Panel
from sdj_remotetools.remote_cat import get_remote_file_content
from sdj_remotetools.utils import ssh_url_type


def rcat():
    """rcat command main routine"""

    # Define the command line arguments parser
    parser = argparse.ArgumentParser(
        prog='rcat',
        description='Works like \'cat\' but through SSH.',
    )
    parser.add_argument('remote_files', nargs='+', type=ssh_url_type,
                        help='SSH path to the remote files, space separate, ie: joe@remote.host:/path/to/file')
    parser.add_argument('-p', '--password', action='store_true', default=False, help='Ask user for password')
    parser.add_argument('-e', '--encoding', type=str, default='utf-8', help='Character encoding, ie: utf-8 (default)')
    parser.add_argument('-b', '--border', action='store_true', help='Draw border around the content')
    parser.add_argument('-s', '--syntax_highlight', action='store_true', default=False,
                        help='Enable console syntax highlighting')

    # Parse command line arguments
    args = parser.parse_args()

    # Define the rich stdout console
    stdout = Console(highlight=args.syntax_highlight)

    # Define the rich stderr console
    stderr = Console(stderr=True, highlight=False)

    # List that will store each output line
    outputs = []

    # Loops through each SSH url passed to rcat
    for remote_file_args in args.remote_files:
        ssh_args = remote_file_args
        ssh_args.update({'password': args.password, 'encoding': args.encoding})

        try:
            # Get content from remote file and add it to the outputs list
            file_content = get_remote_file_content(**ssh_args)
            if args.border:
                file_content = Panel(file_content, highlight=args.syntax_highlight, expand=False,
                                     title=remote_file_args['path_to_file'])
            stdout.print(file_content)
        except (paramiko.AuthenticationException, paramiko.SSHException) as e:
            stderr.print(f"SSH ERROR: {e} -> {remote_file_args['username']}@{remote_file_args['remote_host']} "
                         f"using password: {'Yes' if args.password else 'No'}", style="red")
            sys.exit(71)
        except paramiko.SFTPError as e:
            stderr.print(f"SFTP ERROR: {e}", style="red")
            sys.exit(71)
        except (FileNotFoundError, PermissionError) as e:
            stderr.print(f"FILE ERROR: {e} -> {remote_file_args['path_to_file']}", style="red")
            sys.exit(e.errno)


if __name__ == "__main__":
    pass
