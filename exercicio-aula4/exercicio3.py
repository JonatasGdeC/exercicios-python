#Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos
#dias de vida ela possui. Considere sempre anos completos, e que um ano possui
#365 dias. Ex.: Uma pessoa com 19 anos possui 6935 dias de vida.

print("Descubra quantos dias vividos você possui!")
nome = input("Por favor, digite seu nome: ")
print("Olá", nome)
idade =  int(input("Digite agora a sua idade: "))

diasVividos = idade*365

print(nome,", você possui aproximadamente",diasVividos,"dias vividos...")

