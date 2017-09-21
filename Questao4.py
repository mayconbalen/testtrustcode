import string
def isPrimo (numero):
    for i in range(2, numero):
        if (numero % i) == 0:
            print("não é palavra prima")
            break
    else:
        print("palavra prima")

valores = list (string.ascii_lowercase)
valores.extend(list(string.ascii_uppercase))
palavra = "TrustCode"
total = 0
print("palavra escolhida: ", palavra)
for letra in palavra:
    valor = valores.index(letra) + 1
    total = total + valor
isPrimo(total)

