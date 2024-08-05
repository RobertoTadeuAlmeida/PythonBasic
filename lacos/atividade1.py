print('Bem vindo a lanchonete jucelino')
print('Aqui esta nosso cardapio\n','-'*10,'-'*10,'\n 1-Coxinha R$5,00\n 2-Pastel R$7,00\n 3-Café R$4,00\n 4-Suco R$6,00\n 5-Finalizar\n','-'*10,'-'*10)


total = 0
while True :
    print('Digite a opção desejada:')
    pedido = int (input(''))
    msgQnt = 'Quantas unidades deseja comprar? '
    if pedido == 1 :
        print(msgQnt)
        qnt = int(input(''))
        total = total + qnt * 5.00
    elif pedido == 2 :
        print(msgQnt)
        qnt = int(input(''))
        total = total + qnt * 7.00
    elif pedido == 3 :
        print(msgQnt)
        qnt = int(input(''))
        total = total + qnt * 4.00
    elif pedido == 4 :
        print(msgQnt)
        qnt = int(input(''))
        total = total + qnt * 6.00
    elif pedido == 5 :
        print(f"O valor do seu pedido e de R${total}")
        break

    else : print('Produto inexistente por favor selecione outro')

