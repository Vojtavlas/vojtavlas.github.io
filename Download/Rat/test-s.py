import socket
import os

# Server configuration
host = '127.0.0.1'
port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)
print(f"Server is listening on {host}:{port}")

# Accept a connection
client_socket, addr = server_socket.accept()
print(f"Connection from {addr}")

# Specify the path to the file you want to send
file_path = "C:/Users/Vojtěch Vlasák/Pictures/Screenshots/Screenshot 2023-10-28 224301.png"  # Change the file path as needed
file_extension = os.path.splitext(file_path)[1]

try:
    with open(file_path, 'rb') as file:
        file_data = file.read()
        client_socket.send(f"File is about to be sent{file_extension}".encode("utf-8"))
        client_socket.send(file_data)
    print(f"File '{file_path}' has been sent to the client.")

except FileNotFoundError:
    client_socket.send("Error: File not found".encode("utf-8"))

# Close the client and server sockets
client_socket.close()
server_socket.close()
