#28) ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.

n1 = int(input("Insira um valor: "))
n2 = int(input("Insira outro valor: "))
n3 = int(input("Insira outro valor: "))

maior_valor = max(n1, n2, n3)

print(f"O maior valor é: {maior_valor}")
