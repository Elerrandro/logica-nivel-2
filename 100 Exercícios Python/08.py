#8) escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.


eleitores = int(input("Ensira o número total de eleitores: "))
votos_brancos = int(input("Ensira o número de votos brancos: "))
votos_nulos = int(input("Ensira o número de votos nulos: "))
votos_validos = int(input("Ensira o número de votos validos: "))

percentual_branco = (votos_brancos/eleitores) * 100
percentual_nulo = (votos_nulos/eleitores) * 100
percentual_valido = (votos_validos/eleitores) * 100

print(f"O percentual dos votos brancos é {percentual_branco}%")
print(f"O percentual dos votos nulo é {percentual_nulo}%")
print(f"O percentual dos votos valido é {percentual_valido}%")