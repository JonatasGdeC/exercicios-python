# Faça um algoritmo que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se que este sofreu um aumento de 15,3%.

salarioAtual = int(input("Digite o atual salário do funcionário: R$ "))
salarioReajustado = salarioAtual + (salarioAtual*0.153)

print("O novo salário do funcionário com reajuste de 15,3% será R$", salarioReajustado)
