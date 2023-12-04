import socket
import signal
import sys
import os

# Server configuration
host = '127.0.0.1'
port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)
print(f"Server is listening on {host}:{port}")

def signal_handler(sig, frame):
    print("\nCtrl+C pressed. Exiting...")
    if 'client_socket' in locals():
        client_socket.close()  # Close the client socket
    server_socket.close()  # Close the server socket
    sys.exit(0)

# Register the Ctrl+C signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    while True:
        # Accept a connection
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        print("All Tasks you can run:\nRun-wifi\nRun-ss\nRun-upload")
        message = str(input("Message you want to send to the client: "))
        client_socket.send(message.encode('utf-8'))
        while True:
            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            elif data == "Message is about to be sended":
                print("Receiving an image...")
                image_data = b""
                while True:
                    chunk = client_socket.recv(1024)
                    if not chunk:
                        break
                    image_data += chunk

                # Specify the path where you want to save the received image
                image_file_path = 'ss-client.png'  # You can change the file name and extension

                # Write the received image data to a file
                with open(image_file_path, 'wb') as image_file:
                    image_file.write(image_data)

                print("Image received and saved as:", image_file_path)
                break

            elif data == "Error":
                break
            print(f"Received message: {data}")
            # Process the received message
            if message == "Run-wifi":
                response = "Run-wifi"
            elif message == "Run-ss":
                response = "Run-ss"
            elif message == "Run-upload":
                file_path = "C:/Users/Vojtěch Vlasák/Desktop/Python/AllToolsInOne/ideas.txt"  # Change the file path as needed
                file_extension = os.path.splitext(file_path)[1]
                try:
                    with open(file_path, 'rb') as file:
                        file_data = file.read()
                        client_socket.send(f"File is about to be sent{file_extension}".encode("utf-8"))
                        client_socket.send(file_data)
                    print(f"File '{file_path}' has been sent to the client.")
                except FileNotFoundError:
                    client_socket.send("Error: File not found".encode("utf-8"))
                response = "Upload"
            # Send the response back to the client
            client_socket.send(response.encode('utf-8'))

except KeyboardInterrupt:
    print("Ctrl+C pressed. Exiting...")

finally:
    # Close the client and server sockets
    if 'client_socket' in locals():
        client_socket.close()
    server_socket.close()
