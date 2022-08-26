"""Módulo if - Aula 04.ipynb

# Comparadores

==    igual
!=    diferente
>     maior que (>= maior ou igual)
<     menor que (<= menor ou igual)
in    texto existe dentro de outro texto 
not   verifica o contrário da comparação

Obs: Se em alguma condição você não quiser fazer nada, você pode simplesmente escrever:
pass

"""

faturamento_loja_1 = 2500
faturamento_loja_2 = 2200
email = "liragmail.com"

print('Programa 1')
if faturamento_loja_1 == faturamento_loja_2:
    print('Os faturamentos são iguais')
else:
    print('Os faturamentos são diferentes')

print('Programa 2')
if email != 'lira@gmail.com':
    print('Esse não é o email do Lira')
else:
    print('Email errado')

print('Programa 3')
email_usuario = input('Insira seu e-mail:')
if not '@' in email_usuario:
    print('Email Inválido')
else:
    pass