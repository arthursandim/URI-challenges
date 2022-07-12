#Arthur Sandim
#https://www.beecrowd.com.br/judge/pt/problems/view/2229

teste = 1
resultado = 0
while True:
    N = int(input())
    if (N == - 1):
        break
    if (N > 15):
        N = int(input())
    print(f'Teste {teste}')
    teste += 1
    if (N == 0):
        resultado = 4
    elif (N == 1):
        resultado = 9
    else:
        resultado = (1+2**N)*(1+2**N)
    print (resultado)
    print()