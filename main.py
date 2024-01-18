
from EstrellaDeLaMuerte import EstrellaDeLaMuerte
from naves import NavePequena, NaveGrande

# Crear instancias de la Estrella de la Muerte, NavePequena y NaveGrande
estrella_de_la_muerte = EstrellaDeLaMuerte()
nave_pequena = NavePequena("Nave Pequeña 1", 200)
nave_grande = NaveGrande("Nave Grande 1", 800)

# Llamar a los métodos correspondientes para que la Estrella de la Muerte ataque a sus naves aliadas
estrella_de_la_muerte.atacar_nave_aliada(nave_pequena)
estrella_de_la_muerte.atacar_nave_aliada(nave_grande)
