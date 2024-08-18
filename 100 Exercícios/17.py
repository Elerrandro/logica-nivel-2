#17) ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

a1 = float(input("Insira sua primeira nota: "))
a2 = float(input("Insira sua segunda nota: "))
  
media = (a1 + a2) / 2
print(f"O aluno tirou: {media}")
  
if media >= 6:
    print("O aluno foi APROVADO!")
else:
    print("O aluno foi REPROVADO!")
