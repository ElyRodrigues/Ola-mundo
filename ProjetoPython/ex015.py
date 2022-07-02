#Escreva um programa que pergunte a qtd de km rodados por um carro alugado e qtd de dias
#que ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60,00 por dia 
#e R$0,15 por km rodado
dias = int(input('Digite quantos dias o carro ficou alugado: '))
km = float(input('Digite quantos kilometros o carro poercorreu:'))
total = (dias * 60) + (km * 0.15)
print(f'Seu custo pelo aluguel do veículo ficou em R${total}')