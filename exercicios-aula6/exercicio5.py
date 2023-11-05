#5- Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
#Valide a entrada e permita repetir a operação.

print("Digite a quantidade de habitantes e taxa de crescimento anual e veja quantos anos leva para que a menor população iguale com a maior população...")

def calculando():
  ##Validação do campo de entrada do país A:
  paisA = int(input('Digite a quantidade de habitantes no país A: '))
  while paisA <= 0:
    print("É necessário que exista população né???")
    paisA = int(input('Digite a quantidade de habitantes no país A: '))

  taxaA = int(input('Digite a taxa de crescimento anual do país A em porcentagem: (Apenas números!) '))
  while taxaA <= 0:
    print("Taxa de crescimento maior ou igual a 0 não é crescimento!")
    taxaA = int(input('Digite a taxa de crescimento anual do país A em porcentagem: (Apenas números!) '))
  taxaAporcento = taxaA/100

  ##Validação do campo de entrada do país B:
  paisB = int(input('Digite a quantidade de habitantes no país B: '))
  while paisB <= 0:
    print("É necessário que exista população né???")
    paisB = int(input('Digite a quantidade de habitantes no país B: '))

  taxaB = int(input('Digite a taxa de crescimento anual do país B em porcentagem: (Apenas números!) '))
  while taxaB <= 0:
    print("Taxa de crescimento maior ou igual a 0 não é crescimento!")
    taxaB = int(input('Digite a taxa de crescimento anual do país B em porcentagem: (Apenas números!) '))
  taxaBporcento = taxaB/100

  contadorAno=0

  ##Caso número digitado para "país A" seja menor que "país B"
  if paisA<paisB:
    while paisA <= paisB:
      contadorAno+=1
      paisA = paisA + (paisA*taxaAporcento)
      paisB = paisB + (paisB*taxaBporcento)
      if (paisA >= paisB):
        print('A quantidade de anos necessário para que a população do "país A" seja maior qua a população do "país B" é de', contadorAno, 'anos.')
        break
  ##Caso número digitado para "país B" seja menor que "país A"
  else:
    while paisB <= paisA:
      contadorAno+=1
      paisA = paisA + (paisA*taxaAporcento)
      paisB = paisB + (paisB*taxaBporcento)
      if (paisB >= paisA):
        print('A quantidade de anos necessário para que a população do "país B" seja maior qua a população do "país A" é de', contadorAno, 'anos.')
        break

calculando()
novamente = input('Deseja realizar uma nova conta?\n Sim -> (S)\n Não -> Qualquer outra tecla...\n').lower()

while novamente == 's':
  calculando()
  novamente = input('Deseja realizar uma nova conta?\n Sim -> (S)\n Não -> Qualquer outra tecla...\n').lower()
  if novamente != 's':
    break
