import socket

ip = input("Endereço de IP a ser escaneado: ")

start_port = int(input("Porta de inicio: "))
end_port = int(input("Porta final: "))


for i in range(start_port, end_port):
	socket.setdefaulttimeout(0.5)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		if s.connect_ex((ip, i)) == 0:
			service = socket.getservbyport(i, "tcp")
			print(f"Serviço {service} rodando na porta {i}")
	except:
		pass
	s.close()
print("As outras portas estão fechadas")
		