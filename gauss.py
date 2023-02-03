import numpy as np

A = [[1,1,0],[2,-1,3],[-1,0,1]]
B = [2,4,0]

#Algoritmo de triangularização
n = len(B)
for k in range(0,n-1):
    for i in range(k+1,n):
        m = A[i][k]/A[k][k]
        A[i][k] = 0
        for j in range(k+1,n):
            A[i][j]= A[i][j] - A[k][j] * m
        B[i] = B[i] - B[k] * m

#Matriz A e vetor B após triangularização
print("\nMatriz A triangularizada:")
print(A)
print("\nVetor B triangularizado:")
print(B)

#Algoritmo de retrosubstituição
X = np.zeros(n)
X[n-1] = B[n-1]/A[n-1][n-1] #Solução da última linha
for k in range(n-2,-1,-1):
    soma = 0
    for j in range(k+1,n):
        soma = soma + A[k][j] * X[j]
    X[k] = (B[k] - soma)/A[k][k]

print("\nSolução:")
print(X)