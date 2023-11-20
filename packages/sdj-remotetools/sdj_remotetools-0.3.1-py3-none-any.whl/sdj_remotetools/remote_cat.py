import paramiko
import sys
from getpass import getpass


def get_remote_file_content(remote_host: str, username: str, password: bool, path_to_file: str,
                            encoding: str = 'utf8') -> str:
    """Gets and returns the content of a remote file through SSH

    Arguments:
        remote_host (str):  address or hostname of the remote host
        username (str):     username used to connect to the remote host
        password (bool):    should password authentication be used or not, default: False
        path_to_file (str): path to the file on the remote host
        encoding (str):     encoding to use to read the file content, default: 'utf-8'

    Returns:
        Content of the remote file as a string.
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        if password:
            user_password = getpass(f'({remote_host}) Password: ')
            ssh.connect(hostname=remote_host, username=username, password=user_password)
        else:
            ssh.connect(hostname=remote_host, username=username)

        ftp = ssh.open_sftp()
        content = ftp.open(path_to_file).read().decode(encoding)
        ssh.close()
        return content

    except (
            paramiko.SSHException,
            paramiko.AuthenticationException,
            paramiko.SFTPError,
            FileNotFoundError,
            PermissionError,
    ):
        raise
