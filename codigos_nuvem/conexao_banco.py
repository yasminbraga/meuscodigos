from pymongo import MongoClient

def save_banco_local(doc):
	try:
		conexao = MongoClient('localhost', 27017)
		banco = conexao.banco_local_raspberry
		dados = banco.dados
		dados.save(doc)
	except Exception as error:
		print(error)

def get_banco_local():
	dados_salvos = dados.find()
	return dados_salvos()


