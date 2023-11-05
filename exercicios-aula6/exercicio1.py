##1- Faça um programa que peça uma nota, entre zero e dez.
##Mostre uma mensagem caso o valor seja inválido e continue
##pedindo até que o usuário informe um valor válido.


nota = int(input('Digite sua nota: '))

while (nota < 0) or (nota > 10):
  print('Digite um número de 0 a 10!')
  nota = int(input('Digite sua nota: '))
