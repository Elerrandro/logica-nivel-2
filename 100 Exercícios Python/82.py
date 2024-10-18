#82) Ler um vetor A de 10 números. Após, ler mais um número e guardar em uma variável X. Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. Logo após, imprimir o vetor M.

A = []
M = []

for x in range(10):
    ler = int(input(f"Digite o {x+1}° valor: "))
    A.append(ler)

X = int(input("Digite mais um valor: "))

for x in range(10):
    M.append(A[x] * X)

print(M)