import psycopg2
from modelo import *

class NoticiaDAO:

	def busca(self, valor):
		con = psycopg2.connect("host=localhost user=postgres password=postgres dbname=blog")
		cursor = con.cursor()
		cursor.execute("select * from noticia where titulo ilike %s", [valor + "%"])
		resultado = cursor.fetchone()
		if (resultado is None):
			return Noticia()
			cursor.close()
			con.close()
		else:
			cursor.close()
			con.close()
			return Noticia(resultado[1], resultado[2], int(resultado[0]))

	def busca2(self, valor):
		con = psycopg2.connect("host=localhost user=postgres password=postgres dbname=blog")
		cursor = con.cursor()
		cursor.execute("select * from noticia where titulo ilike %s", [valor + "%"])
		vet = cursor.fetchall()
		vetNoticia = []
		for resultado in vet:
			vetNoticia.append(Noticia(resultado[1], resultado[2], int(resultado[0])))		
		cursor.close()
		con.close()		
		return vetNoticia