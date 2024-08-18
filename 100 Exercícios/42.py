#42) Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou não. Para estar em condições, um dos seguintes requisitos deve ser satisfeito: 

#- Ter no mínimo 65 anos de idade.
#- Ter trabalhado no mínimo 30 anos.
#- Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.

#Com base nas informações acima, faça um algoritmo que leia: o número do empregado (código), o ano de seu nascimento e o ano de seu ingresso na empresa. O programa deverá escrever a idade e o tempo de trabalho do empregado e a mensagem 'Requerer aposentadoria' ou 'Não requerer'.

cod_empregado = int(input("Insira o código do empregado: "))
ano_nascimento = int(input("Insira o ano de seu nascimento: "))
ano_ingresso = int(input("Insira o ano de ingresso na empresa: "))

ano = 65 #anos de idade
trabalhado = 30 #anos
ano_trabalhado = 60 and 25#anos

if ano_nascimento >= ano:
    print(f"A idade do empregado é: {ano_nascimento}")
    print(f"O tempo trabalhado é: {ano_ingresso}")
    print(f"Requerer aposentadoria")
elif ano_nascimento >= trabalhado:
    print(f"A idade do empregado é: {ano_nascimento}")
    print(f"O tempo trabalhado é: {ano_ingresso}")
    print(f"Requerer aposentadoria")
elif ano_nascimento >= 65 >= 25:
    print(f"A idade do empregado é: {ano_nascimento}")
    print(f"O tempo trabalhado é: {ano_ingresso}")
    print(f"Requerer aposentadoria")
else:
    print(f"A idade do empregado é: {ano_nascimento}")
    print(f"O tempo trabalhado é: {ano_ingresso}")
    print(f"Não Requerer")
