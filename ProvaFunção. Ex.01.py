#Escreva uma função que recebe um determinado ano e retorne o século daquele ano.
def seculo():
     if ano >=1 and ano <= 100:
          return (f'Ano: {ano}, pertence ao século: I')
     elif ano >=101 and ano <= 200:
          return (f'Ano: {ano}, pertence ao século: II')
     elif ano >=201 and ano <= 300:
          return (f'Ano: {ano}, pertence ao século: III')
     elif ano >=301 and ano <= 400:
          return (f'Ano: {ano}, pertence ao século: IV')
     elif ano >=401 and ano <= 500:
          return (f'Ano: {ano}, pertence ao século: V')
     elif ano >=501 and ano <= 600:
          return (f'Ano: {ano}, pertence ao século: VI')
     elif ano >=601 and ano <= 700:
          return (f'Ano: {ano}, pertence ao século: VII')
     elif ano >=701 and ano <= 800:
          return (f'Ano: {ano}, pertence ao século: VIII')
     elif ano >=801 and ano <= 900:
          return (f'Ano: {ano}, pertence ao século: IX')
     elif ano >=901 and ano <= 1000:
          return (f'Ano: {ano}, pertence ao século: X')
     elif ano >=1001 and ano <= 1100:
          return (f'Ano: {ano}, pertence ao século: XI')
     elif ano >=1101 and ano <= 1200:
          return (f'Ano: {ano}, pertence ao século: XII')
     elif ano >=1201 and ano <= 1300:
          return (f'Ano: {ano}, pertence ao século: XIII')
     elif ano >=1301 and ano <= 1400:
          return (f'Ano: {ano}, pertence ao século: XIV')
     elif ano >=1401 and ano <= 1500:
          return (f'Ano: {ano}, pertence ao século: XV')
     elif ano >=1501 and ano <= 1600:
          return (f'Ano: {ano}, pertence ao século: XVI')
     elif ano >=1601 and ano <= 1700:
          return (f'Ano: {ano}, pertence ao século: XVII')
     elif ano >=1701 and ano <= 1800:
          return (f'Ano: {ano}, pertence ao século: XVIII')
     elif ano >=1801 and ano <= 1900:
          return (f'Ano: {ano}, pertence ao século: XIX')
     elif ano >=1901 and ano <= 2000:
          return (f'Ano: {ano}, pertence ao século: XX')
     elif ano >=2001 and ano <= 2100:
          return (f'Ano: {ano}, pertence ao século: XXI')
     else:
          print('ERRO!, verifique o ano informado e tente novamente!')

ano = int(input("Digite um ano para saber o século em que ele se enquadra: "))
print('------------------------------------------------')
print('O Resultado para o ano informado é:\n' , seculo())