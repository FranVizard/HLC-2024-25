suma = 0
i=0
numeroFinal = 0 #valor final que indica cuando acaba el bucle, se pide por teclado
numeroFinal = int(input ("¿CUANTOS VALORES QUIERES SUMAR?"))


for i in range(0, numeroFinal*2, 2):  
    print("NUMERO PAR:", end=" ")
    print(i)
    suma = suma + i


print("LA SUMA TOTAL ES:", suma)