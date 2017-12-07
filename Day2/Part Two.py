from itertools import permutations

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
		for posible in permutations(row, 2):
			recolector = []
			for numeros in posible:
				recolector.append(int(numeros))
			if recolector[0] % recolector[1] == 0:
				print(recolector)
				contador.append(int(posible[0])/int(posible[1]))
	return sum(contador)


rutaDeAcceso = "casosTest.txt"
lista = []
preparador(rutaDeAcceso, lista)
print(checksum(lista))
