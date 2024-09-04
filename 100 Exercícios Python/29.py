#29) ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.

n1 = int(input("Insira um valor: "))
n2 = int(input("Insira outro valor: "))
n3 = int(input("Insira outro valor: "))

maior_valor = max(n1, n2, n3)
menor_valor = min(n1, n2, n3)
soma = n1 + n2 + n3 - menor_valor

print(f"A soma dos dois maiores valor é: {soma}")
