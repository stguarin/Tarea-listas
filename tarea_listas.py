# ejercicio 1 original: desarrollar un programa que determine si en una lista no existen elementos repetidos
# variacion del ejersicio 1: Desarrollar un programa que elimine los elementos duplicados de la lista y devuelva una nueva lista con solo elementos únicos.

lista_1 = [1,2,3,4,5,6,7,8,9,2,5,8,10,11,12,13,14,15,16,17,18,19,11,15,17,18,20]
lista_limpia = []
for i in range(0,len(lista_1)):
    comprovacion = lista_1.count(lista_1[i])
    if comprovacion == 1:
        lista_limpia.append(lista_1[i])

print(lista_limpia)
print('---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/')
# ejercicio 2 original: desarollar un programa que determine si un elemento de una lista es una cadena palindrome, si la cadena existe debe imprimirla y si no existe debe imprimir "no existe"
# variacion del ejersicio 3: Desarrollar un programa que cuente cuántas cadenas palíndromas hay en la lista y las imprima.
lista_con_algunas_str_palindromas = ['arenera','Sajon','Batido','Seres','solos','nagual','macarena','sometemos']
palabras_palindromas = []
contador = 0
for i in range(0,len(lista_con_algunas_str_palindromas)):
    if lista_con_algunas_str_palindromas[i].lower() == lista_con_algunas_str_palindromas[i][::-1].lower():
        contador =contador+1
        palabras_palindromas.append(lista_con_algunas_str_palindromas[i])
print(f'la cantidad de palindomes es de {contador} y son {palabras_palindromas}')
print('---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/')
# ejercicio 3 original: desarrollar un programa que determine si en una lista se encuentra cadena con 2 o mas vocales,si existe debe imprimirla y si no existe debe imprimir "no existe"
# variacion del ejersicio 3: Desarrollar un programa que imprima la primera cadena que contenga 3 o más vocales y detenga la búsqueda.
lista_de_cadenas_con_y_sin_vocales = ['logg ','bird','pack','lago','dora','calcar','papa','Askelad','thorusu','dor']
vocales =['A','E','I','O','U','a','e','i','o','u']
for i in range(0,len(lista_con_algunas_str_palindromas)):
    contador_de_vocales = 0
    for b in range(0,len(vocales)):
        vocal = vocales[b]
        sumatoria_de_vocales = lista_de_cadenas_con_y_sin_vocales[i].count(vocal)
        contador_de_vocales = contador_de_vocales +sumatoria_de_vocales
        if contador_de_vocales >=3:
            print(f'la primeta palabra en tener mas de 3 vocales fue: {lista_de_cadenas_con_y_sin_vocales[i]}')
            break
print('---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/')
# ejercicio 4 original: desarrollar un programa que determine si una lista es palindrome el elemento i es el mismo en la posicion n-1-i
# variacion del ejersicio 4: Desarrollar un programa que determine si una frase completa (como una lista de palabras) es un palíndromo, ignorando espacios y signos de puntuación.
frase = "A man, a plan, a canal, Panama"
frase_filtrada= ''
for i in frase:
    if i.isalpha():
        frase_filtrada = frase_filtrada+i.lower()
if frase_filtrada == frase_filtrada[::-1]:
    print('la frase es un palindrome')
else:
    print('la frase no es un palindrome')
