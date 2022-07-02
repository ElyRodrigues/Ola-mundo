#Faça o algoritimo que leia o preço de um produto e mostre seu novo preço, 
# com 5% de desconto
preco = float(input('Digite o preço do produto: '))
novopreco = preco - ((5/100)*preco)
print('O novo preço com desconto de 5% é de {} reais'.format(novopreco))