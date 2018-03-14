import socket
import requests

confiaveis = ['www.google.com', 'www.yahoo.com', 'www.bb.com.br']
servidor = 'http://10.1.19.207:3000'

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

def servidor_online(host):
	try:
		req = requests.get(host)
		status = req.status_code
	except:
		#status criado para quando nao ha conexao com o servidor, baseado em http status codes
		status = 666
	if status != 666:
		return True
	else:
		return False
		

	
		
