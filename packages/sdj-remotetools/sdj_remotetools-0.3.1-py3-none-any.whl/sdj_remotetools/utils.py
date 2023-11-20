import re
from argparse import ArgumentTypeError as ArgparseArgumentError


def ssh_url_type(ssh_url: str) -> dict[str]:
    """Parses an SSH url and returns a dictionary of values

    Arguments:
        ssh_url (str): an SSH url, ie: user@host.tld:/path/to/file

    Returns:
        A dictionary of the url fields, ie:
        {
            'username': 'user',
            'remote_host': 'host.tld',
            'path_to_file': '/path/to/file',
        }
    """
    url_regex = '^(?P<username>\S+)@(?P<remote_host>\S+):(?P<path_to_file>/\S+)'
    result = re.search(url_regex, ssh_url)

    if result is None:
        raise ArgparseArgumentError(f'{ssh_url!r} is not a valid SSH url')

    return result.groupdict()
