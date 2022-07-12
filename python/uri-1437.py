#Arthur Sandim
#https://www.beecrowd.com.br/judge/pt/problems/view/1437

while True:
    N = int(input())
    while (N<0 or N>1000):
        N = int(input())
    if (N == 0):
        break
    direcao = input()
    direcao = list(direcao)
    if (len(direcao) != N):
        print()
        direcao = input()
        direcao = list(direcao)
    a = 0
    
    for i in direcao:  
        if (i.upper() == 'E'):
            a -= 90
        else:
            a += 90
        
        if (a == 360 or a == -360):
            a = 0
    if (a == 0):
        print('N')
    elif a == 180 or a == -180:
        print ('S')
    elif a > 0:
        print ('L')
    else:
        print ('O')