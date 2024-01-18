from planetas import Planeta, Concordia, Ilum, Kamino

class EstrellaDeLaMuerte:
    
    def __init__(self):
        self.puntos = 1000

    def destruir_planeta(self, planeta):
        if planeta.clasificacion <= self.puntos:
            print(f"La Estrella de la Muerte ha destruido {planeta.nombre}.")
            self.puntos -= planeta.clasificacion
        else:
            print(f"La Estrella de la muerte no puede destruir {planeta.nombre}, no tiene suficientes puntos de vida.")

    def atacar_nave_aliada(self, nave_aliada):
        if nave_aliada.puntos_de_vida <= self.puntos_de_vida:
                print(f"La Estrella de la Muerte ha destruido la nave aliada {nave_aliada.nombre}.")
                self.puntos_de_vida -= nave_aliada.puntos_de_vida
        else:
                print(f"No se puede destruir la nave aliada {nave_aliada.nombre}. La Estrella de la Muerte no tiene suficientes puntos de vida.")

concordia = Concordia()
ilum = Ilum()
kamino = Kamino()

estrella_de_la_muerte = EstrellaDeLaMuerte()

estrella_de_la_muerte.destruir_planeta(concordia)
estrella_de_la_muerte.destruir_planeta(ilum)
estrella_de_la_muerte.destruir_planeta(kamino)