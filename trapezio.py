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

while x < xM:
    integral += 2*eval(f)
    x += h
x = xM
integral += eval(f)
integral *= (h/2)
print("\nIntegral =", integral)