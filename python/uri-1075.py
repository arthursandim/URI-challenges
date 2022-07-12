#Arthur Sandim
#https://www.beecrowd.com.br/judge/pt/problems/view/1075

N = int(input())
contador = 1

while (contador <= 10000):
    if (contador % N == 2):
        print (contador)
    contador += 1