import socket, threading

host = "127.0.0.1"
port = 50000

srvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srvr.bind((host, port))
srvr.listen()

clients = []
nicks = []

print("=" * 40)
print("|| === LAZY_SERVER === ||")
print("|| ===   v1.0.0    === ||")
print("=" * 40)

def broadcast(msg): # broadcast message to all clients
    for client in clients:
        client.send(msg)

def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except:
            idx = clients.index(client)
            clients.remove(client)
            nickname = nicks[idx]
            broadcast('{} left the chatroom!'.format(nickname).encode('ascii'))
            nicks.remove(nickname)
            break

def receive():
    while True:
        client, addr = srvr.accept()
        print('\nConnected with {}'.format(str(addr)))

        clients.append(client)

        client.send('NICK'.encode('ascii'))
        nick = client.recv(1022).decode('ascii')
        nicks.append(nick)

        print('Nickname is {}'.format(nick))
        broadcast('{} joined the chatroom!'.format(nick).encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))

        thread.start()

receive()