import socket 
import threading



def adder(n):  
    return lambda x: x + n

adder_3 = adder(3)
adder_5 = adder(5)
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
            try:
                print(adder_3(int(data)))
                print(adder_5(int(data)))
            except ValueError:
                print("Not a number")
            
            conn.sendall(b'Echoing back:' +  data)


