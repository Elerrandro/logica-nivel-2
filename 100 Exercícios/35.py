#35) Um posto está vendendo combustíveis com a seguinte tabela de descontos: 

#Álcool até 20 litros, desconto de 3% por litro | Acima de 20 litros, desconto de 5% por litro.
#Gasolina até 20 litros, desconto de 4% por litro | Acima de 20 litros, desconto de 6% por litro.

#Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90. 
 
preco_alcool = 2.90
preco_gasolina = 3.30


litros = float(input("Digite o números de litros vendidos: "))
tipos_combustivel = input("Digite o tipo de combustível(A para álcool, G para gasolina: ")


a_alcool = litros * preco_alcool
g_gasolina = litros * preco_gasolina

if tipos_combustivel == 'A':
    if litros > 0:
        if a_alcool <= 20:
            valor_desconto = a_alcool * 0.03
            valor_final = a_alcool - valor_desconto
            print(f"O cliente tem que pagar R${valor_final:.2f} no alcool")
        elif a_alcool > 20:
            valor_desconto = a_alcool * 0.05
            valor_final = a_alcool - valor_desconto
            print(f"O cliente tem que pagar R${valor_final:.2f} no alcool")
        else:
            print("Vá trabalhar seu vagabundo!")
if tipos_combustivel == 'G':    
    if litros > 0:
        if g_gasolina <= 20:
            valor_desconto = g_gasolina * 0.04
            valor_final = g_gasolina - valor_desconto
            print(f"O cliente tem que pagar R${valor_final:.2f} na gasolina")
        elif g_gasolina > 20:
            valor_desconto = g_gasolina * 0.06
            valor_final = g_gasolina - valor_desconto
            print(f"O cliente tem que pagar R${valor_final:.2f} na gasolina")
        else:
            print("Vá trabalhar seu vagabundo!")
