#14- Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade
#de números pares e a quantidade de números ímpares.

contador = 0
contadorPar = 0
contadorImpar = 0

while contador < 10:
  contador+=1
  numero = int(input('Digite um número: '))
  if((numero%2) == 0):
    contadorPar+=1
  else:
    contadorImpar+=1
  if(contador == 10):
    print('A quantidade de números pares', contadorPar)
    print('A quantidade de números impares', contadorImpar)
