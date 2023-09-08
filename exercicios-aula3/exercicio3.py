#Sabe-se que o valor de cada 1.000 litros de água corresponde a 2% do salário mínimo.
#Faça um algoritmo que receba o valor do salário mínimo e a quantidade de água consumida em uma residência por mês. Calcule e mostre:

#1) o valor da conta de água.
#2) o valor a ser pago com desconto de 15%.

salarioMinimo = int(input("Digite o valor do salário mínimo: R$ "))
consumoAgua = int(input("Digite a quantidade de litros consumidos no mês: "))

valorConta = (consumoAgua*(salarioMinimo*0.02))/1000
valorContaDesconto = valorConta - (valorConta*0.15)

print("O valor da conta será de R$ ",valorConta)
print("Já o valor da conta com desconto de 15% será de R$ ", valorContaDesconto)
