import socket
import argparse

parser = argparse.ArgumentParser(description="Client to retrieve information from server")
parser.add_argument('--host', dest="host", required=True)
parser.add_argument('--port', dest="port", type=int, required=True)
parser.add_argument('--file', dest="file", required=False)

called_args = parser.parse_args()
host = called_args.host or 'localhost'
port = called_args.port or '8080'
file = called_args.file

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print err

s.connect((host,port))

while True:
    if file is None:
        file = input("Type in the filename (in quotes):")
    else:
        file = 'index.html'

    try:
        s.sendall("GET /" + file + " HTTP/1.1\r\n\r\n")
    except socket.error:
        print("Something went wrong")
    reply = s.recv(16384)
    print(reply)
    s.close()
    break

