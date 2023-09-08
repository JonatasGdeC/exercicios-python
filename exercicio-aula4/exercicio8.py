#O lucro de uma empresa é dado por L(x) = 10x – 5000, onde x é a quantidade de
#produtos vendidos num determinado mês. Elabore um algoritmo que calcule o
#lucro mensal dessa empresa.

produtosVendidos = int(input("Digite a quantida de produtos vendidos este mês: "))
lucro = (10*produtosVendidos)-5000

if(lucro<0):
    divida = lucro*(-1)
    print("Este mês a empresa não possui lucro. O contrário, obteve uma dívida de R$",divida)
else:
    print("O lucro da empresa este mês é de R$",lucro)
