"""3e Realiza un programa que pida por teclado una serie de asignaturas, con su calificación correspondiente, hasta que introduzca una asignatura en blanco. 
Posteriormente nos debe mostrar por pantalla la lista de las que están aprobadas 
(calificación mayor o igual que 5), con su correspondiente nota y la media aritmética de todas las calificaciones (se incluirán también las notas suspensas en la media).py"""

#IMPORTACION DE LIBRERIAS

from os import system

#VARIABLEES

asignatura=" " #CONTENDRA EL NOMBRE DE LA ASIGNATURA (TIPO CADENA)
calificacion=0 #NOTA DE LA ASIGNATURA (TIPO FLOAT)
lista=[] #LISTA CON [NOMBRE DE LA ASIGNATURA, CALIFICACION DE LA ASIGNATURA]
sumacalificaciones=0 #suma de las notas para hacer la media aritmetica

#PROGRAMA PRINCIPAL

system("cls")
while(asignatura != ""):
    asignatura = input("INTRODUCE EL NOMBRE DE LA ASIGNATURA (ENTER PARA FINALIZAR):")
    if asignatura !="":
        calificacion = float(input("TECLEA SU CALIFICACION: "))
    lista.append([asignatura, calificacion])
    print("") #HAGO UN SALTO DE LINEA

for asignatura, calificacion in lista:
    if calificacion >=5:
        print (f"LA ASIGNATURA {asignatura} ESTA APROBADA CON UN {calificacion}")
    sumacalificaciones =sumacalificaciones + calificacion

print(f"LA MEDIA ARITMETICA DE LAS CALIFICACIONES ES {sumacalificaciones/len(lista)}")


