#Num determinado Estado, para transferências de veículos, o DETRAN cobra
#uma taxa de 1% para carros fabricados antes de 2000 e uma taxa de 1.5% para
#os fabricados de 2000 em diante, taxa esta incidindo sobre o valor de tabela do
#carro. O programa abaixo lê o ano e o preço do carro e a seguir calcula e imprime
#imposto a ser pago.

preco = int(input("Digite a valor da tabela fipe do carro: R$ "))
ano = int (input("Digite agorao ano de fabricação do veículo: "))

if (ano < 2000):
    taxa = preco*0.1
    print("O valor da taxa para um veículo com ano de fabricação antes de 2000, e com tabela fipe de R$",preco,"é de",taxa)
else:
    taxa = preco*0.15
    print("O valor da taxa para um veículo com ano de fabricação depois de 2000, e com tabela fipe de R$",preco,"é de",taxa)
