#Arthur Sandim
#https://www.beecrowd.com.br/judge/pt/problems/view/2399


def campoMin(lista,n):
    c=0
    while c<n:
        if len(lista)==1:
            print(lista[c])
        elif c==0:
            print(lista[c]+lista[c+1])
        elif c>0 and c<n-1:
            print(lista[c]+lista[c-1]+lista[c+1])
        else:
            print(lista[c]+lista[c-1])
        c+=1


N = int(input())
while N<1 or N>50:
    N = int(input())

tab = list()

for i in range(N):
    tab.append(int(input()))

campoMin(tab,N)