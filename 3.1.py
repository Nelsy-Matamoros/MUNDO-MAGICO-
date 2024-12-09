import math
print("ingresa el radio del circulo:")
r = float(input())
pi = math.pi
a = math.pi *(r * r)
print("el area del circulo con radio ", r,"es:", round(a , 2))
print("valor de pi:", pi)



base = float(input("ingresa la base  del rectangulo: "))
altura = float(input("ingresa la altura del rectangulo: "))

area = base * altura
print("el area del rectangulo es:", round(area, 1))



lado = int(input("dame un lado:"))
cuadrado=[]
cuadrado.append(lado)
area = cuadrado[0]*cuadrado[0]
cuadrado.append(area)
print(cuadrado)








