# 10.Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
n1 =  float(input("Digite sua altura:"))

result = (72.7*n1) - 58
print(round(result))

# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
male = input("Digite se voce é m ou f:")
h = float(input("Digite sua altura:"))
homem = (72.7*h) - 58
mulher = (62.1*h) - 44.7

if ( male == 'm') or ( male == 'M'):
    print(round(homem))
else:
    print(round(mulher))
