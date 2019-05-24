from back_end import Programadito

class TestJuego:

    def __init__(self, juego):
        self.juego = juego

    def revisar_nombres_vacios(self):
        if self.juego.nombre_jugador_1 != "" \
                or self.juego.nombre_jugador_2 != "":
            raise ValueError("Nombre de ambos jugadores comienza vacio")

    def revisar_nombres(self, nombre_1, nombre_2):
        if self.juego.nombre_jugador_1 != nombre_1 \
                or self.juego.nombre_jugador_2 != nombre_2:
            raise ValueError("Nombres incorrectamente asignados")

    def revisar_tablero_inicial(self):
        if not self.juego.turno_primero:
            raise ValueError("Siempre comienza el primer jugador")
        if self.juego.carta_contada is not None \
                or self.juego.carta_tirada is not None:
            raise ValueError("Aún no se juegan o cuentan cartas")
        if len(self.juego.cartas_pozo) != 0:
            raise ValueError("Pozo de cartas debe comenzar vacio")
        if len(self.juego.mazo_jugador_1) != 52 \
                or len(self.juego.mazo_jugador_2) != 52:
            raise ValueError("Mazos de jugadores comienzan con 52 cartas")

    def revisar_juego_no_iniciado(self):
        if self.juego.juego_comenzo:
            raise ValueError("Juego no ha comenzado aún")
    
    def revisar_juego_iniciado(self):
        if not self.juego.juego_comenzo:
            raise ValueError("Juego ya debió comenzar")

    def revisar_turno(self, n_jugador):
        if n_jugador == 1 and not self.juego.turno_primero:
            raise ValueError("No es el turno del primer jugador")
        if n_jugador == 2 and self.juego.turno_primero:
            raise ValueError("No es el turno del segundo jugador")

    def revisar_mazos(self, pozo, mazo_1, mazo_2):
        if len(self.juego.cartas_pozo) != pozo:
            raise ValueError(f"No hay {mazo_1} cartas en el pozo.")
        if len(self.juego.mazo_jugador_1) != mazo_1:
            raise ValueError(f"No hay {mazo_1} cartas en el primer mazo.")
        if len(self.juego.mazo_jugador_2) != mazo_2:
            raise ValueError(f"No hay {mazo_2} cartas en el segundo mazo.")


if __name__ == "__main__":

    juego = Programadito()
    test = TestJuego(juego)

    # Revisar estado inicial de juego es correcto:
    test.revisar_nombres_vacios()
    test.revisar_tablero_inicial()
    test.revisar_juego_no_iniciado()

    # # Revisar que no ocurra nada cuando se tira una carta sin comenzar a jugar:
    # juego.tirar_carta(1)
    # juego.tirar_carta(2)
    # test.revisar_tablero_inicial()

    # # Revisar validación de nombres:
    # juego.ingresar_nombres("", "")
    # test.revisar_nombres_vacios()
    # juego.ingresar_nombres("Juan", "Juan")
    # test.revisar_nombres_vacios()
    # juego.ingresar_nombres("Juan 1", "Pedro")
    # test.revisar_nombres_vacios()
    # juego.ingresar_nombres("Juan", "Pedro")
    # test.revisar_nombres("Juan", "Pedro")

    # # Revisar si cambia estado al comenzar juego:
    # juego.comenzar_juego()
    # test.revisar_juego_iniciado()

    # # Revisar que no puede comenzar segundo jugador
    # juego.tirar_carta(2)
    # test.revisar_tablero_inicial()

    # juego.tirar_carta(1)
    # test.revisar_turno(2)
    # test.revisar_mazos(1, 51, 52)

    # juego.tirar_carta(2)
    # test.revisar_turno(1)
    # test.revisar_mazos(2, 51, 51)


