from random import randint

numero = randint(2, 50)
print("número {}".format(numero))
for i in range(2, numero):
    for y in range(2,i):
        if (i % y) ==0:
            break
    else:
        print(i, "número primo")
