# 89) Faça um algoritmo para ler dois vetores V1 e V2 de 15 números cada. Calcular e escrever a quantidade de vezes que V1 e V2 possuem os mesmos números e nas mesmas posições.

V1 = []
V2 = []

for x in range(15):
    numero1 = int(input(f"Digite o {x+1}° valor da lista 1: "))
    numero2 = int(input(f"Digite o {x+1}° valor da lista 2: "))
    V1.append(numero1)
    V2.append(numero2)

contador = 0
for x in range(15):
    if V1[x] == V2[x]:
        contador = contador + 1

print(f"A quantidade de vezes que os mesmos números nas mesma posições se repetem são {contador}")