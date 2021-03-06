"""String Indice Negativo e Pedaço de Texto.ipynb

Texto: lira@gmail.com

-14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  l   i   r   a   @  g  m  a  i  l  .  c  o  m
  0   1   2   3   4  5  6  7  8  9 10 11 12 13
  
Para pegar um texto de trás para frente: texto[índice] -> onde índice é negativo
Para pegar o pedaço de um texto use : (dois pontos). texto[:indice] ou texto[indice:] ou ainda texto[indice:indice]
"""

from cgi import print_arguments


email = 'lira@gmail.com'
nome = 'João Paulo Lira'

print(email[:3])
print(email[:-3])
print(email[3:])
print(email[5:8])

"""Exercícios para Fixação:
Basta completar os prints de forma correta
"""

print('Tamanho do e-mail ' + str(len(email)) + ' caracteres')
print('Primeiro Caractere ' + email[0])
print('Último Caractere ' + email[-1])
print('Servidor do email ' + email[5:10])