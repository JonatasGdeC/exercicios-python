#8- Faça um programa que leia 5 números e informe a soma e a média dos números.

somar = 0
media = 0
contador = 0
while contador<5:
  contador+=1
  numeroX = int(input('Digite um número: '))
  somar += numeroX
  media += numeroX/5
  if(contador==5):
    print("O resultado da soma dos número digitados é:",somar)
    print("O resultado da média dos número digitados é:",media)
