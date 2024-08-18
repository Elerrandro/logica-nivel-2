#24) ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.

salario_fixo = float(input("Insira o sálario fixo: "))
Valor_das_vendas = float(input("Insira o valor das vendas efetuada pelo vendedor da empresa: "))

if Valor_das_vendas <= 1500:
    Comissao = Valor_das_vendas * 0.03
else:
    Comissao = Valor_das_vendas * 0.03 + (Valor_das_vendas - 1500) * 0.05
    
salario_total = salario_fixo + Comissao

print(f"O salario total é R${salario_total}")
