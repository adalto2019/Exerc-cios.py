#Mudar 3 listas de animais dentro de uma listaA, para outra listaB. E no fim exibir o resultado das modificações
#usando funções de manipulação de listas

vaca = ['vaca =','branco', 'preto', 'cinza', 'caramelo']
porco = ['porco =','branco', 'preto', 'cinza', 'caramelo']
galinha = ['galinha =','branco', 'preto', 'cinza', 'caramelo']
carneiro = ['carneiro =','branco', 'preto', 'cinza', 'caramelo']
pasto1 = [vaca, porco, galinha, carneiro]
pasto2 = []
print('***Distribuição inicial dos animais nos pastos***')
print('Pasto 01: ', pasto1)
print('Pasto 02: ', pasto2)

pasto1.pop()#removendo o ultimo animal da lista do pasto1
pasto1.remove(porco)#removendo um animal pelo o seu valor
del pasto1[0]#removendo um animal pelo index

pasto2.append(carneiro)#adicionando animal ao final da lista
pasto2.insert(0, porco)#adicionando animal na posição index indicada
pasto2.extend([vaca])#adicionando um ou vários animais a lista
print()
print('***Distribuição final dos animais nos pastos***')
print('Pasto 02: ', pasto2)
print('Pasto 01: ', pasto1)