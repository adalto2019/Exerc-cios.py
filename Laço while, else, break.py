#Escreva um programa que peça ao usuário para adivinhar um número que você deverá escolher com
#antecedência até que ele acerte. Para ajudar o usuário, o programa deve informar se o número é
#maior ou menor que o número a ser adivinhado. Ao final,imprima o número adivinhado e a quantidade
#de tentativas.

numeroSelecionado = 12

print("--- TESTE A SUA SORTE!! ADIVINHE O NUMERO '?' ---")
x = int(input("Digite um numero de 1 a 20 e acerte ao numero da interrogação: "))

cont = 0 #Contando qtd de vezes que e tentado achar o numero '?'
while numeroSelecionado != x:
    if (x <= 20) and (x > 12): #Se maior, retorna a msg 'Maior que ?'          
        x = int(input("Numero MAIOR que '?'. Tente novamente!! :"))
    
    elif (x >= 0) and (x < 12): #Se menor, retorna a msg 'Menor que ?'        
        x = int(input("Numero MENOR que '?'. Tente novamente!! :"))
        cont = cont + 1

    else: #Se o usuário não informar o valores na faixa solicitada o programa se encerra.
        print('---------------------------------------------')                
        print("Sabe nem Bricar.. Valor inválido. GAME OVER!")   
        break 

else: #while-else retornando a mensagem abaixo ao encerrar o loop
    print('---------------------------------------------------------------------')                
    print(f"PARABÉNS!! Você acertou o numero da sorte: *12*, após {cont} tentativa(s)..")  
    

