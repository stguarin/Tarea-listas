## Autores Arnold Joseph Merchan Rojas  y Santiago Guarin Alfaro
##ejercicio litros de leche y numeros de huevos
#se defininenvariables
v = int(input('digite la cantidad de vacas '))
a= int(input('digite la cantidad de aves '))
e = int(input('digite la cantidad de escorpiones '))
#variables de entradapara litros que produce y metros que pata cada vaca
k = int(input('ingrese la cantidad de litros de leche que producen las vacas tras pastar 1 metro cuadrado '))
x = int(input('ingrese la cantidad de metros cuadrados que pastan las vacas en un dia '))
#se hallan la cantidd de litros que se producen
litros = v*(k*x)
#se imprime el resultado
print(f'la cantidad de litros de leche producidos por dia en la granja es de: {litros}\nla cantidad de litros de leche que produce la granja en una semana es de: {litros*7}')
#nueva variable cant_gallinas donde se calcula la cantidad de gallinas excluyendo a los pollos
cant_galli = (a//3)//2
#se calcula la cantiddad de huevos producidos
huev_cad3= cant_galli*10
huev_cad5=cant_galli*6
#se halla el total de huevos producidos y se imprime
tot=huev_cad3+huev_cad5
print(f'la cantidad aproximada de huevos producidos en un mes es de {tot}')
