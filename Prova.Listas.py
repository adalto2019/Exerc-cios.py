#Você foi convidado para escrever um programa que leia o nome do asteroide e uma lista das suas últimas 5 distâncias
# da Terra. Armazene os dados em um dicionário, onde a chave é o nome do asteroide. Exiba no final a distância média
# de todos os asteroides registrados.
listaA = [2.4, 3.3, 4, 4.3, 5]#milhões de quilômetros da terra
listaB = [3.4, 3.9, 4.2, 6.3, 8.4]#milhões de quilômetros da terra
print('***Asteroides mapeados até momento: alfaA e betaB***')
asteroide = input('Digite o nome do asteroide: ')
print()#Espaço
if asteroide == 'alfaA':
    dicionarioA = {'alfaA': listaA}#Armazenando dados em um dicionário, onde a chave e o nome do asteroide.
    print('Últimas cinco distâncias apuradas do asteroide alfaA foram:', dicionarioA['alfaA'],',milhões de km da terra.')
    print('Com uma distância média de: ', sum(listaA)/5,'Km da terra.')#Cálcula a distância média do asteroide foco do interesse.
elif asteroide == 'betaB':
    print(f'Últimas cinco distâncias apuradas do asteroide: betaB foram:{listaB}, milhões de km da terra.')
else:
    print('ATENÇÃO! Nome de asteroide digitado não catalogado. Tente novamente.')