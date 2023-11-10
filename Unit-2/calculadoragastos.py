#Ejercicio 2

import time

print("CALCULA TUS GASTOS")
print("-----------------------------")
time.sleep(3)

salario = float(input("Cuanto ganaste este mes?: $"))
time.sleep(2)
gastos = float(input("Cuanto has gastado este mes?: $"))
time.sleep(2)
print("-------------------------")
print("CALCULANDO RESTANTE")
total = salario - gastos
print("\n Tu restante es de: $",total)

