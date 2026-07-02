from socket import *
import time
from datetime import datetime

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("Servidor pronto para receber conexões...")

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Conexão recebida de {addr}")

    data = connectionSocket.recv(1024).decode()
    parts = data.split('|')
    sentence = parts[0]
    client_send_time = float(parts[1])

    print("Mensagem recebida:", sentence)

    capitalizedSentence = sentence.upper()
    server_response_time = time.time()
    msg_size = len(sentence.encode('utf-8'))

    # Monta resposta
    response = f"{capitalizedSentence}|{addr}|{client_send_time}|{server_response_time}|{msg_size}"
    connectionSocket.send(response.encode())
    connectionSocket.close()