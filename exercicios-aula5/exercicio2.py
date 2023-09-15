#Em uma fábrica, uma máquina precisa de manutenção sempre que o número
#de peças defeituosas supera 10% da produção. Dados o total de peças
#produzidas e o total de peças defeituosas, informe se a máquina precisa de
#manutenção.

pecasProduzidas = int(input("Digite a quantidade de peças produziadas: "))
pecasDefeituosas = int(input("Digite agora quantidade de peças produzidas que apresentam defeitos: "))

dezPorcentoProducao = pecasProduzidas * 0.1

if (pecasDefeituosas >= dezPorcentoProducao):
    print("A máquina necessita de manutenção")
else:
    print("A máquina não necessita de manutenção")
