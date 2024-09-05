#70) Faça um programa que leia 100 valores e no final, escreva o maior e o menor valor lido.

numeros = []
for x in range(1, 101):
  numeros.append(x)
  
valor_min = min(numeros)
print(f"O valor minimo do 1 ate 100 é: {valor_min}")
valor_max = max(numeros)
print(f"O valor maximo de 1 ate 100 é: {valor_max}")
