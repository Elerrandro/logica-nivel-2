#81) O mesmo exercício anterior, mas agora deve escrever o menor elemento do vetor e a respectiva posição dele nesse vetor.

Q = []

while len(Q) < 20:
    ler = int(input(f"Digite algum valor: "))
    if ler > 0:
        Q.append(ler)
    else:
        print("===AVISO===")
        print("Por favor digitar somente números positivos!!!")


maior_valor = min(Q)
posicao = 1 + Q.index(maior_valor)

print("---"*15)
print(f"O maior valor enserido é: {maior_valor}")
print(f"A posição que ele está na lista é: {posicao}")