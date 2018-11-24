import socket
import os
import subprocess

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST=''
PORT=5000

serverSocket.bind((HOST, PORT))
serverSocket.listen(10)

def execute_command(command):
    result = subprocess.check_output(command, shell=True)
    return result

def conn_handler(conn, addr):
    response_success = '200 action successfully completed \n'
    response_error = "400 command wasn't executed\n"
    data = conn.recv(1024) if True else "pwd"
    command = data
    print command
    try:
        conn.sendto(response_success.encode() + execute_command(command) ,addr)
    except Exception as e:
        conn.sendto(response_error.encode(),addr)
    conn.close()

def parse_command(data):
    data

while True:
    print ("Waiting for a connection....")
    conn, addr = serverSocket.accept()
    print ("Connected to", addr[0], addr[1])
    conn_handler(conn, addr)
    continue


