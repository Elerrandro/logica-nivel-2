#41) Faça um algoritmo para ler as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação. Calcular a média de aproveitamento, usando a fórmula abaixo e escrever o conceito do aluno de acordo com a tabela de conceitos mais abaixo:

#Média_de_aproveitamento = (N1 + N2 * 2 + N3 * 3 + Média _dos_ Exercícios)/7  

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media_exercicios = float(input("Digite a media dos exercicios: "))

media_aproveitamento = (n1 + n2 * 2 + n3 * 3 + media_exercicios) / 7

if media_aproveitamento >= 9:
    conceito = 'A'
elif media_aproveitamento >= 7.5 < 9:
    conceito = 'B'
elif media_aproveitamento >= 6.5 < 7.5:
    conceito = 'C'
elif media_aproveitamento < 6:
    conceito = 'D'
    
print(f"O conceito do aluno é {conceito}")
