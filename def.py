def diga_ola(nome):
    a = 1
    print("Olá, {}.".format(nome))

diga_ola("Paulo")

def gerador_num_impar(x):
    return [i for i in range(x) if i % 2 == 1]

gerador_num_impar(11)

a = lambda x: x ** 2
print(a(100))