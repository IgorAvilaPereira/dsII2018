from modelo import *
import os
import psycopg2

class AniversarianteDAO:



	def listar(self):
		vetObj = []
		try:
			conn = psycopg2.connect("dbname=veiga host=localhost user=postgres password=postgres")
			cur = conn.cursor()
			cur.execute("SELECT * FROM aniversariante")
			print cur.rowcount
			vet = cur.fetchall()			
			for linha in vet:
				vetObj.append(Aniversariante(linha[2], linha[1], int(linha[0])))
		except Exception as e:
			print "nao deis...deu xabum na conexao #colmeia"
		cur.close()
		conn.close()
		return vetObj

	def carregar(self, id):
		# vetObj = []
		aniversariante = Aniversariante()
		try:
			conn = psycopg2.connect("dbname=veiga host=localhost user=postgres password=postgres")
			cur = conn.cursor()
			cur.execute("SELECT * FROM aniversariante WHERE id = %s", [id])
			linha = cur.fetchone()
			aniversariante = Aniversariante(linha[2], linha[1], int(linha[0]))
		except Exception as e:
			print "nao deis...deu xabum na conexao #colmeia"
		cur.close()
		conn.close()
		return aniversariante


	def adicionar(self, aniversariante):
		try:
			conn = psycopg2.connect("dbname=veiga host=localhost user=postgres password=postgres")
			cur = conn.cursor()
			data = [aniversariante.nome, aniversariante.cpf]
			cur.execute("INSERT INTO aniversariante (nome, cpf) VALUES (%s, %s);", data)
			# vet = cur.fetchall()			
			# for linha in vet:
				# vetObj.append(Aniversariante(linha[2], linha[1], int(linha[0])))
			conn.commit()	
		except Exception as e:
			print "nao deis...deu xabum na conexao #colmeia"
		cur.close()
		conn.close()



			

	# def listar(self):
	# 	arquivo = open("banco.txt", "r")
	# 	vet = []
	# 	for linha in arquivo:
	# 		aux = linha.strip().split(";")
	# 		aniversariante = Aniversariante(aux[0], aux[1], int(aux[2]), int(aux[3]))
	# 		vet.append(aniversariante)
	# 	arquivo.close()
	# 	return vet

	# def listarMes(self,mes):
	# 	vet = self.listar()
	# 	for n in vet:
	# 		if n.mes == mes: 
	# 			print n.nome

	# def adicionar(self, aniversariante):
	# 	arquivo = open("banco.txt", "a")
	# 	arquivo.write(aniversariante.obj2CSV())
	# 	arquivo.close()

	def excluir(self, id):
		try:
			conn = psycopg2.connect("dbname=veiga host=localhost user=postgres password=postgres")
			cur = conn.cursor()
			cur.execute("DELETE FROM aniversariante WHERE id = %s", [id])
			conn.commit()	
		except Exception as e:
			print "nao deis...deu xabum na conexao #colmeia"
		cur.close()
		conn.close()
	

	def editar(self, aniversariante):
		try:
			conn = psycopg2.connect("dbname=veiga host=localhost user=postgres password=postgres")
			cur = conn.cursor()
			cur.execute("UPDATE aniversariante SET nome = %s, cpf = %s WHERE id = %s", [aniversariante.nome, aniversariante.cpf, aniversariante.id])
			conn.commit()	
		except Exception as e:
			print "nao deis...deu xabum na conexao #colmeia"
		cur.close()
		conn.close()

	def listarOrdemAlfabetica(self):
		vetObj = []
		try:
			conn = psycopg2.connect("dbname=veiga host=localhost user=postgres password=postgres")
			cur = conn.cursor()
			cur.execute("SELECT * FROM aniversariante ORDER BY nome;")
			vet = cur.fetchall()			
			for linha in vet:
				vetObj.append(Aniversariante(linha[2], linha[1], int(linha[0])))
		except Exception as e:
			print "nao deis...deu xabum na conexao #colmeia"
		cur.close()
		conn.close()
		return vetObj	
		
	# 	arquivo = open("ordem.txt", "a+")		
	# 	for nome in vetNome:
	# 		arquivo.write(nome+"\n")
	# 	arquivo.close()

	# def redirecionar(self):
	# 	meses = ["","janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
	# 	qtdePorMes = [0,0,0,0,0,0,0,0,0,0,0,0]
	# 	vet = self.listar()

	# 	for m in meses:
	# 		arquivo = open(m+".txt","w")
	# 		arquivo.close()
		
	# 	for n in vet:
	# 		qtdePorMes[n.mes] = qtdePorMes[n.mes] + 1
	# 		arquivo = open(meses[n.mes]+".txt","a")
	# 		arquivo.write(n.obj2CSV())
	# 		arquivo.close()

	# 	i = 0
	# 	while i < len(qtdePorMes):
	# 		if (qtdePorMes[i] == 0):
	# 			os.remove(meses[i]+".txt")
	# 		i = i + 1