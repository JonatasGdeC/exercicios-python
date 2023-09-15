#Dada a idade de um nadador, informe a sua categoria: Infantil (até 10 anos),
#Juvenil (até 17 anos) ou Sênior (acima de 17 anos).

idade = int(input("Digite a idade do nadador: "))

if (idade <= 10):
    print("Nadador categoria infantil")
else:
    if (idade >= 18):
        print("Nadador categoria Sênior")
    else:
        print("Nadador categoria Juvenil")
