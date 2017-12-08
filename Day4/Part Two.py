from itertools import permutations
def validator(rutaDeAcceso, password):
	fichero = open(rutaDeAcceso, 'r')
	lineas = 0
	invalido = 0
	for linea in fichero:
		lineas += 1
		colector = []
		conjunto = ""
		erroneo = 0
		for letra in linea:
			if letra.isalpha():
				conjunto += letra
			else:
				for posible in permutations(conjunto):
					posible = "".join(posible)
					if posible in colector:

						conjunto = posible

				if conjunto not in colector:
					colector.append(conjunto)
				else:
					if erroneo == 0:
						invalido +=1
						erroneo += 1	
				conjunto = ""
		if len(conjunto) > 0:
			if conjunto not in colector:
				colector.append(conjunto)
			else:
				if erroneo == 0:
						invalido +=1
						erroneo += 1		
	valido = lineas - invalido
	return valido



rutaDeAcceso = "casosTest.txt"
password = []
print(validator(rutaDeAcceso, password))
