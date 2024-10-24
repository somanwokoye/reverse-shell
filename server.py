import socket
import sys


# Defining a Socket to connect two computers
def create_socket() -> socket.socket:
    try:
        s = socket.socket()
        return s
    except socket.error as error:
        print(f"Socket creation error: {error}")
        raise


host: str = ""
port: int = 9999
s = create_socket()


# binding the socket and listening for connections
def bind_socket() -> None:
    try:

        print(f"Binding the port {port}")

        s.bind((host, port))
        s.listen(5)

    except socket.error as error:
        print(f"Socket Binding error {error}, Retrying...")
        bind_socket()


# Establish a connection with client
def socket_accept() -> None:
    conn, address = s.accept()
    print(f"Connection has been established | IP {address[0]} | Port {address[1]}")

    send_commands(conn)
    conn.close()


def send_commands(conn: socket.socket) -> None:
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            sys.exit()
        if (
            len(str.encode(cmd)) > 0
        ):  ## need to encode to string also checks if characters are greater than one
            conn.send(str.encode(cmd))
            client_response: str = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    bind_socket()
    socket_accept()


main()
