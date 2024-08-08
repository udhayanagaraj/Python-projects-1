import socket
import threading

# List to keep track of connected clients
clients = []

def handle_client(client_socket):
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received message: {message}")
                broadcast(message, client_socket)
            else:
                remove(client_socket)
        except:
            continue

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove(client)

def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))
    server.listen(5)
    print("Server started and listening on port 5555")

    while True:
        client_socket, client_address = server.accept()
        clients.append(client_socket)
        print(f"Connection established with {client_address}")

        # Create a new thread to handle the client
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    main()

