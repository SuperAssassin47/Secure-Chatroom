import socket, threading

def chatroom_main():
    nick = input("Please enter your name: ")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 50000))

    def receive():
        while True:
            try:
                msg = client.recv(1022).decode('ascii')
                if msg == 'NICK':
                    client.send(nick.encode('ascii'))
                else:
                    print(msg)
            except:
                print("Oops! An error has occurred :(")
                client.close()
                break

    def write():
        while True:
            try:
                msg = '{}: {}'.format(nick, input(''))
                client.send(msg.encode('ascii'))
            except:
                print("Oops! User seemed to have disconnected :(")
                break

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()
