#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e quantos dólares ela pode comprar
#Considerando o dólar a R$3,27 
num1 = float(input('Quanto dinheiro você possui na carteira: '))
num2 = 3.27
num3 = num1 / num2
print(f'Considerando que o dólar esta valendo R${num2} reais,' 
f'\nvocê poderá comprar US${num3} dólares')