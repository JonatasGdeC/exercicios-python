#10- Faça um programa que receba dois números inteiros e
#gere os números inteiros que estão no intervalo compreendido por eles.

numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))

while numero1 == numero2:
  print('Digite números distintos...')
  numero1 = int(input('Digite um número inteiro: '))
  numero2 = int(input('Digite outro número inteiro: '))

if(numero1<numero2):
  while numero1<numero2:
    numero1+=1
    if(numero1==numero2):
      break
    print(numero1)
else:
  while numero2<numero1:
    numero2+=1
    if(numero2==numero1):
      break
    print(numero2)
