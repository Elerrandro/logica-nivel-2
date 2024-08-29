#45) Reescreva o exercício anterior utilizando a estrutura ENQUANTO.

print("---" * 15)
print("Bem-Vindo a sua calculadora de divisão")
valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite outro valor: "))

while valor2 == 0:    
    print("Por favor informar um valor positivo!")
    valor2 = float(input("Digite outro valor: "))
    
divisao = valor1 / valor2
print(f"O resultado é {divisao}")