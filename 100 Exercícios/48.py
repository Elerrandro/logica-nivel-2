#48) Escreva um algoritmo para ler as notas da 1a. e 2a. avaliações de um aluno, calcule e imprima a média (simples) desse aluno. Só devem ser aceitos valores válidos durante a leitura (0 a 10) para cada nota.

nome = str(input("Digite o nome do Aluno: "))
AV1 = float(input("Digite a nota da primeira avaliação: "))
AV2 = float(input("Digite a nota da segunda avaliação: "))

while AV1 > 10 or AV1 < 0 or AV2 > 10 or AV2 < 0:
    print("Por favor inserir um valor de (0 a 10)")
    AV1 = float(input("Digite a nota da primeira avaliação: "))
    AV2 = float(input("Digite a nota da segunda avaliação: "))

media = (AV1 + AV2) / 2

print(f"A média do {nome} é {media:.2f}")