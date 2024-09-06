#73) A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. Faça um algoritmos para coletar dados sobre o salário e número de filhos de cada habitante e após as leituras, escrever:

#a) Média de salário da população
#b) Média do número de filhos
#c) Maior salário dos habitantes
#d) Percentual de pessoas com salário menor que R$ 150,00

#Obs.: O final da leituras dos dados se dará com a entrada de um “salário negativo”.

lista_nome = []
lista_salario = []
lista_filhos = []
while True:
  populacao = int(input("Nessa Pesquisa, quantas pessoas vão ser entrevistadas: "))
  if populacao <= 0:
    break
  else:
    for x in range(populacao):
      nome = str(input("Insira o seu nome: "))
      salario = float(input("Insira o seu sálario: "))
      filhos = int(input("Insira quantos filhos tem: "))
    
      lista_nome.append(nome)
      lista_salario.append(salario)
      lista_filhos.append(filhos)
    
    #(A)media do sálario da população
    valor_total = sum(lista_salario)
    media_salario = valor_total / len(lista_salario)
    
    
    #(B)média de filhos da população
    filhos_total = sum(lista_filhos)
    media_filho = filhos_total / len(lista_filhos)
    
    
    #(C)o maior sálario entre a população
    maior_salario =  max(lista_salario)
    
    
    #(D)Percentual de pessoas com salário menor de R$150,00
    pessoas_menor_150 = list(filter(lambda x: x < 150, lista_salario))
    total_pessoas = len(lista_salario)
    pessoas_salario_menor_150 = len(pessoas_menor_150)
    percentual = (pessoas_salario_menor_150 / total_pessoas) * 100
    
    print("-----" * 30)
    
    print(f"A média do sálario da população é: R${media_salario:.2f}")
    print(f"A média de filhos da população é: {media_filho:.0f}")
    print(f"O maior sálario entre a população é: R${maior_salario:.2f}")
    print(f"O percentual de pessoas com salário menor que R$150,00 é: {percentual:.2f}%")
