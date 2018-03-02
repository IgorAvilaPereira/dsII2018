from math import *
entrada = raw_input()
vet = entrada.split(" ")
a = int(vet[0])
b = int(vet[1])
c = int(vet[2])
maiorAB = (a+b+fabs(a-b))/2
maiorABC = int((maiorAB+c+fabs(maiorAB-c))/2)
print(str(maiorABC)+" eh o maior")
