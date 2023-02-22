import math

#escrever o valor da função como: math.exp(-x**2)
f = input("F(x)=")
x0 = float(input("Limite inferior: "))
xM = float(input("Limite superior: "))
h = float(input("Passo (h):"))

integral = 0
x = x0
integral += eval(f)
x += h
indice = 1

while x < xM:
    if indice%2 != 0:
        integral += 4*eval(f)
    else:
        integral += 2*eval(f)
    indice += 1
    x += h
x = xM
integral += eval(f)
integral *= (h/3)
print("\nIntegral =", integral)