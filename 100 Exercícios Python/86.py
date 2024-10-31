# 86) Faça um algoritmo para ler 10 números e armazenar em um vetor. Após isto, o algoritmo deve ordenar os números no vetor em ordem crescente. Escrever o vetor ordenado.

vetor = []

for x in range(1, 11):
    temp = int(input(f"Digite o {x}° valor: "))
    vetor.append(temp)

ordenado = sorted(vetor)
print(ordenado)