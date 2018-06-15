"""
CREATE TABLE public.noticia
(
  id integer NOT NULL DEFAULT nextval('noticia_id_seq'::regclass),
  titulo text,
  texto text,
  CONSTRAINT noticia_pkey PRIMARY KEY (id)
)
"""

class Noticia:

	def __init__(self, titulo = "", texto = "", id = 0):
		self.titulo = titulo
		self.texto = texto
		self.id = id
	

	def obj2Str(self):
		# return str(self.id) + ";" + self.titulo + ";" + self.texto
		return self.titulo