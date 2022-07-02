#Escreva um programa que converta um temperatura digitada em °C e a converta para °F:
celsius = float(input('Digite a temperatura em °C: '))
print('A temperatura em Fahrenheit é {:.1f} °F.'.format(celsius * 1.8 + 32))