#Arthur Sandim
#https://www.beecrowd.com.br/judge/pt/problems/view/2434

diasPeriodo, saldoConta = [int(x) for x in input().split()]
contador = 1
menorSaldo = saldoConta
while(contador <= diasPeriodo):
    movimentacao = int(input())
    contador += 1
    saldoConta = saldoConta + movimentacao
    if (menorSaldo > saldoConta):
        menorSaldo = saldoConta
print (menorSaldo)