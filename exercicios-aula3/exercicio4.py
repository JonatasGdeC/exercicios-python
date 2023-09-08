#Faça um algoritmo que receba dois valores nas variáveis A e B respectivamente, troque o valor contido na variável A pelo valor em B, e o valor em B pelo valor em A,
#isto é, ao final do algoritmo, A e B terão os valores trocados.

valorA = int(input("Digite um valor para A: "))
valorB = int(input("Digite um valor para B: "))

valorX = valorA
valorY = valorB

valorA = valorY
valorB = valorX

print("O valor de A é: ", valorA)
print("O valor de B é: ", valorB)
