#62) Ler o número de alunos existentes em uma turma e, após isto, ler as notas destes alunos, calcular e escrever a média aritmética dessas notas lidas.

while True:
    aluno = str(input("Digite o nome do aluno: "))
    AV1 = float(input("Digita a primeira nota: "))
    AV2 = float(input("Digita a primeira nota: "))
    media = (AV1 + AV2) / 2
    print(f"A média do {aluno} é {media}")
    
    decisao = str(input("Quer continuar (S/N): "))
    if decisao != 'S' and decisao != 's':
        print("ENCERRANDO ALGORITMO !")
        break
