import socket

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST='127.0.0.1'
PORT=5000

serverSocket.bind((HOST, PORT))
serverSocket.listen(10)

def get_file(file_name):
        file = open(file_name, "r")
        return file.read()

def conn_handler(conn, addr):
    response_success = 'HTTP/1.1 200 OK \n'
    response_error = 'HTTP/1.1 404 ERROR NOT FOUND\n'
    data = conn.recv(1024)
    file_name = parse_filename(data.decode())
    try:
        conn.sendto(response_success.encode() + get_file(file_name) ,addr)
    except Exception as e:
        conn.sendto(response_error.encode(),addr)
    conn.close()

def parse_filename(data):
    file_name = data.split("HTTP")[0].split(" /")[-1]
    print (file_name)
    return file_name.replace(" ","")

while True:
    print ("Waiting for a connection....")
    conn, addr = serverSocket.accept()
    print ("Connected to", addr[0], addr[1])
    conn_handler(conn, addr)
    #hello_msg = "<p>HEY BRO!</p>"
    #conn.sendto(hello_msg.encode('utf-8'),addr)
    #conn.close()
    continue


