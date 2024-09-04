#9) escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário.

salario = float(input("Ensira seu salário atual: R$"))
reajuste = float(input("Ensira seu percentual de reajuste: "))

calculo_reajustado = salario * (1 + reajuste/100)

print(f"O valor do seu salário agora é: R${calculo_reajustado}")