#!/usr/bin/env python3
import os
import sys
import json
import platform
from pathlib import Path
import urllib.request, urllib.parse, urllib.error
import http.client
from .version import __version__


def get_title():
    user = os.environ.get('USER', '')
    host = platform.node()
    return '{}@{}'.format(user, host)


def pushover(title, msg):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    with open(os.environ['HOME'] + '/.pushover.json', 'r') as f:
        config = json.load(f)

    conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
            "token"   : config['token'],
            "user"    : config['user'],
            "title"   : title,
            "message" : msg,
        }), {"Content-type": "application/x-www-form-urlencoded"})
    conn.getresponse()


def run():
    import argparse
    parser = argparse.ArgumentParser(
        prog='pushover', description='send messages using pushover service',
        epilog='please provide token and user in JSON format at $HOME/.pushover.json',
    )
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s v{version}'.format(version=__version__))
    parser.add_argument('-t', '--title', dest='title', default=get_title(),
                        help='Title of message, (default: user@hostname)')
    parser.add_argument('-f', '--force', dest='force', action='store_true',
                        help='Force sending message using localhost')
    parser.add_argument('msg', metavar='message',
                        help='message')
    args = parser.parse_args()

    # Check hostname
    if args.force or platform.node() == 'mu02':
        pushover(args.title, args.msg)
    else:
        cwd = Path().resolve()
        title = "'" + args.title + "'"
        msg = "'" + args.msg + "'"
        cmd = f'ssh 192.168.0.30 "source /etc/profile; cd {cwd}; {sys.argv[0]} -t {title} {msg}"'
        os.system(cmd)
