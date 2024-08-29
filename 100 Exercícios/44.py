#44) Escreva um algoritmo para ler 2 valores e se o segundo valor informado for ZERO, deve ser lido um novo valor, ou seja, para o segundo valor não pode ser aceito o valor zero e imprimir o resultado da divisão do primeiro valor lido pelo segundo valor lido. (utilizar a estrutura REPITA).

while True:
    print("---" * 15)
    print("Bem-Vindo a sua calculadora de divisão")
    valor1 = int(input("Digite um valor: "))
    valor2 = int(input("Digite outro valor: "))

    if valor2 == 0:
        print("Por favor informar um valor positivo!")
        valor2 = int(input("Digite outro valor: "))


    divisao = valor1 / valor2
    print(f"O resultado é {divisao}")