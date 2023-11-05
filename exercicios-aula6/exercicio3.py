# 3- Faça um programa que leia e valide as seguintes informações:

#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';
#Use a função len(string) para saber o tamanho de um texto (número de caracteres).

nome = input('Digite seu nome: ')
while len(nome) < 3:
  print('É necessário pelo menos 3 carcteres neste campo!')
  nome = input('Digite seu nome: ')

idade = int(input('Digite sua idade: '))
while (idade<0) or (idade>150):
  print('Digite uma idade de 0 a 150!')
  idade = int(input('Digite sua idade: '))

salario = int(input('Digite seu salário: '))
while salario < 0:
  print('Digite um salário maior ou igual a zero!')
  salario = int(input('Digite seu salário: '))

sexo = input('Informe seu sexo: (M) | (F) ')
while ( sexo.lower() != 'm') and (sexo.lower() != 'f'):
  print('Digite " M " para masculino ou "F" para feminino!')
  sexo = input('Informe seu sexo: (M) | (F) ')

estadoCivil = input('Informe seu estado civil: (S)|(C)|(V)|(D) ')
while (estadoCivil !='s') and (estadoCivil !='c') and (estadoCivil !='v') and (estadoCivil !='d'):
  print('Digite os seguintes valores: \n (S) -> Solteiro \n (C) -> Casado \n (V) -> Viúvo \n (D) -> Divorciado')
  estadoCivil = input('Informe seu estado civil: (S)|(C)|(V)|(D) ')
