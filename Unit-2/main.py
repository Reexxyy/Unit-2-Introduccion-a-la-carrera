#Ejercicio 1

from datetime import datetime #Libreria para las fechas



while True: #Ciclo para evitar que ingrese valores invalidos
  fecha_nacimiento = input("Ingresa tu fecha de nacimiento (YYYY/MM/DD): ")

  try: #Try para ver si el usuario ingreso datos en el formato correcto
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y/%m/%d") #Establecemos el formato (YYYY/MM/DD)
    break #Salir del bucle
  except ValueError: #En caso de no poner el formato correcto mandamos un error
    print("Ingresa valores validos Formato: (YYYY/MM/DD)")

fecha_actual = datetime.now() #Sacamos la fecha actual

edad = fecha_actual.year - fecha_nacimiento.year #Hacemos la resta de los años

#Resta para que el mes y el dia 
if fecha_actual.month < fecha_nacimiento.month or (fecha_actual.month == fecha_nacimiento.month and fecha_actual.day < fecha_nacimiento.day):
  edad -= 1 

#Imprimimos el resultado de la edad
print("La edad del usuario es de ", edad, "años")



