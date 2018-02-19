#-* coding: utf8 -*#-

# 1
# F = 9/5 ∗ C + 32
def celsiusFare(celsius):
	return ((9.0/5.0)*celsius)+32.0
def fareCelsius(fare):
	return (fare-32.0)*(5.0/9.0)
# 2
def ehPrimo(n):
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	else:
		divisor = 2
		while (n % divisor != 0):
			divisor = divisor + 1
		if (n == divisor):
			return True
		else:
			return False

#n = raw_input("bota na colmeia ")
#resultado = fareCelsius(float(n))

# 2
# print ehPrimo(73)

# 3
'''
lista = [[0,1,2], [3,4], [5]]
listaResultado = []
for aux in lista:
	for elemento in aux:
		listaResultado.append(elemento)
print listaResultado
'''

dicionario = {'valores':[0,1,2,3,4,5]}
soma = 0.0
for elemento in dicionario['valores']:
	soma = soma + elemento
print "Media:", str(float(soma)/float(len(dicionario['valores'])))
print "Variacao:", str(float(max(dicionario['valores'])) - float(min(dicionario['valores'])))
















