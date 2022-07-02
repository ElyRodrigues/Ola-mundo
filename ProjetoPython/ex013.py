#Faça um algoritimo que leia o salário de um funcionário 
#e mostre seu novo salário, com 15% de aumento
num1 = float(input('Entre com o valor de seu salário: '))
num2 = num1 * 1.15
print(f'Seu salário R${num1}, após um aumento de 15%, vai passar a valer R${num2:.2f}')
