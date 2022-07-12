#Arthur Sandim
#https://www.beecrowd.com.br/judge/pt/problems/view/1796


q = int(input())
cont1=0
cont0=0
while not (4 <= q <= 233000):
    q = int(input())

v = [int(x) for x in input().split()]

for element in v:
    if element == 1:
        cont1+=1
    elif element == 0:
        cont0+=1

if cont1>=cont0:
    print('N')
else:
    print('Y')