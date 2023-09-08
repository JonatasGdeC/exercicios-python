#O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição.
#Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e
#imprima o valor a pagar. Assuma que a balança já desconte o peso do prato.

while True: 
    peso = int(input("Digite aqui quantos quilos possui seu prato: "))
    valorPagar = peso*12
  
    if peso <= 0:
        print("Digite o peso em Kgs")        
    else:
        print("Para o prato de",peso,"Kgs, o valor a ser pago será R$",valorPagar)
        break
