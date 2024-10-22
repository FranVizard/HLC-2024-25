"""Crea una programa de Login que compruebe el usuario y contraseña en el diccionario a continuación:
usuarios = 
		{
		"aexposito":
		{"nombre": "Antonio",
		"apellidos": "Expósito",
		"password": "123456"},
	"fgonzalez":
		{"nombre": "Francisco",
		"apellidos": "González",
		"password": "jejejaja"},
	"lcastillo":
		{"nombre: "Lourdes",
		"apellidos": "Castillo",
		"password": "6789"}
	}
	
	El usuario tendrá un máximo de 3 intentos, y al acceder correctamente se mostrará el nombre y apellido del usuario.
		"""
#IMPORTACION DE LIBRERIAS

from os import system

#VARIABLEES

usuarios =		{
		"aexposito":
		    {"nombre": "Antonio",
		    "apellidos": "Expósito",
		    "password": "123456"},
	    "fgonzalez":
		    {"nombre": "Francisco",
		    "apellidos": "González",
		    "password": "jejejaja"},
	    "lcastillo":
		    {"nombre": "Lourdes",
		    "apellidos": "Castillo",
		    "password": "6789"}
	}

print(usuarios["fgonzalez"]["apellidos"])
