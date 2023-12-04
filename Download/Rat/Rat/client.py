import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))

    while True:
        message = input("Enter your message (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        client.send(message.encode('utf-8'))

    client.close()

if __name__ == "__main__":
    start_client()
