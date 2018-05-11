import psycopg2
from modelo import *

class JogadorDAO:

	def excluir(self, id):
		conn = psycopg2.connect("dbname=lol host=localhost user=postgres password=postgres")
		cur = conn.cursor()
		cur.execute("DELETE FROM jogador WHERE id = %s;", [id])
		conn.commit()
		cur.close()
		conn.close()

	def obter(self, id):
		conn = psycopg2.connect("dbname=lol host=localhost user=postgres password=postgres")
		cur = conn.cursor()
		cur.execute("SELECT * FROM jogador WHERE id = %s;", [id])
		registro = cur.fetchone()		
		jogador = Jogador()
		jogador.id = int(registro[0])
		jogador.nome = registro[1]
		jogador.foto = registro[2]
		cur.close()
		conn.close()
		return jogador

	def listar(self):
		conn = psycopg2.connect("dbname=lol host=localhost user=postgres password=postgres")
		cur = conn.cursor()
		cur.execute("SELECT * FROM jogador;")
		vet = cur.fetchall()
		vetJogador = []
		for registro in vet:
			jogador = Jogador()
			jogador.id = int(registro[0])
			jogador.nome = registro[1]
			jogador.foto = registro[2]
			vetJogador.append(jogador)
		cur.close()
		conn.close()
		return vetJogador

	def alterar(self, jogador):
		conn = psycopg2.connect("dbname=lol host=localhost user=postgres password=postgres")
		cur = conn.cursor()
		cur.execute("UPDATE jogador SET nome = %s, foto = %s WHERE id = %s;", [str(jogador.nome), str(jogador.foto), jogador.id])
		conn.commit()
		cur.close()
		conn.close()

	def adicionarNome(self, jogador):
		conn = psycopg2.connect("dbname=lol host=localhost user=postgres password=postgres")
		cur = conn.cursor()
		cur.execute("INSERT INTO jogador (nome) VALUES (%s) RETURNING id;", [str(jogador.nome)])
		conn.commit()
		id = cur.fetchone()[0]
		cur.close()
		conn.close()
		return int(id)
