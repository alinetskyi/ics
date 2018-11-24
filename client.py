import socket
import argparse

parser = argparse.ArgumentParser(description="FTP client to retrieve files from server")
parser.add_argument('--host', dest="host", required=True)
parser.add_argument('--port', dest="port", type=int, required=True)
parser.add_argument('--command', dest="command", required=False)

called_args = parser.parse_args()
host = called_args.host or 'localhost'
port = called_args.port or '8080'
command = called_args.command

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print err

s.connect((host,port))

while True:
    if command is None:
        command = input("Type in the command (in quotes):")
    else:
        command = 'pwd'

    try:
        s.sendall(command)
    except socket.error:
        print("Something went wrong")
    reply = s.recv(16384)
    print(reply)
    s.close()
    break

