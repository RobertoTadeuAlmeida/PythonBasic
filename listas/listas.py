nota = [9,7,7,10,3,9,6,6,2]

#Trocando ultimo valor da Lista
nota[-1] = 4

#Encontra um valor expecifico na Lista
print(nota.count(7))
print(nota)

#Pega a maior nota
print(max(nota))

#Coloca os valores em orden crescente
nota.sort()
print(nota)

#Pegando media dos valores
print(sum(nota) / len(nota))