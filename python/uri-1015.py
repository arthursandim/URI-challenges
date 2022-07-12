#Arthur Sandim
#URI 1015 - https://www.beecrowd.com.br/judge/pt/problems/view/1015
import math

x1, y1 = [float(x) for x in input().split()]
x2, y2 = [float(x) for x in input().split()]

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f'{distancia:.4f}')