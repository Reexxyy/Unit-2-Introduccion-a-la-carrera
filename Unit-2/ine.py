#Ejercicio 4

#Librerias importadas
import time

print("MODULO DE INE")
print("-------------------------")
time.sleep(2)

name = str(input("Ingresa tu nombre: "))
print(f"Hola {name} verifica si puedes votar")
time.sleep(1)

edad = int(input(f"{name} ingresa tu edad: ")) #El usuario ingresa su edad
time.sleep(1)

print("Validando tus datos")
print("--------------------")
time.sleep(2)
#Condicion que decide si puede o no votar
if edad >= 18:
  print(f"Felicidades {name}, puedes pasar a votar")
else:
  print(f"Lo sentimos {name}, debes ser mayor de edad para poder votar")
