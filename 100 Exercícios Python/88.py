# 88) Faça um algoritmo para ler um vetor de 20 números. Após isto, deverá ser lido mais um número qualquer e verificar se esse número existe no vetor ou não. Se existir, o algoritmo deve gerar um novo vetor sem esse número. (Considere que não haverão números repetidos no vetor).

vetor = []

for x in range(20):
    valor = int(input(f"Digite o {x+1}° valor: "))
    vetor.append(valor)

print(vetor)
print("---"*15)

procurando_numero = int(input("Digite o número que deseja eliminar: "))

nova_lista = []
for valor in vetor:
    if valor != procurando_numero:
        nova_lista.append(valor)

print(f"A nova lista é: {nova_lista}")