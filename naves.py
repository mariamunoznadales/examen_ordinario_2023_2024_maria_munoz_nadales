from EstrellaDeLaMuerte import EstrellaDeLaMuerte

class NavePequena(EstrellaDeLaMuerte):
    def __init__(self, nombre, puntos):
        super().__init__()
        self.nombre = nombre
        self.puntos = puntos

class NaveGrande(EstrellaDeLaMuerte):
    def __init__(self, nombre, puntos):
        super().__init__()
        self.nombre = nombre
        self.puntos = puntos

