numero = 0

error = ValueError("El número debe ser positivo: "+str(numero))

def nivel(numero):
	if numero<0:
		raise error
	else:
		return numero

print(nivel(-1))