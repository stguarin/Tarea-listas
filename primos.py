num = int(input('digite el numero para comprobar si es primo '))
x= 0

for i in range(2,num):
    if num%i==0:
        print('el numero no es primo')
        x=1
        break

if x==0:
    print('el numero es primo')

nombre = 'santiago'
print(nombre[0])