#Arthur Sandim
#https://www.beecrowd.com.br/judge/pt/problems/view/1038

codigo, quantidade = [int(x) for x in input().split()]

if (codigo == 1):
    total = quantidade * 4.00
    print(f'Total: R$ {total:.2f}')
elif (codigo == 2):
    total = quantidade * 4.50
    print(f'Total: R$ {total:.2f}')
elif (codigo == 3):
    total = quantidade * 5.00
    print(f'Total: R$ {total:.2f}')
elif (codigo == 4):
    total = quantidade * 2.00
    print(f'Total: R$ {total:.2f}')
elif (codigo == 5):
    total = quantidade * 1.50
    print(f'Total: R$ {total:.2f}')