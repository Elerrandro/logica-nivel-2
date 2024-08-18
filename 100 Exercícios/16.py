#16) as maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

custo_maca = 1.30
duzia_maca = 1.00

n1 = int(input("Insira quantas maçãs comprou: "))

if n1 >= 12:
    soma = n1 * duzia_maca
    print(f"O valor é: R${soma}")
else:
   soma = n1 * custo_maca
   print(f"O valor é: R${soma}")
