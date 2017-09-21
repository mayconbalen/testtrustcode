from random import randint

lista = [randint(0, 5000000) for x in range(500)]

lista2 = [randint(0, 5000000) for x in range(50000)]



for numero in lista2:
    try:
        idx = lista.index(numero)
        if(idx > 0):
            print(numero)
    except:
        continue


