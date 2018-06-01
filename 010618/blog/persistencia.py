import psycopg2 
from modelo import *

class NoticiaDAO:

	def adicionar(self, noticia):
		sql = "INSERT INTO noticia (titulo, texto) VALUES (%s, %s);"
		con = psycopg2.connect("host=localhost dbname=blog user=postgres password=postgres")
		cursor = con.cursor()
		cursor.execute(sql, [noticia.titulo, noticia.texto])					
		con.commit()
		cursor.close()
		con.close()	

	def listar(self):
		sql = "SELECT * FROM noticia"
		con = psycopg2.connect("host=localhost dbname=blog user=postgres password=postgres")
		cursor = con.cursor()
		cursor.execute(sql)
		vet = cursor.fetchall()
		vetNoticia = []
		for registro in vet:
			vetNoticia.append(Noticia(registro[1], registro[2], int(registro[0])))
		cursor.close()
		con.close()
		return vetNoticia	