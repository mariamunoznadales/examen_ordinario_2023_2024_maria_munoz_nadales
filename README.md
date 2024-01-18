# EJERCICIO 3 Y 4 : Estrella de la Muerte vs. Planetas, Naves Aliadas vs. Estrella de la Muerte
## ¿Para qué sirve cada archivo.py?
Planetas.py:
Archivo que contiene las clases relacionadas con los planetas.
Clase base Planeta con atributos nombre, volumen, y clasificacion.
Subclases para tres planetas específicos: Concordia, Ilum y Kamino.

EstrellaDeLaMuerte.py:
Archivo que contiene la clase EstrellaDeLaMuerte.
Clase con un atributo para los puntos de vida (1000) y un método destruir_planeta que determina si puede destruir un planeta.

Uso en main.py:
Crear instancias de la Estrella de la Muerte y varios planetas.
Llamar al método destruir_planeta para cada planeta y mostrar mensajes correspondientes.

Naves.py:
Archivo que contiene las clases relacionadas con las naves.
Subclases NavePequena y NaveGrande heredando de EstrellaDeLaMuerte.
Cada subclase tiene su propio constructor para inicializar nombre y puntos de vida.

EstrellaDeLaMuerte.py:
Modificación para interactuar con naves aliadas.
Métodos para atacar naves aliadas y verificar si pueden ser destruidas.

main.py:
Crear instancias de la Estrella de la Muerte, una NavePequena y una NaveGrande.
Llamar a los métodos correspondientes para simular el ataque y mostrar mensajes en la terminal.
