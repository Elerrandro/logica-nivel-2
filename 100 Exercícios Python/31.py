#31) ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e escrever se formam ou não um triângulo. OBS: para formar um triângulo, o valor de cada lado deve ser menor que a soma dos outros 2 lados.

a = int(input("Insira um numero"))
b = int(input("Insira outro numero"))
c = int(input("Insira outro numero"))

if a < b + c and b < c + a and c < a + b:
    print("Forma um triângulo")
else:
    print("Não forma um triângulo")
