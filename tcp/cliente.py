from socket import *

serverName = 'localhost'
serverPort = 12000

# Cria socket TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# Estabelece conexão com o servidor
clientSocket.connect((serverName, serverPort))

# Lê mensagem do usuário
sentence = input("Digite uma mensagem: ")

# Envia mensagem ao servidor
clientSocket.send(sentence.encode())

# Recebe resposta
modifiedSentence = clientSocket.recv(1024)

print("Resposta do servidor:", modifiedSentence.decode())

# Fecha conexão
clientSocket.close()