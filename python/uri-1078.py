#Arthur Sandim
#https://www.beecrowd.com.br/judge/pt/problems/view/1078

tabuada = int(input())
contador = 1

while (contador < 11):
    print(f'{contador} x {tabuada} = {tabuada * contador}')
    contador += 1