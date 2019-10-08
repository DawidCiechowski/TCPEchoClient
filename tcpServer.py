import socket 
import threading

HOST  = "" # Inser IP Address
PORT = 65432 #Default port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    print("Listening on port " + str(PORT) + "...")

    conn, addr = sock.accept()

    with conn:
        print("Connected by,", addr)
        while True:
            data = conn.recv(4096)
            if not data:
                break

            print("Received: " + repr(data))            
            conn.sendall(b'Echoing back:' +  data)


