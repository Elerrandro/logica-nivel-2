#75) Escreva um algoritmo que imprima as seguintes sequências de números: (1, 1 2 3 4 5 6 7 8 9 10) (2, 1 2 3 4 5 6 7 8 9 10) (3, 1 2 3 4 5 6 7 8 9 10) (4, 1 2 3 4 5 6 7 8 9 10) e assim sucessivamente, até que o primeiro número (antes da vírgula), também chegue a 10.

for x in range(1, 11):
    print(f"({x},", end=" ")# O 'end=" "' impede a quebra de linha

    for y in range(1, 11):
        print(y, end=" ") # Imprime cada número da sequência sem quebrar a linha

    print(")") # Fecha o parêntese e pula para a próxima linha