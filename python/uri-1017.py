#Arthur Sandim
#URI 1017 - https://www.beecrowd.com.br/judge/pt/runs/code/27548172
tempoViagem = int(input())
velocidade = int(input())

distancia = velocidade * tempoViagem

consumo = distancia/12

print(f'{consumo:.3f}')