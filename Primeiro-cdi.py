# Approval or disapproval of students
a = float(input('Digite a nota do Primeiro bimestre:'))
while a > 10:
    a = int(input('Você digitou errado. Insira a nota do Primeiro bimestre:'))

b = float(input('Digite a nota do Segundo bimestre:'))
while b > 10:
    b = int(input('Você digitou errado. Insira a nota do Segundo bimestre:'))

c = float(input('Digite a nota do Terceiro bimestre:'))
while c > 10:
    c = int(input('Você digitou errado. Insira a nota do Terceiro bimestre:'))

d = float(input('Digite a nota do Quarto bimestre:'))
while d > 10:
    d = int(input('Você digitou errado. Insira a nota do Quarto bimestre:'))

media = (a + b + c + d) / 4
if a <= 10 and b <= 10 and c <= 10 and d <= 10 and a >= 7 and b >= 7 and c >= 7 and d >= 7:
    print('A media do aluno foi: {}'.format(media))
    print('Aluno aprovado!')
else:
    print('A media do aluno foi: {}'.format(media))
    print('Aluno reprovado!')


# To pass, the average must be greater than or equal to '7'.
