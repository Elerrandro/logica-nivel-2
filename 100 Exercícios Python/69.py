#69) O mesmo exercício anterior, mas agora não será informado o número de mercadorias em estoque. Então o funcionamento deverá ser da seguinte forma: ler o valor da mercadoria e perguntar ‘MAIS MERCADORIAS (S/N)?’. Ao final, imprimir o valor total em estoque e a média de valor das mercadorias em estoque.

valor_mercadoria = []
while True:
    #O valor de cada mercadoria.
    mercadoria = float(input("Insira o valor da mercadoria: "))
    valor_mercadoria.append(mercadoria)
    decisao = str(input("MAIS MERCADORIA (S/N): "))
    
    if decisao != 'S' and decisao != 's':
        
        
        #valor total das mercadorias
        valor_total = sum(valor_mercadoria)
        #média do valor das mercadorias.
        media = valor_total / len(valor_mercadoria)
        
        # Impressão dos resultados
        print(f"Valor total em estoque: R$ {valor_total:.2f}")
        print(f"Média de valor das mercadorias: R$ {media:.2f}")
        break
