#40) Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário. Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que: 

#- Se quantidade <= 5 o desconto será de 2%
#- Se quantidade > 5 e quantidade <=10 o desconto será de 3%
#- Se quantidade > 10 o desconto será de 5%

descricao_produto = str(input("Qual nome do produto: "))
quantidade_adquirida = int(input("Qual a quantidade obtida: "))
preco_unitario = float(input("Qual o preço unitário: "))

total = quantidade_adquirida * preco_unitario


if quantidade_adquirida <= 5:
    desconto = total * 0.02
elif quantidade_adquirida > 5 and quantidade_adquirida <= 10:
    desconto = total * 0.03
elif quantidade_adquirida > 10:
    desconto = total * 0.05
    
total_pagar = total - desconto
    
print(f"Nome do produto: {descricao_produto}")
print(f"Quantidade adquirida: {quantidade_adquirida}")
print(f"Preço unitário: R${preco_unitario:.2f}")
print(f"Desconto recebido: R${desconto:.2f}")
print(f"Preço a ser pago: R${total_pagar:.2f}")
