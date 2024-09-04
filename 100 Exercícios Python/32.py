#32) ler o nome de 2 times e o número de gols marcados na partida (para cada time). Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.

time1 = input("Insira o nome de um time: ")
time2 = input("Insira o nome de outro time: ")
gols1 = int(input(f"Insira o numero de gols do {time1} na partida: "))
gols2 = int(input(f"Insira o numero de gols do {time2} na partida: "))

if gols1 > gols2:
    print(f"O {time1} GANHOU!")
elif gols1 < gols2:
    print(f"O {time2} GANHOU!")
else:
    print(f"O {time1} e o {time2} EMPATOU!")
