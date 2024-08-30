#63) Escreva um algoritmo para ler 10 números e ao final da leitura escrever a soma total dos 10 números lidos.

numeros = []

for x in range(1, 11):
    numeros.append(int(input("Digite algum número: ")))

print(f"A soma dos números inseridos é: {sum(numeros)}")
