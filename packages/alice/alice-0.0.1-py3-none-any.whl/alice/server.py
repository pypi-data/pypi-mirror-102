import asyncio
import yaml
import sys

block_size = 64


async def handle_echo(reader, writer):
    header_str = None
    codec = "utf-8"
    data_buffer = b""
    while True:
        data = await reader.read(block_size)
        if data == b'':
            break

        data_buffer +=data
        if header_str is None:
            *header_str, data_buffer = data_buffer.split(b'\n---\n')
            if header_str:
                print("header >>>", header_str)
                header = yaml.load(b''.join(header_str).decode('utf-8'), Loader=yaml.FullLoader)
                print(header)
                codec = header.get('codec', codec)
        try:
            message = data_buffer.decode(codec)
        except UnicodeDecodeError:
            pass

        # addr = writer.get_extra_info('peername')
        print(message, end="")
        sys.stdout.flush()

    writer.close()
    print("Connection is closed.")
    sys.stdout.flush()


async def main():
    server = await asyncio.start_server(handle_echo, '0.0.0.0', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()


asyncio.run(main())
