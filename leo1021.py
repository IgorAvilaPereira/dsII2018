
dinheiros = float(input())

if dinheiros >= 0 and dinheiros <= 1000000.00:
	parteInteira = int(dinheiros)

	cemzao = (parteInteira/100)
	total = cemzao*100

	cinquentao = (parteInteira%100)/50
	total =  total + cinquentao*50

	vintao = ((parteInteira%100)%50)/20
	total = total + vintao*20

	dez = (((parteInteira%100)%50)%20)/10
	total = total + dez*10

	cinco = ((((parteInteira%100)%50)%20)%10)/5
	total = total + cinco*5 


	dois = (((((parteInteira%100)%50)%20)%10)%5)/2
	total = total + dois * 2

	print("NOTAS:")
	print(str(cemzao)+" nota(s) de R$ 100.00")
	print(str(cinquentao)+" nota(s) de R$ 50.00")
	print(str(vintao)+" nota(s) de R$ 20.00")
	print(str(dez)+" nota(s) de R$ 10.00")
	print(str(cinco)+" nota(s) de R$ 5.00")
	print(str(dois)+" nota(s) de R$ 2.00")

	um = (((((parteInteira%100)%50)%20)%10)%5)%2
	total = total + um * 1

	parteDecimal = int((dinheiros - parteInteira) * 100)

	cinquentamoeda = (parteDecimal/50)
	total = total + cinquentamoeda*0.5


	vintecinco = (parteDecimal%50)/25
	total = total + vintecinco*0.25

	dezmoeda = ((parteDecimal%50)%25)/10
	total = total + dezmoeda*0.10


	cincomoeda = (((parteDecimal%50)%25)%10)/5
	total = total + cincomoeda*0.05

	#umcentavo = ((((parteDecimal%50)%25)%10)%5)

	umcentavo = (dinheiros - total)*100


	print("MOEDAS:")
	print(str(um)+" moeda(s) de R$ 1.00")
	print(str(cinquentamoeda)+" moeda(s) de R$ 0.50")
	print(str(vintecinco)+" moeda(s) de R$ 0.25")
	print(str(dezmoeda)+" moeda(s) de R$ 0.10")
	print(str(cincomoeda)+" moeda(s) de R$ 0.05")
	print(str(int(round(umcentavo, 1)))+" moeda(s) de R$ 0.01")

