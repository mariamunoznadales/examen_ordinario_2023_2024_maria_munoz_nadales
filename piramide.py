'''Escribe un programa en Python que solicite al usuario un número entero n y 
luego genere una pirámide de asteriscos con n niveles. La pirámide debe ser centrada y consistir en niveles de asteriscos, 
comenzando con 1 asterisco en el nivel superior y aumentando en 2 asteriscos por nivel. 
Asegúrate de que el programa valide que el número ingresado por el usuario sea mayor o igual a 1 antes de continuar.
'''

def piramide():
    print("Bienvenido al generador de pirámides.")
    print("Ingrese un número y se creará una pirámide de ese nivel ")
    nivel = int(input("Número : ")) #El usuario introduce el número de niveles

    if nivel < 1 : 
        print("No es un nivel válido")
    else:
          for i in range(1, nivel + 1, 2):    #Iterar según el número que introduzca el usuario
            espacios = " " * ((nivel - i) // 2)  #Para centrar la prirámide
            asteriscos = "*" * i
            print(espacios + asteriscos) 

piramide()