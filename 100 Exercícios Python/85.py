# 85) Faça um algoritmo para ler e armazenar em um vetor a temperatura média de todos os dias do ano. Calcular e escrever: 

# a) Menor temperatura do ano
# b) Maior temperatura do ano
# c) Temperatura média anual
# d) O número de dias no ano em que a temperatura foi inferior a média anual

Temperaturas = []

for x in range(1, 366):
    Temp = float(input(f"Digite a temperatura do {x}° dia: "))
    Temperaturas.append(Temp)

media = sum(Temperaturas) / len(Temperaturas)

menor_temp = min(Temperaturas)
maior_temp = max(Temperaturas)
media_anual = media

dias_abaixo_media = 0
for x in Temperaturas:
    if x < media_anual:
        dias_abaixo_media = dias_abaixo_media + 1


print("Resultados:")
print(f"Menor temperatura do ano: {menor_temp:.2f}°C")
print(f"Maior temperatura do ano: {maior_temp:.2f}°C")
print(f"Temperatura média anual: {media:.2f}°C")
print(f"Número de dias com temperatura abaixo da média: {dias_abaixo_media}")