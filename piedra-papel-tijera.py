

nombre1 = input("Ingrese su nombre Jugador 1: ")
nombre2 = input("Ingrese su nombre Jugador 2: ")

contador_jugador1 = 0
contador_jugador2 = 0

while contador_jugador1 <3 and contador_jugador2 < 3 :

    jugador1 = input(nombre1 +" Elija y escriba la opcion (piedra, papel ó tijera): ")
    jugador2 = input(nombre2 +" Elija y escriba la opcion (piedra, papel ó tijera): ")

    opcion1 = jugador1.lower() == "piedra" and jugador2.lower() == "tijera"
    opcion2 = jugador1.lower() == "tijera" and jugador2.lower() == "papel"
    opcion3 = jugador1.lower() == "papel" and jugador2.lower() == "piedra"

    empate = jugador1.lower() == jugador2.lower()

    if (empate):
        print("Es un empate")

    elif (opcion1 or opcion2 or opcion3):
        contador_jugador1 += 1
        print("Felicidades " + nombre1 + " ganaste esta partida")
        print("Tienes: " + str(contador_jugador1) + " puntos")
    else:
        contador_jugador2 += 1
        print("Felicidades " + nombre2 + " ganaste ganaste esta partida")
        print("Tienes: " + str(contador_jugador2) + " puntos")
        
if(contador_jugador1 == 3):
    print(nombre1 + " ganaste el juego")
else:
    print(nombre2 + " ganaste el juego")
    