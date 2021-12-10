#funcion de calculadora
def calculadora(nro1, nro2, operador):
	if operador == "+":
		print(nro1+nro2)
	elif operador == "-":
		print(nro1-nro2)
	elif operador == "*":
		print(nro1*nro2)
	elif operador == "/":
		print(nro1/nro2)
	else:
		print("El operador no es valido")
