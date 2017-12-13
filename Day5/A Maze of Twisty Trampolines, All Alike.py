def reclutador(rutaDeAcceso, lista):
	fichero = open(rutaDeAcceso, 'r')
	for elemento in fichero:
		numero = ""
		for valor in elemento:	
			if valor.isdigit() or valor == '-':
				numero += valor
		lista.append(int(numero))
	print(lista)	
	return lista
def trampolin(lista):
	contador = 0
	indice = [numeros for numeros in range(len(lista))]
	indice = 0
	while True:
		try:

			if lista[indice] < 0:
				
				contador += 1
				lista[indice], indice = (lista[indice] +1), (indice + lista[indice])
				
			if lista[indice] == 0:
			
				contador += 1
				lista[indice] += 1
			if lista[indice] > 0:
				
				contador += 1
				lista[indice], indice = (lista[indice] +1), (indice + lista[indice])


		except IndexError:
			return contador		
			
			

		
				

rutaDeAcceso = "casosTest.txt"
lista = []
print(reclutador(rutaDeAcceso, lista))
print(trampolin(lista))		