#ex 01#

a = input('Qual seu nome?')

print(a)

#ex 02#

av1 = int(input('Qual foi a sua nota da AV1?'))

av2 = int(input('Qual foi a sua nota da AV2?'))

s = (av1+av2) /2

if s>=6:
    print('Você passou')
else:
    print('Você foi reprovado')

#ex03#

n1 = float(input('Digite um numero aleatorio: '))

if n1>=10 and n1<=99:
    print('True')
else:
    print('False')

#ex04#

ano = int(input('Qual o seu ano de nascimento?'))

if ano<= 2005:
    print('Você tem mais de 18 anos')
else:
    print('Você é menor de idade')
    
#ex05#

f1 = "É genial festejar o sucesso, mas é mais importante aprender com as lições do fracasso."
f2 = "Os líderes do futuro são os que empoderam os outros."
f3 = "É mais fácil ser o primeiro, do que continuar a ser o primeiro."

print(f1 + f2 + f3)


#ex06#

p1 = float(input('Qual foi a sua nota na primeira prova: '))
p2 = float(input('Qual foi a sua nota na segunda prova: '))
p3 = float(input('Qual foi a sua nota na terceira prova: '))

res = (p1 + p2 + p3)/3

if res>=7:
    print('Você passou')
else:
    print('Você foi reprovado')

#ex 07#

nome = input('Qual seu nome?')

print('Olá',nome, 'Tudo bem?')
