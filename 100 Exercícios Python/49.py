#49) Acrescente uma mensagem 'NOVO CÁLCULO (S/N)?' ao final do exercício [48]. Se for respondido 'S' deve retornar e executar um novo cálculo, caso contrário deverá encerrar o algoritmo.

while True:
    nome = str(input("Digite o nome do Aluno: "))
    AV1 = float(input("Digite a nota da primeira avaliação: "))
    AV2 = float(input("Digite a nota da segunda avaliação: "))

    while AV1 > 10 or AV1 < 0 or AV2 > 10 or AV2 < 0:
        print("Por favor inserir um valor de (0 a 10)")
        AV1 = float(input("Digite a nota da primeira avaliação: "))
        AV2 = float(input("Digite a nota da segunda avaliação: "))

    media = (AV1 + AV2) / 2

    print(f"A média do {nome} é {media:.2f}")
    novo_calculo = str(input("NOVO CÁLCULO (S/N)?: "))

    if novo_calculo != 'S' and novo_calculo != 's':
        print("ENCERRANDO ALGORITMO!")
        break