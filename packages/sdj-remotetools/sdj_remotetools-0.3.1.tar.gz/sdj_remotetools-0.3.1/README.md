![](https://img.shields.io/badge/python-3.9-blue) ![](https://img.shields.io/badge/python-3.10-blue) ![](https://img.shields.io/badge/python-3.11-blue) ![](https://img.shields.io/badge/python-3.12-blue)
# SDJ-REMOTETOOLS

## Description
`sdj-remotetools` is a python collection of tools working through SSH.

## Tools
All tools handle SSH connection using Paramiko.

### rcat
Works like 'cat' command but for remote files through SSH and with few enhancements
```
usage: rcat [-h] [-p] [-e ENCODING] [-b] [-s] remote_files [remote_files ...]

Works like 'cat' but through SSH.

positional arguments:
  remote_files          SSH path to the remote files, space separate, ie: joe@remote.host:/path/to/file

options:
  -h, --help            show this help message and exit
  -p, --password        Ask user for password
  -e ENCODING, --encoding ENCODING
                        Character encoding, ie: utf-8 (default)
  -b, --border          Draw border around the content
  -s, --syntax_highlight
                        Enable console syntax highlighting
```
