#Arthur Sandim
#URI 1037 - https://www.beecrowd.com.br/judge/pt/problems/view/1037

valor = float(input())

if (0 <= valor <= 25):
    print ('Intervalo [0,25]')
elif (25 < valor <= 50):
    print ('Intervalo (25,50]')
elif (50 < valor <= 75):
    print ('Intervalo (50,75]')
elif (75 < valor <= 100):
    print ('Intervalo (75,100]')
elif (valor < 0 or valor > 100):
    print ('Fora de intervalo')