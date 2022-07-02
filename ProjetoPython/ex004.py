# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis nela:


a = input('Digite alguma coisa: ')
print('O tipo de primitivo desse valor é:', type(a))
print('Só tem espaços', a.isspace())
print('É um número', a.isnumeric())
print('É alfabético', a.isalpha)
print('É alfanumérico', a.isalnum())
print('Está em maiuscula', a.isupper())
print('Está em minuscula', a.islower())
print('Está em capitalizada', a.istitle())
