import socket

# Set IP and port to listen on
server_ip = '10.10.10.1'
server_port = 8080

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the IP and port to the server
server_socket.bind((server_ip, server_port))

# Start listening for connections
server_socket.listen(1)
print(f"[] Listening on {server_ip}:{server_port}")

# Accept the incoming connection
client_socket, client_address = server_socket.accept()
print(f"[] Accepted connection from {client_address}:{client_address}")

# Receive data and execute commands
while True:
    command = input("Shell: ")
    if command.lower() == "exit":
        break

    client_socket.send(command.encode())
    response = client_socket.recv(2048)
    print(response.decode('utf-8'))

# Close the sockets
client_socket.close()
server_socket.close()
