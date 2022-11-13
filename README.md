# Exercicios.py
Exercícios em Linguagem de Programação Python

<img src = "img.png">

#

```
#1. PRIMEIRO PROGRAMA EM PYTHON: Olá Mundo!
print("Olá Mundo!")
```
```
#2. Faça um programa que leia 5 números com a soma e médias deles.
n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))
n3 = float(input("Digite outro numero: "))
n4 = float(input("Digite outro numero: "))
n5 = float(input("Digite outro numero: "))
#Obs. float - numeros de pontos flutuantes. Ex. 2.75
print("---------------------------------")
print("A SOMA dos numeros digitados é: ", n1+n2+n3+n4+n5)
print("A MÉDIA dos numeros digitados é: ", (n1+n2+n3+n4+n5)/5)
```
```
#3. CONDICIONAIS: programa que ler três numeros e imprime o maior.
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
```
#4. LAÇO {FOR} e CONDICIONAIS: programa que ler valor inteiro e mostra a tabuada de 1 a 10 do valor lido de acordo com a operação informada.
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
```
#5. ESTRUTURA DE REPETIÇÃO {FOR}: #Imprime na tela os numeros de 1 a 50 ímpares.
for x in range(1, 51):
    if x % 2 == 1:
     print(x) 
```
```
#6. {FOR} ANINHADO: dado uma lista com nomes. Exibir os nomes com a lista de sobrenomes.
nomes = ['Adalto', 'Aline', 'Laura', 'Sara']
sobreN = ['Carvalho', 'Marinho']

for x in nomes:
    for z in sobreN:
        x = x + z
        print(x)
```
```
#7. ESTRUTURA DE REPETIÇÃO {WHILE}: programa que ler nome  e senha e não aceita senha igual ao nome,
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
```
#8. ESTRUTUTA DE REPETIÇÃO e CONDICIONAIS: 'X' equipes de 3 jogadores em um campeonato de arco e flecha não tiveram
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
```

```
```

```
```

```
```

```




## Autor
:snake:  Adalto Carvalho RIbeiro Simão Junior.
