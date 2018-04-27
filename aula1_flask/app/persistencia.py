import psycopg2
from modelo import *

class Conexao:
	def abre(self):
		self.conexao = psycopg2.connect("dbname=keep user=postgres password=postgres host=localhost")
		self.cursor = self.conexao.cursor()

	def encerra(self):
		self.conexao.close()
		self.cursor.close()


class AnotacaoDAO:

	def adicionar(self, anotacao):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("INSERT INTO anotacao (titulo, descricao) VALUES(%s, %s);", [anotacao.titulo, anotacao.descricao])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
	# se False (padrao) = lista as anotacoes que nao estao na lixeira
	# se True = lista as anotacoes da lixeira
	def listar(self, lixeira = False):
		conexao = Conexao()
		conexao.abre()
		conexao.cursor.execute("SELECT * FROM anotacao WHERE lixeira = %s", [lixeira])
		vet = conexao.cursor.fetchall()
		# print "======================"
		# print vet
		# print "======================"
		vetAnotacao = []
		for a in vet:
			# titulo, descricao, lixeira, id
			vetAnotacao.append(Anotacao(a[1], a[2], a[3], a[0]))
		conexao.encerra()
		return vetAnotacao
	def excluir(self, id):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("DELETE FROM anotacao WHERE id = %s", [id])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
	def alterar(self, anotacao):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("UPDATE anotacao SET titulo = %s, descricao = %s WHERE id = %s;", [anotacao.titulo, anotacao.descricao, anotacao.id])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()	
		
	def obter(self, id):
		conexao = Conexao()
		conexao.abre()
		conexao.cursor.execute("SELECT * FROM anotacao WHERE id = %s", [id])
		a = conexao.cursor.fetchone()
		anotacao = Anotacao(a[1], a[2], a[3], a[0])
		conexao.encerra()
		return anotacao
	def replicar(self, id):
		anotacaoAux = self.obter(id)
		anotacaoAux.id = 0
		self.adicionar(anotacaoAux)
	def lixeira(self, id, lixeira = True):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("UPDATE anotacao SET lixeira = %s WHERE id = %s;", [lixeira, id])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()		