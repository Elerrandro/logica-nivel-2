#60) Ler 10 valores e escrever quantos desses valores lidos estão no intervalo [10,20] (inlcuindo os valores 10 e 20 no intervalo) e quantos deles estão fora deste intervalo.

valores = []

for x in range(1, 11):
    valores.append(int(input("Insira um valor inteiro: ")))
    
dentro_intervalo = list(filter(lambda x: x >= 10 and x <= 20, valores))
fora_intervalo = list(filter(lambda x: x < 10 or x > 20, valores))

print("A QUANTIDADE DE NÚMEROS ENTRE 10 E 20 INCLUINDO OS MESMO")
print(f"A quantidade é {(len(dentro_intervalo))}")
print("A QUANTIDADE DE NÚMEROS FORA DO INTERVALO DE 10 E 20")
print(f"A quantidade é {(len(dentro_intervalo))}")
