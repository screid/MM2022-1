# Problema 1: Ver si numero es par o no
"""
numero = 4

if numero % 2 == 0:
	print("si es par")
else:
	print("no es par")
"""

#Problema2: Problema de la pizza
#pregunta = input("¿Quiere pizza?: ")
"""
if pregunta == "SI":
	print("Tome su pizza")
elif pregunta == "NO":
	print("Usted es un demente")
else:
	print("No le entiendo")
"""

#Cosas que no se debe hacer:
"""
if pregunta == "SI":
	print("Tome su pizza")
if pregunta == "NO":
		print("Usted es un demente")
else:
	print("No le entiendo")
"""

#Problema 3: Suma del 0 al 10
#Ciclo while:

suma = 0

"""
i = 0
while i <= 10:
	suma = suma + i
	print(suma)
	i = i + 1
"""
"""
for i in range(0,10+1,1):
	if i % 2 == 0:
		suma = suma + i
		print(suma)
"""
for i in range(0,10+1,2):
	suma = suma + i
	print(suma)

print("Suma final: ", suma)
hello
