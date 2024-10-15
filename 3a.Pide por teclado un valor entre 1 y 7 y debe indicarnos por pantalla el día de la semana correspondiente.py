"""(USO DE LISTAS) PEDIRA POR TECLADO LA LISTA DE LOS NUMEROS DE LA LOTERIA DE LOS ULTIMOS 7 DIAS. POSTERIORMENTE LOS MOSTRARA ORDENADOS DE MENOR A MAYOR Y DE MAYOR A MENOR"""

#declaracion de variables

numerosLoteria = [0, 0, 0, 0, 0, 0, 0]

for contador in range(0,7):
    numerosLoteria[contador] = int(input(f"INTRODUCE EL DIA DE LA LOTERIA DEL {contador+1}º dia: "))

numerosLoteria.sort() # ORDENAR LA LISTA DE MENOR A MAYOR

print(numerosLoteria)

numerosLoteria.sort(reverse = True) #ORDENAR LA LISTA DE MAYOR A MENOR

print(numerosLoteria)

""" (numerosLoteria).append("LO QUE QUIERO AÑADIR") #AÑADE UNN ELEMNETO DE LA LISTA
    (numerosLoteria).remove("LO QUE QUIERO AÑADIR") #BORRA UN ELEMENTO DE LA LISTA """