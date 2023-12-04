import socket

# Client configuration
host = '127.0.0.1'
port = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Receive and display the response from the server
response = client_socket.recv(1024).decode('utf-8')
file_extension = ''

if response.startswith("File is about to be sent"):
    file_extension = response[len("File is about to be sent"):]
    # Specify the path to save the received file with the provided extension
    file_path = f'received_file{file_extension}' if file_extension else 'received_file'

    # Receive the file data
    file_data = b""
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        file_data += data

    # Save the file with the determined or original extension
    with open(file_path, 'wb') as file:
        file.write(file_data)

    print(f"File received and saved as '{file_path}'.")

elif response == "Error: File not found":
    print("Server reports that the file is not found.")

# Close the client socket
client_socket.close()
