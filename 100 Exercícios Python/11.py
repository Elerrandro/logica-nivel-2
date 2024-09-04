#11) uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.

carro_vendido = int(input("carros vendidos: "))
valor_vendas = float(input("O valor total das vendas: R$"))
salario_fixo = float(input("Salario Fixo: R$"))
valor_por_carro = float(input("O valor recebido por carro vendido: R$"))

comissao_percentual = valor_vendas * 0.05
comissao_carro = valor_por_carro * carro_vendido

salario_final = salario_fixo + comissao_percentual + comissao_carro
print(f"O salario final é: R${salario_final}")
