a= int
#nueva variable cant_gallinas donde se calcula la cantidad de gallinas excluyendo a los pollos
cant_galli = (a//3)//2
#se calcula la cantiddad de huevos producidos
huev_cad3= cant_galli*10
huev_cad5=cant_galli*6
#se halla el total de huevos producidos y se imprime
tot=huev_cad3+huev_cad5
print(f'la cantidad aproximada de huevos producidos en un mes es de {tot}')