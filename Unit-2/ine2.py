#Ejercicio 5

#Librerias importadas
from datetime import datetime
import time 

print("MODULO INE")
print("----------------")
time.sleep(2)
print("Bienvenido al verificador del INE")
time.sleep(1)
name = str(input("Ingresa tu nombre: "))

age = int(input("Ingresa tu año de nacimiento: ")) #Tomamos el año de nacimiento del usuario
year_actual = datetime.now() #Sacamos la fecha actual

edad = year_actual.year - age #Calculamos su edad

#Funcion para ejecutar una barra de carga
bar_len = 24
elements = ['-', '\\', '|', "/"]

print("Validando datos")

for i in range(bar_len+1): #For que va cargando la barra
  frame = i % len(elements)
  print(f'\r[{elements[frame]*i:=<{bar_len}}]', end='')
  time.sleep(0.09)

#Condicion para saber si el usuario puede votar 
if edad >= 18:
  print(f"\n Felicidades {name}, puedes votar")
else:
  print(f"\n Lo sentimos {name}, debes ser mayor para votar")