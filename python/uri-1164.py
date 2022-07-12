#Arthur Sandim
#https://www.beecrowd.com.br/judge/pt/problems/view/1164

n = int(input())
while not (1 <= n <= 20):
    n = int(input())

for i in range(n):
    soma = 0
    j = 1
    x = int(input())
    divisores = list()
    while not (1 <= x <= 10**8):
        print()
        x = int(input())
    while j < x:
        if x % j == 0:
            divisores.append(j)
        j += 1
    
    for element in divisores:
        soma += element

    if soma == x:
        print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')