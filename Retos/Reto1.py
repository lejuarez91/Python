'''
 Escribe un programa que muestre por consola (con un print) los
 números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

for i in range(1,101):

    multiplo_tres = i % 3
    multiplo_cinco = i % 5

    if multiplo_tres == 0 and multiplo_cinco == 0:
        print('fizzbuzz')
    elif multiplo_tres == 0:
        print('fizz')
    elif multiplo_cinco == 0:
        print('buzz')
    else:
        print(i)
        