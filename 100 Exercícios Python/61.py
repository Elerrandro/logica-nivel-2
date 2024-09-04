#61) Ler 10 valores, calcular e escrever a média aritmética desses valores lidos.

valores = []

for x in range(1, 11):
    valores.append(int(input("Insira um valor inteiro: ")))
    
soma = (sum(valores))
media = soma / 10
print(f"A média dos valores lidos é {media}")
