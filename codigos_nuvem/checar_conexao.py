import socket

confiaveis = ['www.google.com', 'www.yahoo.com', 'www.bb.com.br']

def checar_conexao():
	global confiaveis
	for host in confiaveis:
		connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connection.settimeout(.5)
		try:
			connection_connect = connection.connect_ex((host, 80))
			if connection_connect == 0:
				return True
		except:
			pass
		connection.close()
	return False



