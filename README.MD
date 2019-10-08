# Basic Server-Client Echo TCP connection in Python

## General

 - Basic echo call socket connection. Two files: one dealing with server side, listening to clients and connecting the sockets, and echoing the message - sent by the client - right back; second being a client server side connecting to the server side; sending and receiving the echo message.

 ## Usage

- Enter the IP address (the same one into both files) and the message you wish to send at client side.
- Run two files at the same time: server side first, then client. 
- Server should be listening until the client connects, then print the received message. Client should print the received echoed message.