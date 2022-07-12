#Arthur Sandim
#URI 1009 - https://www.beecrowd.com.br/judge/pt/problems/view/1009
nome = str(input())
salario = float(input())
vendas = float(input())

porcentagemComissao = (15/100)

total = salario + (vendas * porcentagemComissao)

print (f'TOTAL = R$ {total:.2f}')