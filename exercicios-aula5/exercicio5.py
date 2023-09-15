#Escrever um programa de computador que leia o código do item pedido, a
#quantidade e calcule o valor a ser pago por aquele lanche. Caso seja digitado
#um código que não existe, envie a mensagem “Item não encontrado no
#cardápio”.

codigoItem = int(input("Digite o código do seu pedido: "))

if (codigoItem<100) or (codigoItem>105):
    print("Este código não existe! Digite um código de 100 a 105")
else:
    quantidade = int(input("Digite a quantidade: "))
    if (codigoItem == 100):
        valorFinal = quantidade*7.9
    if (codigoItem == 101):
        valorFinal = quantidade*4.9
    if (codigoItem == 102):
        valorFinal = quantidade*6.5
    if (codigoItem == 103):
        valorFinal = quantidade*9.9
    if (codigoItem == 104):
        valorFinal = quantidade*10.9
    if (codigoItem == 105):
        valorFinal = quantidade*3.6

print("O valor total da compra é R$",valorFinal)
    
