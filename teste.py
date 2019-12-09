'''
nome = 'Cristiana'

print('hello')

print('{0}'.format(nome))

nome = 'Diego'

print('{0}'.format(nome))

numero = 42

numero = numero + 58

print('{0}'.format(numero))

for n in range(10):
    print('Estou imprimindo o número {0}'.format(n))

nome = input('Qual o seu nome?')

print('Ola {0}'.format(nome))

a = 2

b = 3

print('O número é', a)

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo: '))

print(n1+n2)

a = str(2**1000000)

print(len(a))

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
if a > b:
    print("O primeiro é maior que o segundo")
if b > a:
    print('O segundo é maior que o primeiro')

idade = int(input('Digite qual a idade do seu carro: '))
if idade <= 3:
    print('Seu carro é novo')
if idade > 3:
    print('Seu carro é velho')
 
v = int(input('Qual a velocidade do veiculo:'))
if v > 110:
    print('Usuário foi multado')
    multa = (v-110)*5
    print ('Valor da multa: R$ %5.2f' %multa)

# Estruturas Aninhadas

minutos = int(input('Minutos utilizados: '))
if minutos < 200:
    preço = 0.20
else:
    if minutos <= 400:
        preço = 0.18
    else:
        preço = 0.15
print('Conta telefonica: R$%6.2f' %(minutos * preço))

minutos = int(input('Minutos utilizados: '))
if minutos < 200:
    preço = 0.20
elif minutos <= 400:
    preço = 0.18
elif minutos <= 800:
    preço = 0.15    
else:
    preço = 0.08

print('Conta telefonica: R$%6.2f' %(minutos * preço))

n1 = int(input('primeiro: '))
n2 = int(input('segundo: '))
n3 = int(input('terceiro: '))
if n1 >= n2 and n1 >= n3:
    print (n1)
elif n2 >= n3:
    print ('segundo: %d' %n2)
else:
    print (n3)

    Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
    da área a ser pintada. Considere qua a cobertura da tinta é de 1 litro para cada 3 metros quadrados
    e  que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
    Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
    obs: somente são vendidos um número inteiro de latas.

m = int(input('metros: '))
if m % 54 != 0:
    latas = (m/54) +1
else:
    latas = m/54

valor = latas * 80

print ('%d lata(s) no valor de %2f' %(latas,valor))

x = 1
while x <= 3:
    print (x)
    x = x+1

n = int(input('número: '))
x = 1
while x <= n:
    print(x)
    x = x + 1

# somente números pares

n = int(input('número: '))
i = 0
while i <= n:
    i = i + 1
    if i % 2 == 0:
        print(i)

# sem usar o if:

n = int(input('número: '))
i = 0
while i <= n and i % 2 == 0:
    print(i)
    i = i + 1
  #ou
n = int(input('número: '))
i = 0
while i <= n:
    print(i)
    i = i + 2      

# Número impares:

n = int(input('número: '))
i = 1
while i <= n:
    print(i)
    i = i + 2   
#ou
n = int(input('número: '))
i = 0
while i <= n:
    i = i + 1
    if i % 2 != 0:
        print(i)

# Multiplos de 3

n = int(input('número: '))
i = 0
while i <= n:
    i = i + 1
    print('%d' %(i*3))

# Acumuladores
n = 1 #contador
soma = 0
while n <= 10:
    x = int(input('Digite o %d número: ' %n))
    soma = soma + x
    n = n + 1
print ('Soma: %d' %soma)

# Média
n = 1
soma = 0
while n <= 10:
    x = int(input('Digite o %d número: ' %n))
    soma = soma + x
    n = n + 1
print ('Média: %5.2f' %(soma/10))

# Fatorial de dez
n = 1
fat = 1
while n <= 10:
    fat = fat * n
    n = n + 1
print ('Fat(10 = %d)' %fat)

# Fatorial de um inteiro
n = int(input('número: '))
i = 1
fat = 1
while i <= n:
    fat = fat * i
    i = i + 1
print ('Fat(%d= %d)' %(n, fat))

# Interronpendo a repetição
soma = 0
while True: # significa, que não tem condição de parada, esse programa não tem uma parada prevista. Aqui somente terá uma parada prevista quando digitar o zero
    x = int(input('Digite o número (0 sai): '))
    if x == 0:
        break
    soma = soma + x
print ('Soma: %d' %soma)

# Repetições aninhadas
tabuada = 1
while tabuada <= 10:
    n = 1
    print ('Tabuada %d' %tabuada)
    while n <= 10:
        print ('%d x %d = %d'
                %(tabuada, n, tabuada*n))
        n = n+1
    tabuada = tabuada +1

# Sequencia Fibonacci
n = int(input('N: '))
a, b = 1, 1
k = 1

while k <= n-2:
    a, b = b, a + b
    k = k+1
print('Fib(%d) = %d' %(n,b))

# Algoritmo de Euclides
a = int(input('a: '))
b = int(input('b: '))

while a % b != 0:
    a,b = b, a % b

print('mdc = %d' %b)

#Média de 5 notas
notas = [1,2,3,4,5]
count = 0
soma = 0
while count < 5:
    soma += notas[count]
    count += 1
print ('Média: %5.2f' %(soma/count))


# Faça um programa que leia um vetor de 5 números inteiros e mostre o vetor
vetor = []
i = 1
while i <= 5:
    n = int(input("Digite um número: "))
    vetor.append(n)
    i = i +  1
    print("Vetor lido:", vetor)

# Faça um programa que leia um vetor de dez números reais e mostre-os na ordem inversa
vetor = []
i = 1
while i <= 10:
    n = float(input("Digite um número: "))
    vetor.append(n)
    i += 1
i = 9
while i >= 10:
    print(vetor[i])
    i -= 1


# Faça um programa que leia quatro notas, mostre as notas e a média na tela
notas = []
count = 0
soma = 0
while count < 4:
    n = float(input("Digite uma nota: "))
    notas.append(n)
    soma += notas[count]
    count += 1
print('Notas:', notas)
print ('Média: %5.2f' %(soma/count))

# Faça um Programa que leia um vetor de 10 caracteres minusculos, e diga quantas consoantes foram lidas
letras = []
i = 1
while i <= 10:              
    letras.append(input("Letra: "))
    i += 1
i = 0
cont = 0
while i <= 9:
    if letras[i] not in 'aeiou':    # quanto queremos perguntar se uma coisa esta dentro de um conjunto de possibilidades: variável IN conjunto
        cont += 1                   # no código usamos NOT IN, quer dizer, aquela letra NÃO ESTA em 'aeiou'. Se esta no conjunto não irá contar, senão estiver será uma consoante e contará.
    i += 1
print('Foram lidos %d consoantes' %cont)

# Ler mais sobre Fatiamento ou Fatias de Listas (pegar pedaços (vídeo TWP280 Strings))
# Verifique se uma palavra é palíndrome
palavra = input('Palavra: ')
if palavra == palavra[::-1]: #inverte a palavra ou a string (strings são imutáveis)
    print('%s é palíndrome' % palavra)
else:
    print('%s não é palíndrome' % palavra)

# Faça um programa que leia uma palavra e troque as vogais por  "*"
palavra = input('Palavra: ')
i = 0
troca = ''
while i < len(palavra):
    if palavra[i] in 'aeiou':
        troca = troca + '*'
    else:
        troca = troca + palavra[i]
    i += 1
print('Nova palavra %s' %troca)
'''
# Faça um programa que solicite a data de nascimento (dd/mm/aaaa)e imprima com o nome do mês por extenso
from collections import defaultdict

names_dict = defaultdict(list)
names_dict["Bob"] = 1
names_dict["Katie"] = 2
sara_number = names_dict["Sara"]
print(names_dict)





