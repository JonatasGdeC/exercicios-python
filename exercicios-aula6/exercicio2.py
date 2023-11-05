##2- Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual
##ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

while usuario == senha:
  print('A senha não pode ser igual ao usuário!')
  usuario = input('Digite seu usuário: ')
  senha = input('Digite sua senha: ')
