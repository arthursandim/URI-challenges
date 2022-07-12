#Arthur Sandim
#URI 1021 - https://www.beecrowd.com.br/judge/pt/problems/view/1021

valorMonet = float(input())

notaCem = valorMonet // 100
valorMonet = valorMonet - notaCem * 100

notaCinq = valorMonet // 50
valorMonet = valorMonet - notaCinq * 50

notaVinte = valorMonet // 20
valorMonet = valorMonet - notaVinte * 20

notaDez = valorMonet // 10
valorMonet = valorMonet - notaDez * 10

notaCinco = valorMonet // 5
valorMonet = valorMonet - notaCinco * 5

notaDois = valorMonet // 2
valorMonet = valorMonet - notaDois * 2

notaUm = valorMonet // 1
valorMonet = valorMonet - notaUm * 1
notaUm= float('%.2f'% notaUm)
valorMonet=float('%.2f'% valorMonet)

moedaCinq = valorMonet // 0.5
valorMonet = valorMonet - moedaCinq * 0.5
moedaCinq = float('%.2f'% moedaCinq)
valorMonet=float('%.2f'% valorMonet)

moedaVintCinc = valorMonet // 0.25
valorMonet = valorMonet - moedaVintCinc * 0.25
moedaVintCinc = float('%.2f'% moedaVintCinc)
valorMonet = float('%.2f'% valorMonet)

moedaDez = valorMonet // 0.10
valorMonet = valorMonet - moedaDez * 0.10
moedaDez = float('%.2f'% moedaDez)
valorMonet = float('%.2f'% valorMonet)

moedaCinco = valorMonet // 0.05
valorMonet = valorMonet - moedaCinco * 0.05
moedaCinco = float('%.2f'% moedaCinco)
valorMonet = float('%.2f'% valorMonet)

moedaUm = valorMonet * 100
moedaUm = float('%.2f'% moedaUm)
valorMonet = float('%.2f'% valorMonet)

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(notaCem)))
print('{} nota(s) de R$ 50.00'.format(int(notaCinq)))
print('{} nota(s) de R$ 20.00'.format(int(notaVinte)))
print('{} nota(s) de R$ 10.00'.format(int(notaDez)))
print('{} nota(s) de R$ 5.00'.format(int(notaCinco)))
print('{} nota(s) de R$ 2.00'.format(int(notaDois)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(int(notaUm)))
print('{} moeda(s) de R$ 0.50'.format(int(moedaCinq)))
print('{} moeda(s) de R$ 0.25'.format(int(moedaVintCinc)))
print('{} moeda(s) de R$ 0.10'.format(int(moedaDez)))
print('{} moeda(s) de R$ 0.05'.format(int(moedaCinco)))
print('{} moeda(s) de R$ 0.01'.format(int(moedaUm)))