# Exercicios.py
Exercícios em Linguagem de Programação Python

<img src = "img.png">


```python
#PRIMEIRO PROGRAMA EM PYTHON: Olá Mundo!
print("Olá Mundo!")
```
```python
#Faça um programa que leia python5 números com a soma e médias deles.
n1 = float(input("Digite um numero: "))
n2 = float(input("Digpythonite outro numero: "))
n3 = float(input("Digite outro numero: "))
n4 = float(input("Digite outro numero: "))
n5 = float(input("Digite outro numero: "))
#Obs. float - numeros de pontos flutuantes. Ex. 2.75
print("---------------------------------")
print("A SOMA dos numeros digitados é: ", n1+n2+n3+n4+n5)
print("A MÉDIA dos numeros digitados é: ", (n1+n2+n3+n4+n5)/5)
```
```python
# Escreva um algoritmo que armazene o valor 10 em uma variável A e o valor 20 em uma variável B.
# A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo com que o valor que está em A
# passe para B e vice-versa.
# Ao final, escrever os valores que ficaram armazenados nas variáveis;
a = 10
b = 20
print('Valores pythonde A e B: ',a , 'e',b)
a, b = 20, 10
print('Valores trocados de A e B: ',a, 'e',b)
```
```python
#Escreva um algoritmo para ler o número total de eleitores de um município,
#o número de votos brancos, nulos e válidos. Calcule e escreva o percentual
#que cada um representa em relação ao total de eleitores;
eleitores =  int(input('Digite o numero total de eleitores: '))
branco = pythonint(input('Digite o numero total de votos brancos: '))
nulos  = int(input('Digite o numero total de votos nulos: '))
validos = int(input('Digite o numero total de votos válidos: '))
print('------------------------------------------------------------')#Espaço
if eleitores == (branco + nulos + validos):
    print('Percentual de votos brancos: ', (branco/eleitores)*100,'%')
    print('Percentual de votos nulos: ',(nulos/eleitores)*100,'%')
    print('Percentual de votos válidos: ',(validos/eleitores)*100,'%')
else:
    print('Erro! os valores digitados não correspondem ao numero total de eleitores.')
```
```python
#Escreva um algoritmo para ler uma temperatura em graus Fahrenheit e, calcule e
#escreva o valor correspondente em graus Celsius. Fórmula: (°F − 32) ÷ 1, 8.
temp = float(input('Digite uma temperatura °F: '))
fomrm = (temp-32)/1.8
print('---------------------------------------')
print('Temperatura em F°:', temp)
print('Temparatura convertida em °C:', round(fomrm, 2))
```
```python
#Faça um programa que leia o sexo de uma pessoa, identificado pelos valores ‘M’ ou ‘F’.
#Caso esteja errado, peça para digitar novamente.
sexo = input('Digite o sexo, M - Masculino e F - Feminino: ')
while sexo != 'm' and sexo != 'f' and sexo != 'M' and sexo != 'F':
    print('-------------Sigla Errada, digite novamente-------------')
    sexo = input('Digite o sexo, M - Masculino e F - Feminino: ')
if sexo == 'M' or sexo == 'm':
        print()
        print('Sexo digitado Masculino.')
elif sexo == 'F' or sexo == 'f':
        print()
        print('Sexo digitado Feminino.')
```

### CONDICIONAIS [1]:

```python
#programa que ler três numeros e imprime o maior.
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite outro numero: "))

if n1 > n2 and n1 > n3:
    print("Numero maior", n1)
elif n2 > n3 and n2 > n1:
    print("Numero maior", n2)
elif n3 > n2 and n3 > n1:
    print("Numero maior", n3)
```
### LAÇO FOR e CONDICIONAIS [1]:

```python
#programa que ler valor inteiro e mostra a tabuada de 1 a 10 do valor lido de acordo com a operação informada.
print("-----TABUADA DE 10-----")
n = int(input("Digite o numero para obter a sua tabuada: "))
op = input("Digite: (+) para somar   (-)para subtrair  (x)para multiplicar  (/)para dividir  :")
for x in range (1, 11):
    if op == '+':
        print(n, "+", x, "=", n+x)
    elif op == '-':
        print(n, "-", x, "=", n-x)
    elif op == 'x':
        print(n, "x", x, "=", n*x)        
    elif op == '/':
        print(n, "/", x, "=", n/x)   
```
### ESTRUTURA DE REPETIÇÃO FOR [1]:

```python
#Imprime na tela os numeros de 1 a 50 ímpares.
for x in range(1, 51):
    if x % 2 == 1:
     print(x) 
```
### FOR ANINHADO [1]:

```python
#dado uma lista com nomes. Exibir os nomes com a lista de sobrenomes.
nomes = ['Adalto', 'Aline', 'Laura', 'Sara']
sobreN = ['Carvalho', 'Marinho']

for x in nomes:
    for z in sobreN:
        x = x + z
        print(x)
```
### ESTRUTURA DE REPETIÇÃO WHILE e CONDICIONAIS[3]:

```python
#programa que ler nome  e senha e não aceita senha igual ao nome,
#mostrando mensagem de erro e voltando a pedir o nome.
h = 0
nome = input("Digite o seu nome: ")
senha = input("Cadastre uma senha: ")
while nome == senha:
    print("ATENÇÃO, senha não pode ser o seu nome, tente novamente.")
    nome = input("Digite o seu nome: ")
    senha = input("Cadastre uma senha: ")
if nome != senha:
    print("NOME e SENHA Gravados com SUCESSO.")    
```
```python
#ESTRUTURA DE REPETIÇÃO {WHILE}: empresa de energia faz leitura mensal dos medidores de consumo, calculando os seguintes dados:
#1. Número do consumidor
#2. Consumo Kwh mês
#3. Tipo do consumidor (1-Residencial R$0,30/Khh, 2-Comercial R$0,50/Khh, 3-Indústria R$0,70/Khh)
#os dados devem ser lidos até achar o comsumidor zero. Programe: custo total de cada consumidor, total de consumo dos três tipos
#e cálcular média de consumo dos tipos 1 e 2.
consumidor = int
somaConsumo1 = 0
somaConsumo2 = 0
somaConsumo3 = 0
contTipo1 = 0
contTipo2 = 0

while consumidor != 0:
    consumidor = int(input("Digite o numero do consumidor: "))    
    consMes= float(input("Digite o consumo do mes: "))
    tipo = int(input("Infome o tipo do cliente 1-Residencial, 2-Comercial, 3_indústrial: ")) 
    

    if tipo == 1 :
        custoConsumidor = consMes * 0.30
        somaConsumo1 = somaConsumo1 + consMes#guarda a soma do consumo do cliente Tipo 1
        contTipo1 += 1
        print("Valor a pagar deste consumidor R$: ", custoConsumidor, "reais")
    elif tipo == 2 :
        somaConsumo2 = somaConsumo2 + consMes#guarda a soma do consumo do cliente Tipo 2
        custoConsumidor = consMes * 0.50
        contTipo2 += 1
        print("Valor a pagar deste consumidor R$: ", custoConsumidor, "reais")
    elif tipo == 3 :
        somaConsumo3 = somaConsumo3 + consMes#guarda a soma do consumo do cliente Tipo 3
        custoConsumidor = consMes * 0.70
        print("Valor a pagar deste consumidor R$: ", custoConsumidor, "reais")
print('---------------RESUMO---------------')
print(contTipo1)
print("Total de consumo do tipo1: ", somaConsumo1, "tipo2: ", somaConsumo2,  "Tipo3: ", somaConsumo3)
print("A Média de Consumo do Tipo1 é: ",somaConsumo1/contTipo1,"e do Tipo2 é: ",somaConsumo2/contTipo2) 
```
```python
#'X' equipes de 3 jogadores em um campeonato de arco e flecha não tiveram
#os mesmos pontos,crie um programa que informe se uma equipe foi classificada seguindos os critérios: 1.ler 
#pontos obitido por cada jogador da equipe, 2.mostrar eses valores em ordem decrecente, 3.se a soma for
#maior do que 100, imprime media. Caso contrário imprime equipe desclassificada.
x = 0
eqp = int(input("Informe quantas equipes irão participar: "))
while x < eqp:
    x = x+1
    j1 = float(input(f"Digite pontos 1° jogador Eqp{x}: "))
    j2 = float(input(f"Digite pontos 2° jogador Eqp{x}: "))
    j3 = float(input(f"Digite pontos 3° jogador Eqp{x}: "))
    print(f"Valores dos pontos da Eqp{x} em ordem decrecente: ", j3, "//", j2, "//", j1)
    if (j1+j2+j3) > 100:
        print("Media dos pontos", (j1+j2+j3)/3)
    else:
        print(f"Equipe {x} desclassificada!") 
```

### LISTAS [5]:

```python
#ler lista de 10 numeros inteiros e mostra na ordem inversa
lista = []
for x in range(1,11):
    n = int(input('Digite numero: '))
    lista.append(n)
lista.reverse()
print(lista)
```
```python
#ler 4 notas e em seguida exibe as notas e a media
lista = []
for x in range(1, 4+1):
    n = int(input(f'Digite nota {x}: '))
    lista.append(n)

print("Notas: ",lista)
print("Media: ", sum(lista)/4)
```
```python
#ler 20 idades e mostra a idade maior e a menor
lista = []
for x in range(20):
    n = int(input(f'Digite idade {x}: '))
    lista.append(n)
print()
print("Idade Maxima: ",max(lista))
print("Idade minima: ", min(lista))
```
```python
#armazenar 10 letras em uma lista e imprime uma listagem enumerada.
lista = []
for x in range(10):
    n = (input('Digite uma letra: '))
    lista.append(n)
for x,i in enumerate(lista):
    print(x+1, "° =", i)
```
```python
#Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule e armazene a média.
#armazene também a situação do aluno: 1- Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
#contendo as notas, a média e a situação de cada aluno. Utilize quantas listas forem necessárias para armazenar os dados.
notas1 = []
notas2 = []
media = []

for x in range(1,3):
    print(f"Digite notas do aluno {x}")
    n1 = float(input("Digite nota um: "))
    notas1.append(n1)
    n2 = float(input("Digite nota dois: "))
    notas2.append(n1)
    media.append((n1+n2)/2)
    print(f"Media aluno {x}", media)
```
### TUPLAS [2]:

```python
#dada uma tupla com N valores, remova todos so numeros pares da tupla
t = ()
print(type(t))
lista = list(t)#Convertendo tupla em uma lista
n = int(input('Informe quantos valores inteiros você quer adicionar: '))
for i in range(n):
    numero = int(input(f'Digite {i+1}° numero : '))#Retorna a marcação do numero que se pede
    if numero % 2 == 1:#Retorna numeros impares
     lista.append(numero)#Retorna na lista os possivéis numeros impares da condição
     t = tuple(lista)
print()
print('Numeros impares digitados dentro da tupla: ', type(t), t)
```
```python
#dada duas tuplas com N valores reais que representa as notas de uma turma
#calcule a media da turma nas provas 1 e 2, imprimindo em qual das provas a turma
#obteve a melhor media
n = int(input('Informe quantas notas serão lançadas: '))
provas1 = ()#Tupla
lista1 = list(provas1)#Convertendo tupla em lista
provas2 = ()#Tupla
lista2 = list(provas2)  # Convertendo tupla em lista
for i in range(n):
    notas1 = float(input(f'Digite nota prova 01: '))
    notas2 = float(input(f'Digite nota prova 02: '))
    lista1.append(notas1)#Adicionando valores da 'notas1' na lista
    lista2.append(notas2)  # Adicionando valores da 'notas2' na lista
    m1 = sum(lista1)/len(lista1)
    m2 = sum(lista2)/len(lista2)
    print()#Espaço
if m1 > m2:
        print('Media Prova 01: ', m1, '||  Média Prova 02: ', m2)
        print('A média das 1° provas foram melhores que a da 2° nessa turnma!')
else:
        print('Media Prova 01: ', m1, '||  Média Prova 02: ', m2)
        print('A média das 2° provas foram melhores que a da 1° nessa turma!')
```
### DICT [0]:

```python

```
### FUNÇÕES [1]:

```python
#Faça um código no qual tenha como principal finalidade definir as colocações dos participantes, leve em conta que,
#é impossível haver empate técnico, a saída do código deverá dizer o nome do participante e sua pontuação adjunto 
#da sua colocação final e por fim defina uma função que consiga abranger todo código e a execute com as pontuações abaixo . 
#Lucas - 1454 pontos
#Pedro - 1243 pontos
#Ricardo - 1452 pontos

def colocacao():#criando um afunção chamada 'colocacao' 
    dic = {}#criando um dicionario vazio
    x = 0
    n = int(input("Informe o número de participantes: "))
    print()#espaço
    while x < n:#laço que ira solicitar nome e pontução conforme numero de participantes informados.
        x+=1
        nome = input(f"Informe o nome do participante N° {x}:  ")#recebe o nome do participante.
        pont = int(input(f"Informe a pontuação do participante N° {x}: "))#recebe a prontução do participante.
        dic.update({nome: pont})#adicionando chave e valores ao dicionario.
    print()#espaço
    print("Classificação 1°, 2°, 3° Lugar:")
    for i in sorted(dic, key = dic.get, reverse=True):#percorrendo o dicionario colocando key e values em ordem descrecente
        print(i, dic[i])#apresentando o resultado
 
colocacao()#Chamando a função chamamada ' colocacao'
```




## Autor 
:snake:
```python
print("Adalto Carvalho Ribeiro Simão Junior.")
```
