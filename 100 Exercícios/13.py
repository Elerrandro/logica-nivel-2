#13) faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno. Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5. Fórmula para o cálculo da média final é:

n1 = float(input("Insira sua primeira nota: "))
n2 = float(input("Insira sua segunda nota: "))
n3 = float(input("Insira sua terceira nota: "))

peso_nota1 = 2
peso_nota2 = 3
peso_nota3 = 5

soma = (n1 * peso_nota1 + n2 * peso_nota2 + n3 * peso_nota3) / 10

print(f"Sua nota é: {soma}")
