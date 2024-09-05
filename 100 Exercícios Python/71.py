#71) Faça um algoritmo para ler uma quantidade e a seguir ler esta quantidade de números. Depois de ler todos os números o algoritmo deve apresentar na tela o maior dos números lidos e a média dos números lidos.

numero = []
for x in range(5):
  valor = float(input(f"Insira o {x+1}° valor: "))
  numero.append(valor)

valor_max = max(numero)
valor_total = sum(numero)

media = valor_total / len(numero)

print(f"O maior número lido é: {valor_max}")
print(f"A média dos números lidos é: {media}")
