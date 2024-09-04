#59) Ler 10 valores e escrever quantos desses valores lidos são NEGATIVOS.

valores = []

for x in range(1, 11):
    valores.append(int(input("Insira um valor inteiro: ")))

#FILTRA SOMENTE OS NÚMEROS NEGATIVOS
negativos = list(filter(lambda x: x < 0, valores))
#Len irá ler quantos números tem na variavel
print(f"Dos 10 valores {len(negativos)} São negativos !")
