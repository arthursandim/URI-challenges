#Arthur Sandim
#URI 1008 - https://www.beecrowd.com.br/judge/pt/problems/view/1008
numFuncionario = int(input())
horasTrabalhadas = int(input())
valorPorHora = float(input())

salario = horasTrabalhadas * valorPorHora

print(f'NUMBER = {numFuncionario}')
print (f'SALARY = U$ {salario:.2f}')