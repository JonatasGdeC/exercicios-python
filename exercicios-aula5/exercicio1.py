#Faça um algoritmo que receba um número e diga se este número está no
#intervalo entre 100 e 200.

num = int(input("Digite um número qualquer: "))

if (num >= 100) and (num <= 200):
    print("O número digitado está entre 100 e 200")
else:
    if (num<100):
        print("O número digitado é menor que 100")
    if (num>200):
        print("O número digitado é maior que 200")
    
