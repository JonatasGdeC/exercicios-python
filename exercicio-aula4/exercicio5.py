#. A padaria Hotpão vende certa quantidade de pães franceses e uma quantidade de broas a cada
#dia. Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia, o dono quer saber
#quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar numa conta de
#poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono. Com
#base nestes fatos, faça um algoritmo para ler as quantidades de pães e de broas, e depois
#calcular os dados solicitados.

paes = int(input("Digite a quantidade de pães vendidos hoje: "))
broas = int(input("Digite a quantidade de broas vendidas hoje: "))

paesLucros = paes*0.12
broasLucros = broas*1.5

lucroTotal = paesLucros+broasLucros
valorPoupanca = lucroTotal-(lucroTotal*0.1)

print("O lucro total com a vendas de pães e broas hoje foi de R$",lucroTotal,". Sendo assim, o valor de 10% que deve ser depositado na poupança é R$",valorPoupanca)

