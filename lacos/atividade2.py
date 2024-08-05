totalPessoas = 0
dinheiro = 0
totalIdade = 0

while True :

    idade = int(input("Ola bem vindo ao cinema em casa, para saber o valor do seu ingresso informe sua idade: \nSe deseja sair digite 0: "))
    if idade == 0 :
        break
    totalPessoas += 1
    totalIdade += idade

    if idade < 3 :
        ingresso = 0
    else :
        if idade > 12 :
            ingresso = 30
        else :
            ingresso = 15
    dinheiro += ingresso

if totalPessoas > 0 :
    media = totalIdade / totalPessoas
    print(f'Total de pessoas são: {totalPessoas}')
    print(f'Total arrecadado é: {dinheiro}')
    print(f'Media de idade dos clientes são: {media}')