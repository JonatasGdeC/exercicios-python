#Num triângulo retângulo, segundo Pitágoras, o quadrado da hipotenusa (a) é igual à soma dos quadrados dos catetos (b e c), isto é, a² = b² + c².
#Faça um algoritmo, receba os valores dos catetos e imprima o valor da hipotenusa.

catetoB = int(input("Digite o valor do cateto 1: "))
catetoC = int(input("Digite o valor do cateto 2: "))

hipotenusa = ((catetoB*catetoB)+(catetoC*catetoC))**(1/2)

print("O valor da hipotenusa é: ", hipotenusa)
