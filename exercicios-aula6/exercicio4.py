#4- Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
#taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma
#taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de
#anos necessários para que a população do país A ultrapasse ou iguale
#a população do país B, mantidas as taxas de crescimento.

paisA = 80000
paisB = 200000
contadorAno=0

while paisA <= paisB:
  contadorAno+=1
  paisA = paisA + (paisA*0.03)
  paisB = paisB + (paisB*0.015)
  if (paisA >= paisB):
    print('A quantidade de anos necessário para que a população do país A seja maior qua a população B é de', contadorAno, 'anos.')

