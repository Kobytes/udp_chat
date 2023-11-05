import argparse, socket

#TODO: The client and server both need to stay alive and not exit after each message sent/received.
#TODO: Both the client and the server need to print every message received from the other side.
#TODO: The server should not be chatting with more than one client at a time.

MAX_SIZE_BYTES = 65535

def server(port):
    pass
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = '127.0.0.1'
    sock.bind((hostname, port))
    print('Listening at {}'.format(sock.getsockname()))
    while True:
        data, clientAddress = sock.recvfrom(MAX_SIZE_BYTES)
        message = data.decode('ascii')
        print('The client at {} says {!r}'.format(clientAddress, message))
        msg_to_send = input('Input message to send to client:' )
        data = msg_to_send.encode('ascii')
        sock.sendto(data, clientAddress)

def client(port):
    pass
    host = '127.0.0.1'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        sock.connect((host, port))
        message = input('Input lowercase sentence: ')
        data = message.encode('ascii')
        sock.send(data)
        data = sock.recv(MAX_SIZE_BYTES)
        text = data.decode('ascii')
        print('The server replied with {!r}'.format(text))


if __name__ == '__main__':
    funcs = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='UDP client and server')
    parser.add_argument('functions', choices=funcs, help='client or server')
    parser.add_argument('-p', metavar='PORT', type=int, default=3000,
                        help='UDP port (default 3000)')
    args = parser.parse_args()
    function = funcs[args.functions]
    function(args.p)