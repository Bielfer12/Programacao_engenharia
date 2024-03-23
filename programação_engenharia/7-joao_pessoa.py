# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
peso=float(input('Digite a quantidade de kilos voce trouxe:'))


if (peso <= 50):
    print("Os kilos sem a tava é:", peso)
else:
    calc = (peso - 50)
    result = (calc * 4.00)
    print("Os kilos são", peso, "e a taxa é", result)