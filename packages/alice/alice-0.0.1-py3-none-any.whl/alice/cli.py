import argparse
import socket
import sys
import os
import select
import time

__version__ = '0.0.1'

from textwrap import dedent

import yaml

SOCKET_TIMEOUT = 10  # seconds




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default="/", help='target path to write the file')
    parser.add_argument('-b', '--buffer-size', type=int, default=64, help='size of the buffer')
    parser.add_argument('-q', '--quiet', action='store_true', help='disable stdin pass-through')
    parser.add_argument('-i', '--ip', default='localhost', help='host')
    parser.add_argument('--port', type=int, default='8888', help='server port')
    parser.add_argument('-d', '--delay', type=float, default=0, help='delay before starting to send data')
    parser.add_argument('-u', '--username', type=str, default=None, help='username for the server')
    parser.add_argument('--token', type=str, default=None, help='access_token')

    args, unknown = parser.parse_known_args()

    alice(**vars(args))


HEADER_DELIM = "\n---\n"


def alice(ip, port, path=None, username=None, token=None, delay=None, quiet=False, buffer_size=64, codec=None):
    if hasattr(sys.stdin, 'buffer'):
        stdin = sys.stdin.buffer
    else:
        stdin = os.fdopen(sys.stdin.fileno(), 'r', 0)

    stdout = sys.stdout.buffer if hasattr(sys.stdout, 'buffer') else sys.stdout
    stderr = sys.stderr.buffer if hasattr(sys.stderr, 'buffer') else sys.stderr

    def read1(stream):
        if hasattr(stream, 'read1'):
            return stream.read1(buffer_size)
        else:
            # XXX is there a better way to do this without doing a bunch of syscalls?
            buf = []
            while len(buf) < buffer_size:
                ready, _, _ = select.select([stream], [], [], 0)  # poll
                if not ready:
                    break
                data = stream.read(1)
                if not data:
                    # even if we hit this case, it's fine: once we get to EOF, the
                        # fd is always ready (and will always return "")
                    break
                buf.append(data)
            return ''.join(buf)

    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.settimeout(SOCKET_TIMEOUT)
        conn.connect((ip, port))

        header = {}
        if path:
            header['path'] = path
        if username:
            header['username'] = username
        if token:
            header['access_token'] = token
        if codec:
            header['codec'] = codec

        header_str = yaml.dump(header) + HEADER_DELIM
        conn.sendall(header_str.encode())

        time.sleep(delay)

        # pipe data from stdin to server
        while True:
            ready, _, _ = select.select([conn, stdin], [], [])
            if stdin in ready:
                pipe_in = read1(stdin)
                if len(pipe_in) == 0:
                    # EOF
                    break
                conn.sendall(pipe_in)
                if not quiet:
                    stdout.write(pipe_in)
                    stdout.flush()
            elif conn in ready:
                conn.settimeout(SOCKET_TIMEOUT)
                data = conn.recv(buffer_size)
                print(data)
                stderr.write(data)
                stderr.flush()

    except KeyboardInterrupt:
        # exit silently with an error code
        exit(1)
    except socket.error as e:
        stderr.write(('socket error: %s\n' % e).encode('utf8'))
        stderr.flush()
        # continue running
        while True:
            try:
                pipe_in = read1(stdin)
                if len(pipe_in) == 0:
                    # EOF
                    break
                if not quiet:
                    stdout.write(pipe_in)
                    stdout.flush()
            except KeyboardInterrupt:
                exit(1)
