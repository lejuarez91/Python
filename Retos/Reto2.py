'''
 Escribe una función que reciba dos palabras (String) y retorne
 verdadero o falso (Bool) según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS
   las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama.
'''

# Solución 1
def anagrama(palabra1, palabra2):
    if(palabra1 == palabra2):
        return False
    if(len(palabra1) != len(palabra2)):
        return False
    
    letras_palabra1 = list(palabra1)
    letras_palabra2 = list(palabra2)

    for i in range(0,len(palabra1)):
       letra = letras_palabra1[i]
       index = 0

       try:
           index = letras_palabra2.index(letra)
           letras_palabra2[index] = ""
       except:
           return False

    anagrama = ""

    for i in range(0,len(letras_palabra2)):
        anagrama = anagrama + letras_palabra2[i]

    if(len(anagrama) == 0):
        return True
    else:
        return False

## Ejecuta la función
res = anagrama("amor", "roma")
print(res)


# Solución 2
def anagrama2(palabra1, palabra2):
    if palabra1 == palabra2:
        return False
    if len(palabra1) != len(palabra2):
        return False
    
    palabra2_copy = list(palabra2)

    for letra in palabra1:
       try:
           palabra2_copy.remove(letra)
       except ValueError:
           return False

    return sorted(palabra1) == sorted(palabra2)

## Ejecuta la función
res = anagrama2("amor", "roma")
print(res)
