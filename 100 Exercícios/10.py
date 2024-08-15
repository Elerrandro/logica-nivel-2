#10) O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.

print("Custo de um carro novo!")
distribuidor = 0.28
imposto = 0.45
custo_fabrica = float(input("Ensira o valor de fábrica: R$"))

soma = (custo_fabrica * distribuidor) + (custo_fabrica * imposto)

print(f"O valor do carro novo é: R${soma}")