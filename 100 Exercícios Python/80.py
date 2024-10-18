#80) Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor.

Q = []

while len(Q) < 20:
    ler = int(input(f"Digite algum valor: "))
    if ler > 0:
        Q.append(ler)
    else:
        print("===AVISO===")
        print("Por favor digitar somente números positivos!!!")


maior_valor = max(Q)
posicao = 1 + Q.index(maior_valor)

print("---"*15)
print(f"O maior valor enserido é: {maior_valor}")
print(f"A posição que ele está na lista é: {posicao}")