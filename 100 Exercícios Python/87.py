# 87) O mesmo exercício anterior, mas depois de ordenar os elementos do vetor em ordem crescente, deve ser lido mais um número qualquer e inserir esse novo número na posição correta, ou seja, mantendo a ordem crescente do vetor.

vetor = []

for x in range(1, 11):
    temp = int(input(f"Digite o {x}° valor: "))
    vetor.append(temp)

ordenado = sorted(vetor)
print(ordenado)
print("---"*15)

temp = int(input("Digite mais um valor: "))
vetor.append(temp)
ordenado = sorted(vetor)
print(ordenado)