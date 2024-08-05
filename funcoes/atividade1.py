def valida_fat(pergunta,min,max):
    x = int(input(pergunta))
    while ((x < 0)or (x>99999999)):
        x = int(input(pergunta))
    return x


def fatorial (num):

    fat = 1
    if num == 0 :
        return fat

    for i in range(1,num+1):
        fat*= i
    return fat


x = valida_fat('Digite um valor para calcular a fatorial: ',0,99999999)
print(f'{x}! = {fatorial((x))}')