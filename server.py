import socket

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST='127.0.0.1'
PORT=5000

serverSocket.bind((HOST, PORT))
serverSocket.listen(10)


def conn_handler(conn, addr):
    data = conn.recv(1024)
    parse_filename(data.decode())

def parse_filename(data):
    file_name = data.split("HTTP")[0].split(" /")[-1]
    print (file_name)

while True:
    print ("Waiting for a connection....")
    conn, addr = serverSocket.accept()
    print ("Connected to", addr[0], addr[1])
    conn_handler(conn, addr)
    #hello_msg = "<p>HEY BRO!</p>"
    #conn.sendto(hello_msg.encode('utf-8'),addr)
    #conn.close()
    continue


