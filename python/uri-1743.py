#Arthur Sandim
#https://www.beecrowd.com.br/judge/pt/problems/view/1743

def plugLinha(l1,l2):
    cont=0
    while True:
        if cont>=5:
            break
        if l1[cont]!=l2[cont]:
            cont+=1
        else:
            break
        
    if cont==5:
        return True
    else:
        return False
    
lista1=[int(x) for x in input().split()]
lista2=[int(x) for x in input().split()]

if plugLinha(lista1,lista2):
    print('Y')
else:
    print('N')