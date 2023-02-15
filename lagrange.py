pontos = int(input("Quantidade de pontos: "))
X, Y = [], []
for i in range(pontos):
    x = float(input("x" + str(i) + "= "))
    X.append(x)
    y = float(input("y" + str(i) + "= "))
    Y.append(y)

x = float(input("\nValor para a interpolação: "))
coeficientes = []
for indice in range(pontos):
    L = 1
    for j in range(len(X)):
        if indice != j:
            L *= (x-X[j])/(X[indice] - X[j])
    coeficientes.append(L)

pn = 0
for i in range(len(coeficientes)):
    pn += Y[i]*coeficientes[i]

print("\np(" +str(x) + ")=",pn)