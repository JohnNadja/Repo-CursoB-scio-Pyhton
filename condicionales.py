# Declaramos una variable 
from ctypes import BigEndianStructure


calificacion = (float(input("Intoduce tu calificación de AZ-900: ")))

mal = "Que mal, inténtalo a la próxima vez"
perfecto = "Felicidades" 
maximo= "no puedes obtener más de 1000"
minimo= 0
# Se pregunta si la calificación en mayor a 700
if (calificacion > 700):
    print(perfecto)
elif (calificacion > 1000):
    print(maximo)
else:
    print(mal)
    
    
edad = (int(input("Cuál es tu edad: ")))

if (edad >= 18 and edad <=115):
    print("Bienvenido, usuario")
elif(edad > 115):
    print("Si vienes acompañado con tus abuelos, podemos fiar")
elif (edad < minimo):
    print("No es posible que seas viajer@ en el tiempo")
else:
    print("No se puede entrar aquí")
