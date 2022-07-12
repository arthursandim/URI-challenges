#Arthur Sandim
#https://www.beecrowd.com.br/judge/pt/problems/view/1261


def calculo(lista,dicio):
    soma = 0
    for element in lista:
        if element.lower() in dicio.keys():
            soma += dicio[element]
    return soma

n,m = [int(x) for x in input().split()]


palavras = dict()
for i in range(n):
    palavra = input().split()
    palavra[1] = int(palavra[1])
    while len(palavra[0]) > 16 or palavra[1] > 1000000:
        print()
        palavra = input().split()
        palavra[1] = int(palavra[1])
    palavras[palavra[0]] = palavra[1]



for j in range(m):
    descricoes = list()
    while True:
        desc = list()
        desc = input().split()
        if desc == ['.']:
            break
        descricoes += desc[:]

    print(calculo(descricoes, palavras))