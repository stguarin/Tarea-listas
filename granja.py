v = int(input('digite la cantidad de vacas '))
a= int(input('digite la cantidad de aves '))
e = int(input('digite la cantidad de escorpiones '))

k = int(input('ingrese la cantidad de litros de leche que producen las vacas tras pastar 1 metro cuadrado '))
x = int(input('ingrese la cantidad de metros cuadrados que pastan las vacas en un dia '))
litros = v*(k*x)
print(f'la cantidad de litros de leche producidos por dia en la granja es de: {litros}\nla cantidad de litros de leche que produce la granja en una semana es de: {litros*7}')
cant_galli = (a//3)//2
huev_cad3= cant_galli*10
huev_cad5=cant_galli*6
tot=huev_cad3+huev_cad5
print(f'la cantidad aproximada de huevos producidos en un mes es de {tot}')
