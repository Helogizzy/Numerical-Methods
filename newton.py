quant_pontos = int(input("Quantidade de pontos: "))
pontos, f_pontos = [], []
tabela = []
for i in range(quant_pontos):
    ponto = float(input("x%d = "%i))
    f_ponto = float(input("F(x%d) = "%i))
    pontos.append(ponto)
    f_pontos.append(f_ponto)
tabela.append(f_pontos)

x = float(input("\nPonto x a ser estimado: "))
print()

passo = 1
for n in range(quant_pontos-1):
    ordem = []
    for m in range(len(tabela[n])-1):
        dif_divida = (tabela[n][m+1] - tabela[n][m])/(pontos[m+passo] - pontos[m])
        ordem.append(dif_divida)
    tabela.append(ordem)
    passo += 1

for k in range(len(tabela)):
    print("Ordem %d "%k, tabela[k])
print();

aprox=0
grau=0
for i in range(len(tabela)):
    fator = tabela[i][0]
    for j in range(grau):
        fator *= (x - pontos[j])
    grau += 1
    aprox += fator
print("Aproximação encontrada para F(%f) = %f" %(x, aprox))