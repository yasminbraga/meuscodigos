from pymongo import MongoClient
		
#a variavel conexao faz conexao com o banco
conexao = MongoClient('localhost', 27017)
#a variavel banco conecta com o banco chamado banco_local_raspberry
banco = conexao.banco_local_raspberry
#a variavel dados guarda a colecao dados que esta no banco
dados = banco.dados

def save_banco_local(doc):
	#faz conexao com o banco de dados
	try:
		#salva os dados no banco
		dados.insert_one(doc)
	#se der erro na conexao com o banco vai printar qual o erro	
	except Exception as error:
		print(error)

def get_banco_local():
	#dados_salvos guarda os dados que serao encontrados dentro da colecao "dados"
	dados_salvos = dados.find_one()
	#retorna os dados que serao enviados pela internet assim que a conexao for reestabelecida
	return dados_salvos

def num_de_documentos():
	num_documentos = dados.count()
	return num_documentos

def excluir_dados_banco(dado):
	#remove os dados da colecao "dados"
	dados.remove(dado)




