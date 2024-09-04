#47) Acrescentar uma mensagem de 'VALOR INVÁLIDO' no exercício [45] caso o segundo valor informado seja ZERO.

print("---" * 15)
print("Bem-Vindo a sua calculadora de divisão")
valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite outro valor: "))

while valor2 == 0: 
    print("VALOR INVÁLIDO")   
    print("Por favor informar um valor positivo!")
    valor2 = float(input("Digite outro valor: "))
    
divisao = valor1 / valor2
print(f"O resultado é {divisao}")