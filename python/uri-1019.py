#Arthur Sandim
#URI 1019 - https://www.beecrowd.com.br/judge/pt/problems/view/1019

segundos = int(input())

horas = segundos//3600
minutos = (segundos%3600)//60
segundos = segundos%60

print(f'{horas}:{minutos}:{segundos}')