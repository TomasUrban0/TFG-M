import subprocess
import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 1
server_sock.bind(("", port))
server_sock.listen(1)

print("Esperando conexión en RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()
print("Aceptada conexión desde ", client_info)

try:
    while True:
        data = client_sock.recv(1024)
        if len(data) == 0: break
        print("Recibido [%s]" % data)

        # Decodifica los datos y elimina los espacios en blanco al principio y al final
        command = data.decode().strip()

        # Comprueba los datos recibidos y envía una respuesta
        if command.startswith("nmcli dev wifi connect"):
            output = subprocess.check_output(command, shell=True)
            client_sock.send(output)
        elif command == "ip a":
            output = subprocess.check_output(command, shell=True)
            client_sock.send(output)
        elif command == "df -h":
            output = subprocess.check_output(command, shell=True)
            client_sock.send(output)
        elif command == "sensors":
            output = subprocess.check_output(command, shell=True)
            client_sock.send(output)
        elif command.startswith("sudo ifconfig"):
            output = subprocess.check_output(command, shell=True)
            client_sock.send(output)
        elif command == "htop":  # Nuevo comando
            output = subprocess.check_output("top -b -n 1 | head -n 12", shell=True)
            client_sock.send(output)

except IOError:
    pass

print("Desconectado")

client_sock.close()
server_sock.close()
print("Todo cerrado")