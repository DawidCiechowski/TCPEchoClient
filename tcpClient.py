import socket


HOST  = "" #Insert IP Address
PORT = 65432 #Default port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:


    sock.connect((HOST, PORT))
    sock.sendall(b'') #Enter the message you wish to echo.


    data = sock.recv(4096)


print("Received: " +  repr(data))


