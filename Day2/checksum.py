def preparador(casostest, lista):
	fichero = open(casostest, 'r')
	fila = []
	for linea in fichero:
		numeros = []
		for j in linea:
			try:
				j = int(j)
				numeros.append(str(j))
			except ValueError:
				if not j.isdigit():
					numeros = "".join(numeros)
					fila.append(numeros)
					numeros = []
		if len(numeros) > 0:
			numeros = "".join(numeros)
			fila.append(numeros)
		lista.append(fila)
		fila = []		
	return lista	


def checksum(matrix):
	contador = []
	for row in matrix:
		recolector=[]
		for i in row:
			i = int(i)
			recolector.append(i)	
		contador.append(max(recolector) - min(recolector))							
	return sum(contador)


rutaDeAcceso = "casosTest.txt"
lista = []
preparador(rutaDeAcceso, lista)
print(checksum(lista))


