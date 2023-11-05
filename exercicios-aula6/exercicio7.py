#7- Faça um programa que leia 5 números e informe o maior número.

contador = 0
numeros = []
while contador<5:
  contador+=1
  numeros.append(int(input('Digite um número: ')))
  if(contador == 5):
    print(max(numeros))
