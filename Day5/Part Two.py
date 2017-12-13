def reclutador(rutaDeAcceso, lista):
	fichero = open(rutaDeAcceso, 'r')
	for elemento in fichero:
		numero = ""
		for valor in elemento:	
			if valor.isdigit() or valor == '-':
				numero += valor
		lista.append(int(numero))
	fichero.close()			
	return lista

def trampolin(lista):
	contador = 0
	indice = 0
	while True:
		
		try:
			if lista[indice] < 3:
				lista[indice], indice = (lista[indice] +1), (indice + lista[indice])
				contador += 1
			else:
				lista[indice], indice = (lista[indice] -1), (indice + lista[indice])
				contador += 1	

		except IndexError:
			return contador		
			
			

		
				

rutaDeAcceso = "casosTest.txt"
lista = []
reclutador(rutaDeAcceso, lista)
print(trampolin(lista))