from pymongo import MongoClient

def conexao_local_banco(doc):
	try:
		cliente = MongoClient('localhost', 27017)
		banco = cliente.banco_database
		dados = banco.dados
		dados.save(doc)
	except Exception as error:
		print(error)
	
