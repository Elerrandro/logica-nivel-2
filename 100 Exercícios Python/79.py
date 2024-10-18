#79) Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos. Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada. Escrever a média da turma e o resultado da contagem.

notas = []
contador = 0

for x in range(1, 21):
    nota = float(input(f"Digite a nota do {x}° aluno: "))
    notas.append(nota)

media = sum(notas) / len(notas)

for nota in notas:
    if nota > media:
        contador = contador + 1
        
print("---"*15)
print(f"A média da turma é: {media:.2f}")
print(f"Quantidade de alunos acima da média: {contador}")