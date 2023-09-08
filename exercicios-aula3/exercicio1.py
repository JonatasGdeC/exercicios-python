#Faça um algoritmo que leia dois números e escreva (devolva como resultado) o menor deles.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um segundo número: "))

if (num1 == num2):
  print("Os números são iguais")
else:
  if (num1>num2):
    print("O número maior é ",num1)
  else:
    print("O número maior é ",num2)
