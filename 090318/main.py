import sys
from persistencia import *
from modelo import *

# main
if __name__ == '__main__':
	#arquivo = open("banco.txt", "w")
	#arquivo.close()

	aniversarianteDAO = AniversarianteDAO()
	#aniversarianteDAO.adicionar(Aniversariante("666","Andreyna", 17, 3))
	#aniversarianteDAO.adicionar(Aniversariante("190","beck love", 19, 5))
	"""
	vet = aniversarianteDAO.listar()
	for n in vet:
		print n.nome
"""
	#print "Excluindo beck"
	#aniversarianteDAO.excluir("777")
	#vet = aniversarianteDAO.listar()
	#for n in vet:
	#	print n.nome
	aniversarianteDAO.listarMes(5)


