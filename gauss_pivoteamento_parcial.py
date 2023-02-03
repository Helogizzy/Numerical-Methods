import math

A = [[1,1,0],[2,-1,3],[-1,0,1]]
b = [2, 4, 0]

#acessa as linhas da matriz
for i in range(len(A)):
    #verifica o maior pivô
    pivo = math.fabs(A[i][i])
    linhaPivo = i
    #verifica se há algum número maior nas linhas abaixo da coluna do pivô
    for j in range(i+1, len(A)):
        if math.fabs(A[j][i])>pivo:
            pivo = math.fabs(A[j][i])
            linhaPivo = j

    #pivoteamento
    if linhaPivo != i:
        linha_aux = A[i]
        A[i] = A[linhaPivo]
        A[linhaPivo] = linha_aux
            
        b_aux = b[i]
        b[i] = b[linhaPivo]
        b[linhaPivo] = b_aux

    #eliminação de gauss
    for m in range(i+1, len(A)):
        #razao entre os numeros que estão abaixo do pivô pelo pivô
        multiplica = A[m][i]/A[i][i]
        for n in range(i, len(A)):
            A[m][n] -= multiplica*A[i][n]
        b[m] -= multiplica*b[i]

#print matriz A e o vetor B escalonados
print("\nMatriz A escalonada:")
for k in range(len(A)):
    print(A[k])
print("\nVetor B escalonado:")
print(b)

#calculo da solucao
vet_solucao = []
for i in range(len(A)):
    vet_solucao.append(0)

linha = len(A) - 1
while linha >= 0:
    x = b[linha]
    coluna = len(A) - 1

    while coluna > linha:
        x -= A[linha][coluna]*vet_solucao[coluna]
        coluna -= 1
        
    x/= A[linha][linha]
    linha -= 1
    vet_solucao[coluna] = x
    
print("\nSolução:")
for j in range(len(vet_solucao)):
    print("X"+str(j)+"="+str(vet_solucao[j]))