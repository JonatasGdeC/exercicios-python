#Escreva um algoritmo para ler o salário mensal atual de um funcionário e o
#percentual de reajuste. Calcular e escrever o valor do novo salário


salarioAtual = int(input("Digite o atual salário mensal do funcionário: "))
reajusteEntrada = int(input("Digite a porcentagem do reajuste: "))
reajustePercentual = reajusteEntrada/100

while True: 
    print("(1) Aumento de salário")
    print("(2) Redução de salário")
    reajuste = int(input("Digite qual será a tipo de reajuste de acordo com as opções acima: "))

    if (reajuste <=0 or reajuste>2):
        print("As opções são 1 e 2 !")
    else:
        if(reajuste == 1):
            novoSalario = salarioAtual + (salarioAtual*reajustePercentual)
            print("Parabéns! Você recebeu um aumento de",reajusteEntrada,"% no seu salário. Seu novo salário é de R$",novoSalario)
            break
        else:
            novoSalario = salarioAtual - (salarioAtual*reajustePercentual)
            print("Infelizmente tivemos que reduzir",reajusteEntrada,"% do seu salário. Seu novo salário é  de R$",novoSalario)
            break
