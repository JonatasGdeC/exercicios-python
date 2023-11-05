#13- Faça um programa que peça dois números, base e expoente, calcule e mostre o
#primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input('Digite o número base: '))
expoente = int(input('Digite o número expoente: '))
multiplicador=base

if (expoente>=2):
  while expoente > 0:
    expoente-=1
    multiplicador*=base
    if(expoente==1):
      break
else:
  if(expoente == 1):
    multiplicador=base
  else:
    multiplicador=1
print("O resultado é",multiplicador)
