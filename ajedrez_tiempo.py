# Inicialización de variables
tiempo_carlsen = tiempo_nakamura = 180
tiempo_movimiento = 10
turno_actual = "Carlsen"

# Bucle principal del juego
while tiempo_carlsen > 0 and tiempo_nakamura > 0:
    print(f"Tiempo de Carlsen: {tiempo_carlsen} segundos")
    print(f"Tiempo de Nakamura: {tiempo_nakamura} segundos")
    print(f"Turno de {turno_actual}")

    movimiento = input("Ingrese 'Carlsen', 'Hikaru' o 'Salir' para terminar: ")

    if movimiento.lower() == "salir":
        break

    tiempo_movimiento_actual = tiempo_movimiento if tiempo_carlsen > 60 and tiempo_nakamura > 60 else 5

    if movimiento.lower() == turno_actual.lower():
        tiempo_carlsen -= tiempo_movimiento_actual if turno_actual == "Carlsen" else 0
        tiempo_nakamura -= tiempo_movimiento_actual if turno_actual == "Nakamura" else 0
        turno_actual = "Nakamura" if turno_actual == "Carlsen" else "Carlsen"
    else:
        print("Movimiento no válido. Inténtalo de nuevo.")

# Fin del juego
print("¡La partida ha finalizado!")

# Determina el ganador o si fue un empate
if tiempo_carlsen < tiempo_nakamura:
    print("¡Magnus Carlsen ha ganado!")
elif tiempo_nakamura < tiempo_carlsen:
    print("¡Hikaru Nakamura ha ganado!")
else:
    print("¡Es un empate!")

