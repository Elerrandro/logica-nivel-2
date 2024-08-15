#7) faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.

ano = (365)
mes = (30)
ANOS = int(input("Ensira sua idade em anos: "))
MESES = int(input("Adicione os meses adicionais: "))
DIAS = int(input("Adicione os dias adicionais: "))

calculo = (ANOS*ano) + (MESES*mes) + DIAS

print(f"Sua idade expressa em dias é: {calculo}")