# CREATE TABLE anotacao (
# 	id serial primary key,
# 	titulo text,
# 	descricao text,
# 	lixeira boolean
# );

class Anotacao:
	def __init__(self, titulo = "", descricao = "", lixeira = False, id = 0):
		self.titulo = titulo
		self.descricao = descricao
		self.lixeira = lixeira
		self.id = id
	def __repr__(self):
		return str(self.id) + ";" + self.titulo + ";" + self.descricao		