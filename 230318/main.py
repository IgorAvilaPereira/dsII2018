import sys
import os
from persistencia import *
from modelo import *

# main
if __name__ == '__main__':
	aniversarianteDAO = AniversarianteDAO()
	# aniversariante = aniversarianteDAO.carregar(3)
	# aniversariante.nome = "marcio josue"
	# aniversarianteDAO.editar(aniversariante)
	# aniversarianteDAO.excluir(3)
	# print aniversariante
	# aniversarianteDAO.adicionar(Aniversariante("22222222222", "marcio yoda"))
	vet = aniversarianteDAO.listar()
	for a in vet:
		print a



