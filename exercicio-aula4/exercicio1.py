#A imobiliária Imóbilis vende apenas terrenos retangulares ou quadrados. Faça um
#algoritmo para ler as dimensões de um terreno e depois exibir a área do mesmo.

base = int(input("Digite quantos metros possui a base do terreno: "))
altura = int(input("Digite agora quantos metros possui a altura do terreno: "))

area = base*altura

if (base == altura):
    print("O terreno possui um formato quadrado com",area,"m de área")
else:
    print("O terreno possui um formato retangular com",area,"m de área")
