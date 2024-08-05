palavras = ('Mario', 'Luigi', 'Peach', 'Yoshi', 'Bowser')

for palavra in palavras:
    print(f'\nPalavra: {palavra.upper()}. Vogais:')
    for letras in palavra:
        if letras.lower() in 'aeiou':
            print(letras.upper(), end= ' ')