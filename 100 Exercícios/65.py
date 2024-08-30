#65) Ler 2 valores, calcular e escrever a soma dos inteiros existentes entre os 2 valores lidos (incluindo os valores lidos na soma). Considere que o segundo valor lido será sempre maior que o primeiro valor lido.

valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))

while valor2 <= valor1:
  print("VALOR INVÁLIDO")
  print("Por favor digitar um valor maior")
  valor2 = int(input("Digite outro valor: "))

soma = valor1 + valor2
print(f"A soma do {valor1} e {valor2} resulta em: {soma}")
