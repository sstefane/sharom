# Ejercicio(2): Angie Alvarez, Jesús Polo, Sharom Steffane, Deivis Vergara, Gabriela Zambrano.
print("Operación con dos números y sus respectivos digitos")
x=int(input("ingrese un número de 3 digitos:\n"))
y=int(input("ingrese un número de 3 digitos:\n"))
m=x-y
print(f"la diferencia entre {x} y {y} es {m}")
# Digitos del primer número
a=int(round(x/100))
b=x-(a*100)
c=int(round(b/10))
d=b-(c*10)
# Digitos de segundo numero
e=int(round(y/100))
f=y-(e*100)
g=int(round(f/10))
h=f-(g*10)
# Suma de los digitos
k=a+c+d+e+g+h
# Digitos de la diferencia
p=int(round(m/100))
q=m-(p*100)
r=int(round(q/10))
s=q-(r*10)
if (m % 2 == 0):
  print(f"La suma de los digitos de los numeros es {k}")
else:
  print(f"La diferencia entre estos valores no es par")
#Se tomó una pequeña muestra de números posibles para el desarrollo del algoritmo, no se completó por el hecho de que sería algo infinito
if m<5 and m>0 and (m==4) and y<x:
  print(f"Los digitos en forma ascendente serian {y}, {y+1},{y+2},{y+3},{y+4}")
elif  m<5 and m>0 and (m==3) and y<x:
  print(f"Los digitos en forma ascendente serian {y}, {y+1},{y+2},{y+3}")
elif  m<5 and m>0 and (m==2) and y<x:
  print(f"Los digitos en forma ascendente serian {y}, {y+1},{y+2}")
elif  m<5 and m>0 and (m==1) and y<x:
  print(f"Los digitos en forma ascendente serian {y}, {y+1}")
else:
  print(f"La diferencia entre estos valores no es menor que 5")
if (p==1 or p==3 or p==5):
  print(f"Los digitos de los numeros son:")
  print(f"Del primer termino:")
  print(f"{a}")
  print(f"{c}")
  print(f"{d}")
  print(f"Del segundo termino:")
  print(f"{e}")
  print(f"{g}")
  print(f"{h}")
else:
  print("La diferencia entre estos numeros no inicia por el dígito 1, 3 o 5")