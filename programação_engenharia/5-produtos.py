# 6.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# 7.o produto do dobro do primeiro com metade do segundo 
# 8.a soma do triplo do primeiro com o terceiro.
# 9.o terceiro elevado ao cubo.

n1 =  int(input("Digite um numero"))
n2 =  int(input("Digite um numero"))
n3 =  float(input("Digite um numero"))

soma = n1 + n2 + n3
prod= n1 * 2 *(n2/2)
soma2 = (n3 + n1) * 3
elevado = n3**3
print('A soma de todos é',soma,'Sei la 1:',soma2,'sei la 2:',prod,'sei la 3:',elevado)
