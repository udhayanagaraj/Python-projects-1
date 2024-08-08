import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            # Receive message from server
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received: {message}")
            else:
                break
        except:
            break

def send_messages(client_socket):
    while True:
        message = input("Enter the message: ")
        try:
            client_socket.send(message.encode('utf-8'))
        except:
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 5555))

    print("Connected to the server")

    # Create threads for receiving and sending messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()

if __name__ == "__main__":
    main()

