#Recebe dois números inteiros positivos e imprime os números entre eles que são primos.
n1 = int(input('Digite um numero positivo inteiro: '))
n2 = int(input('Digite outro numero positivo inteiro: '))
#Primos de 1 a 10: 2,3,5,7.
for x in range(n1, n2):#range mostra os valores entre os inputs 'n1' e 'n2'.
    if n1 > 0:
     if x > 2:
         for z in range(2, x):#2° laço começando do digito 2 e incrementando outro digito a cada laço.
            if (x % z == 0):
                break
         else:
            print(x)