def valida_fat(pergunta,min,max):
    x = int(input(pergunta))
    while ((x < 0)or (x>99999999)):
        x = int(input(pergunta))
    return x


def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Arquivo não pode ser criado.')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso!\n')

def cadastrarJogo(nomeArquivo, nomeJogo, nomevideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abir o arquivo!')
    else:
        a.write(f'{nomeJogo};{nomeVideogame}\n')
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a= open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        print(a.read())
    finally:
        a.close()


arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador.')
else:
    print('Arquivo inexistente.')
    criaArquivo(arquivo)

while True :
    print('MENU')
    print('1 - Cadastrar novo iten')
    print('2 - Listar cadastros')
    print('3 - Sair')

    op = valida_fat("Digite a opção desejada: ", 1, 3)
    if (op == 1):
        print('Opção de cadastrar novo iten selecionada...\n')
        nomeJogo = input("Digite o nome do jogo:")
        nomeVideogame = input('Digite o nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)

    elif (op == 2):
        print('Opção de listar selecionada...\n')
        listarArquivo(arquivo)
    elif (op == 3):
        print('Encerrando programa...')
        break