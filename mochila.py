from itertools import combinations

'''
Se penso en separar la lista en 2 y realizar distintas combinaciones para buscar los valores que correspondieran a un valor mas alto, sin
exceder la capacidad de la mochila, pero a la hora de llevarlo a cabo se encontro que habian complicaciones para realizar eso,
hubiera sido mejor trabajar con diccionarios, en donde la key fuera el peso, y hacer la combinacion para aquellas que no superen la
capacidad de la mochila, pero por tiempo no se modifico para trabajar de la ultima manera
'''

def  AlistarMochila(elementos=[(2, 3), (3, 4), (4, 5), (5, 6),(1,9)], capacidadMochila = 10):
    pesoElementos = []
    valorElementos = []

    for elemento in elementos:
        peso, valor = elemento
        pesoElementos.append(peso)
        valorElementos.append(valor)
    

    combinaciones = []
    for i in combinations(pesoElementos,3):
            if sum(i) == capacidadMochila:
                combinaciones.append(i)
                
    print (combinaciones)

AlistarMochila()