from unittest import TestCase, TestLoader, TextTestRunner
from back_end import Programadito

class TestearJuego(TestCase):
    
    def setUp(self):
        self.juego = Programadito()
        
    def test_nombres_vacios(self):
        self.assertEqual(self.juego.nombre_jugador_1, "")
        self.assertEqual(self.juego.nombre_jugador_2, "")

    def test_tablero_inicial(self):
        self.assertTrue(self.juego.turno_primero)
        self.assertIsNone(self.juego.carta_contada)
        self.assertIsNone(self.juego.carta_tirada)
        self.assertEqual(len(self.juego.cartas_pozo), 0)
        self.assertEqual(len(self.juego.mazo_jugador_1), 52)
        self.assertEqual(len(self.juego.mazo_jugador_2), 52)
        
    def test_validacion_de_nombres(self):
        self.juego.ingresar_nombres("", "")
        self.assertEqual(self.juego.nombre_jugador_1, "")
        self.assertEqual(self.juego.nombre_jugador_2, "")
        self.juego.ingresar_nombres("Juan", "Juan")
        self.assertEqual(self.juego.nombre_jugador_1, "")
        self.assertEqual(self.juego.nombre_jugador_2, "")
        self.juego.ingresar_nombres("Juan 1", "Pedro")
        self.assertEqual(self.juego.nombre_jugador_1, "")
        self.assertEqual(self.juego.nombre_jugador_2, "")
        self.juego.ingresar_nombres("Juan", "Pedro")
        self.assertEqual(self.juego.nombre_jugador_1, "Juan")
        self.assertEqual(self.juego.nombre_jugador_2, "Pedro")

    def test_tirar_cartas(self):
        self.juego.comenzar_juego()
        
        for _ in range(52):
            self.assertTrue(self.juego.turno_primero)
            self.juego.tirar_carta(1)
            self.assertFalse(self.juego.turno_primero)
            self.juego.tirar_carta(2)

        self.assertEqual(len(self.juego.cartas_pozo), 103)
        self.assertEqual(len(self.juego.mazo_jugador_1), 0)
        self.assertEqual(len(self.juego.mazo_jugador_2), 1)
        

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(TestearJuego)
    TextTestRunner().run(suite)