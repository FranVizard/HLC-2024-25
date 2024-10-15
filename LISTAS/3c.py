"""PROGRAMA QUE 	Introduciremos por teclado una matriz de 2 x 2, y nos devolverá el valor de su determinante.
"""

#DECLARACION DE VARIABLE


fila=0 #RECORRE EL NUMERO DE FILAS DE LA MATRIZ
col=0   #RECORRE EL NUMERO DE COLUMNAS DE LA MATRIZ
matriz=[[0,0],[0,0]]
determinante=0

#PROGRAMA PRINCIPAL
for fila in range(0,2): #BUCLE QUE RECORRE LAS FILAS
    for col in range(0,2): #BUCLE QUE RECORRE LAS COLUMNAS
        matriz[fila][col]= int(input(f"INTRODUCE EL ELEMENTO ({fila},{col} DE LA MATRIZ: )"))


determinante=matriz[0][0]*matriz[1][1]-matriz[1][0]*matriz[0][1]

print(f"EL DETERMINANTE DE LA MATRIZ ES {determinante}")


