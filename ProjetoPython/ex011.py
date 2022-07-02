#Faça um programa que leia a largura e altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necesária para pinta-la,
#Sabendo que a cada litro de tinta, pinta uma área de 2m²

n = int(input('Insira o valor do comprimento em metros da parede: '))
p = int(input('Insira o valor da largura em metros da parede: '))
a = n * p
print(f'A parede tem {a}m²')
if a%2 == 0:
         a = a
         print(f'A parede precisará de  {a/2:.0f} baldes de tinta para ser pintada completa')
else:
         a = a + 1
         print(f'A parede precisará de  { a / 2:.0f} baldes de tinta para ser pintada completa')