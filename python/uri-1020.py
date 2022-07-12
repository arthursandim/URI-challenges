#Arthur Sandim
#URI 1020 - https://www.beecrowd.com.br/judge/pt/problems/view/1020

idadeEmDias = int(input())

idadeAnos = idadeEmDias // 365
idadeMeses = (idadeEmDias % 365) // 30
idadeEmDias = (idadeEmDias % 365) % 30

print(f'{idadeAnos} ano(s)')
print(f'{idadeMeses} mes(es)')
print(f'{idadeEmDias} dia(s)')