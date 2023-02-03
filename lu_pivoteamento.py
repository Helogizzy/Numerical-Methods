import numpy as np

A = [[1,1,1],[2,1,-1],[2,-1,1]]
b = [-2,1,3]

#acessa as linhas da matriz
for k in range(len(A)):
    #define o pivô
    pivo = abs(A[k][k])
    linhaPivo = k
  
    #verifica se há algum número maior nas linhas abaixo da coluna do pivô
    for i in range(k+1, len(A)):
        if abs(A[i][k]) > pivo:
            pivo = abs(A[i][k])
            linhaPivo = i

    #pivoteamento
    if linhaPivo != k:
        linha_aux = A[k]
        A[k] = A[linhaPivo]
        A[linhaPivo] = linha_aux
            
        b_aux = b[k]
        b[k] = b[linhaPivo]
        b[linhaPivo] = b_aux

    #eliminação de gauss
    for i in range(k+1, len(A)):
        multiplica = A[i][k] / A[k][k]
        #atribui o multiplicador nos elementos abaixo da diagonal principal
        A[i][k] = multiplica
        for j in range(k+1, len(A)):
            A[i][j] -= multiplica*A[k][j]

print("\nMatriz depois da eliminação gaussiana e o pivoteamento:")
for i in range(len(A)):
    print(A[i])
 
L, U = [], []
for i in range(len(A)):
    linha_L = []
    linha_U = []
    for j in range(len(A)):
        #elementos da diagonal principal
        if i == j:
            linha_L.append(1)
            linha_U.append(A[i][j])
        #se a linha for maior que a coluna, elementos abaixo da diagonal principal
        elif i > j:
            linha_L.append(A[i][j])
            linha_U.append(0)
        #elementos acima da diagonal principal
        else:
            linha_L.append(0)
            linha_U.append(A[i][j])
          
    L.append(linha_L)
    U.append(linha_U)

print("\nMatriz L")
for i in range(len(L)):
    print(L[i])

print("\nMatriz U")
for i in range(len(U)):
    print(U[i])

print("\nLy = b")
y = np.linalg.solve(L, b)
print("Y = ", y)

print("\nUx = y")
x = np.linalg.solve(U, y)
print("X = ", x)
