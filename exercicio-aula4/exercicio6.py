#A empresa Hipotheticus paga R$ 30,00 por hora normal trabalhada, e R$ 15,00 por hora extra.
#Faça um algoritmo para calcular e imprimir o salário bruto e o salário líquido de um determinado
#funcionário. Considere que o salário líquido é igual ao salário bruto descontando-se 10% de
#impostos

horasNormais = int(input("Digite quantas horas normais o funcionário trabalhou: "))
horasExtras = int(input("Digite agora quantas horas extras o funcionário trabalhou: "))

salarioNormal = horasNormais*30
salarioExtra = horasExtras*45

salarioBruto = salarioNormal+salarioExtra
salarioLiquido = salarioBruto - (salarioBruto*0.1)

print("o salário bruto do funcionário é de R$",salarioBruto,". Porém, com o desconto de 10% de imposto, o salário líquido é de", salarioLiquido)

