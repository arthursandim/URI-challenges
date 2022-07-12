#Arthur Sandim
#https://www.beecrowd.com.br/judge/pt/problems/view/1173

N = list()
N.append(int(input()))
i = 0

while i<10:
    print(f'N[{i}] = {N[i]}')
    N.append(N[i]*2)
    i+=1