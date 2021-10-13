#Sharom Brigett Steffane Hernandez
#Ejercicio 1
print("Algoritmo que determina de n números cuál es el mayor, el menor y el promedio")
n = int(input("Indique la cantidad de números que desea analizar:"))
s = 0
for i in range(n):
    x = float(input("ingrese el valor # ",i))
    s = s + x
p = s / n
print("el promedio de los datos ingresados es; ", p)
