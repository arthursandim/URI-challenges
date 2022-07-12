#Arthur Sandim
#https://www.beecrowd.com.br/judge/pt/problems/view/2378

linhas, capacidadeMaxima = [int(x) for x in input().split()]
saida = 0
entrada = 0
soma = 0
acumulador = 0
maior = 0

for i in range (0,linhas):
    saida,entrada = [int(x) for x in input().split()]
    soma = -(saida) + entrada
    acumulador += soma
    if (acumulador > maior):
        maior = acumulador
    
    
if (maior > capacidadeMaxima):
    print('S')
else:
    print('N')
    