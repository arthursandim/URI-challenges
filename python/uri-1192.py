#Arthur Sandim
#https://www.beecrowd.com.br/judge/pt/problems/view/1192

casos = int(input())
produto = 0
soma = 0

for i in range(0,casos):
    seq = input()
    for i in seq:
        numA = int(seq[0])
        numB = int(seq[2])
        letra = seq[1]
    if(numA == numB or numB == numA):
        produto = numA * numB
        print(produto)
    elif(letra == letra.lower()):
        soma = numA + numB
        print(soma)
    elif(letra == letra.upper()):
        soma = numB - numA
        print(soma)