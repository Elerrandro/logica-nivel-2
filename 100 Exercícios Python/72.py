#72) Faça um algoritmo para ler o código e o preço de 15 produtos, calcular e escrever: 
#- o maior preço lido
#- a média aritmética dos preços dos produtos

cod = []
preco = []

for x in range(15):
  codigo = int(input("Insira o código: "))
  produto = float(input("Insira o preço do produto: "))
  cod.append(codigo)
  preco.append(produto)

#busca o maior preço
maior_preco = max(preco)
#busca a posição do maior preço
indeci_maior_preco = preco.index(maior_preco)
#liga a posição do preço com o código correspondente
maior_cod = cod[indeci_maior_preco]


#calcula a média do preço
valor_total = sum(preco)
media = valor_total / len(preco)

print(f"O maior preço lido é: R${maior_preco} e o código do produto é: {maior_cod}")
print(f"A média dos preços dos produtos é: R${media}")
