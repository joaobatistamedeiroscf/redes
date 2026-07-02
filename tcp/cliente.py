from socket import *
import time
from datetime import datetime

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input("Digite uma mensagem: ")

# Tempo de envio (preciso - para cálculo de RTT)
send_time = time.time()

# Envia mensagem + timestamp
data_to_send = f"{sentence}|{send_time}"
clientSocket.send(data_to_send.encode())

# Recebe resposta
response = clientSocket.recv(1024).decode()

receive_time = time.time()

# Processa resposta
parts = response.split('|')
modified_sentence = parts[0]
client_addr = parts[1]
client_send_ts = float(parts[2])
server_resp_ts = float(parts[3])
msg_size = int(parts[4])

rtt = receive_time - send_time

# === Formatação legível ===
def format_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%d-%m-%y %H:%M:%S.%f")[:-3]

print("=== Resposta do Servidor ===")
print("Mensagem processada:", modified_sentence)
print("Endereço do cliente:", client_addr)
print(f"Tempo envio (cliente): {format_time(client_send_ts)}")
print(f"Tempo resposta (servidor): {format_time(server_resp_ts)}")
print(f"Intervalo (RTT): {rtt:.6f} segundos")
print(f"Tamanho da mensagem: {msg_size} bytes ({msg_size * 8} bits)")

clientSocket.close()