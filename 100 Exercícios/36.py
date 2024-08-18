#36) Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres). Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e o produto das idades do homem mais novo com a mulher mais velha.

homem1 = int(input("Digite a idade do primeiro homem: "))
homem2 = int(input("Digite a idade do segundo homem: "))

mulher1 = int(input("Digite a idade da primeira mulher: "))
mulher2 = int(input("Digite a idade da segunda mulher: "))

homem_mais_velho = max(homem1, homem2)
mulher_mais_velha = max(mulher1, mulher2)
homem_mais_novo = min(homem1, homem2)
mulher_mais_nova = min(mulher1, mulher2)

soma1 = homem_mais_velho + mulher_mais_nova
soma2 = homem_mais_novo + mulher_mais_velha

print(f"A soma da idade do homem mais velho com a mulher mais nova é: {soma1}")
print(f"A soma da idade do homem mais novo com a mulher mais velha é: {soma2}")
