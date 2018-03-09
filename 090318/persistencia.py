from modelo import *

class AniversarianteDAO:

	def listar(self):
		arquivo = open("banco.txt", "r")
		vet = []
		for linha in arquivo:
			aux = linha.strip().split(";")
			aniversariante = Aniversariante(aux[0], aux[1], int(aux[2]), int(aux[3]))
			vet.append(aniversariante)
		arquivo.close()
		return vet
	def listarMes(self,mes):
		vet = self.listar()
		for n in vet:
			if n.mes == mes: 
				print n.nome
			
	def adicionar(self, aniversariante):
		arquivo = open("banco.txt", "a")
		arquivo.write(aniversariante.obj2CSV())
		arquivo.close()
	def excluir(self, cpf):
		vet = self.listar()
		vetAux = []
		for aniversariante in vet:
			if (aniversariante.cpf != cpf):
				vetAux.append(aniversariante)

		arquivo = open("banco.txt", "w")
		arquivo.close()		
		for e in vetAux:
			self.adicionar(e)