#64) Escreva um algoritmo para ler 10 números. Todos os números lidos com valor inferior a 40 devem ser somados. Escreva o valor final da soma efetuada.

numeros = []

for x in range(1, 11):
    numeros.append(int(input("Insira algum número: ")))

inferior = list(filter(lambda x: x < 40, numeros))
print(f"A soma dos valores inferior a 40 é {sum(inferior)}")
