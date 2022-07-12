#Arthur Sandim
#https://www.beecrowd.com.br/judge/pt/problems/view/2339

quantCompetidores, quantFolhas, folhasCompetidores = [int(x) for x in input().split()]

if (quantCompetidores * folhasCompetidores <= quantFolhas):
    print('S')
else:
    print ('N')