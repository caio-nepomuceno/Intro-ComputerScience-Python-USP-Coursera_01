import math

a = float(input("qual o valor de a? "))
b = float(input("qual o valor de b? "))
c = float(input("qual o valor de c? "))

delta = (b**2) - (4*a*c)
raiz1 = (-b+math.sqrt(delta))/(2*a)
raiz2 = (-b-math.sqrt(delta))/(2*a)

if delta == 0:
    print("a única raiz é", raiz1)
    
if delta < 0:
    print("esta equação não tem raízes")
    
if delta > 0:
    print("a primeira raiz é", raiz1, "e a segunda raiz é", raiz2)