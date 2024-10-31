# 90) Faça um algoritmo para ler um vetor de 30 números. Após isto, ler mais um número qualquer, calcular e escrever quantas vezes esse número aparece no vetor.

vetor = []

for x in range(30):
    numero = int(input(f"Digite o {x+1}° valor: "))
    vetor.append(numero)


mais_uma_vez = int(input("Digite mais um valor: "))

contador = 0

for numero in vetor:
    if numero == mais_uma_vez:
        contador = contador + 1

print(f"O número ({mais_uma_vez}) aparece ({contador}) vezes")