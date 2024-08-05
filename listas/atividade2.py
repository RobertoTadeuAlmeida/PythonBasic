import random

def vencedor(j1,j2):
    global vj1
    global vj2
    global emp
    if j1 == 1 & j2 == 3 :
        vj1 += 1
    elif j1 == 3 & j2 == 2:
        vj1 += 1
    elif j1 == 2 & j2 == 1:
        vj1 += 1
    elif j1 == j2 :
        emp += 1
    else:
        vj2 += 1




print('JOKENPO')
print('1 - PEDRA\n2 - PAPEL\n3 - TESOURA\n0 - SAIR')

placar = []
jogadas = []
vj1 = 0
vj2 = 0
emp = 0



while True:


    j1 = int(input('Sua vez: '))

    if j1 > 3:
        print('Opção invalida tente novamente...')
        continue

    elif j1 == 0:
        print(jogadas)
        print(f'O jogador 1 contabilizou {vj1} vitorias')
        print(f'O jogador 2 contabilizou {vj2} vitorias')
        print(f'Numero de empates: {emp}')
        break

    j2 = random.randint(1,3)
    jogadas.append ([j1,j2])
    vencedor(j1,j2)


    print(f'vez do adversario: {j2}')