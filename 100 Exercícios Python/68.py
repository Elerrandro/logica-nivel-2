#68) Uma loja está levantando o valor total de todas as mercadorias em estoque. Escreva um algoritmo que permita a entrada das seguintes informações: a) o número total de mercadorias no estoque; b) o valor de cada mercadoria. Ao final imprimir o valor total em estoque e a média de valor das mercadorias. 

#O número total de mercadorias no estoque.
total_estoque = int(input("Insira o número total de mercadorias no estoque: "))

#O valor de cada mercadoria.
valor_mercadoria = []

for x in range(total_estoque):
    mercadoria = float(input(f"Insira o valor da {x+1}° mercadoria: "))
    valor_mercadoria.append(mercadoria)

#valor total das mercadorias
valor_total = sum(valor_mercadoria)
#média do valor das mercadorias.
media = valor_total / total_estoque

# Impressão dos resultados
print(f"Valor total em estoque: R$ {valor_total:.2f}")
print(f"Média de valor das mercadorias: R$ {media:.2f}")