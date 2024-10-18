#83) Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.

vetor = []

for x in range(20):
    numeros = int(input(f"Digite o {x+1}° valor: "))
    vetor.append(numeros)

print("---"*15)
print("Como ficou a lista na ordem normal")
print(vetor)
print("---"*15)

vetor.reverse()
print("Como ficou a lista na ordem inversa")
print(vetor)