#Arthur Sandim
#https://www.beecrowd.com.br/judge/pt/problems/view/1708

import math
x, y = [int(x) for x in input().split()]
x = y - x
x = math.ceil(y/x)
print(x)