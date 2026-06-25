from socket import *

# Porta do servidor
serverPort = 12000

# Cria socket TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

# Associa o socket à porta
serverSocket.bind(('', serverPort))

# Coloca o servidor em modo de escuta
serverSocket.listen(1)

print("Servidor pronto para receber conexões...")

while True:
    # Aguarda conexão do cliente
    connectionSocket, addr = serverSocket.accept()

    print(f"Conexão recebida de {addr}")

    # Recebe mensagem do cliente
    sentence = connectionSocket.recv(1024).decode()

    print("Mensagem recebida:", sentence)

    # Processa a mensagem (converte para maiúsculas)
    capitalizedSentence = sentence.upper()

    # Envia resposta ao cliente
    connectionSocket.send(capitalizedSentence.encode())

    # Fecha conexão
    connectionSocket.close()