#21) ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os minutos) e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.


inicio = int(input("Insira que hora inicia o jogo: "))
fim = int(input("Insira que o jogo acaba: "))

hora = fim - inicio

if fim >= inicio:
    print(f"A duração é de {hora} horas")
else:
    soma = hora + 24
    print(f"A duração é de {soma} horas (dia seguinte)")
