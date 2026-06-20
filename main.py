"""
PROYECTO AUTÓNOMO 2: LÓGICA DE PROGRAMACIÓN
PROGRAMA: JUEGO DEL AHORCADO (ARQUITECTURA MODULAR MVC)
"""

import os
import random


class AhorcadoModelo:
    """CAPA DE DATOS (MODELO): Gestiona las palabras y el estado de la sesión."""

    DEF_WORDS = ["ARTIFICIAL", "INGENIERIA", "LOGICA", "PROGRAMACION", "CODIGO"]

    def __init__(self):
        self.palabra_secreta = random.choice(self.DEF_WORDS).upper()
        self.letras_unicas = set(self.palabra_secreta)
        self.letras_intentadas = set()
        self.intentos_restantes = 6

    def registrar_intento(self, letra: str) -> bool:
        self.letras_intentadas.add(letra)
        if letra in self.letras_unicas:
            return True
        self.intentos_restantes -= 1
        return False

    @property
    def palabra_enmascarada(self) -> str:
        return " ".join(
            [
                letra if letra in self.letras_intentadas else "_"
                for letra in self.palabra_secreta
            ]
        )

    def ha_ganado(self) -> bool:
        return self.letras_unicas.issubset(self.letras_intentadas)

    def ha_perdido(self) -> bool:
        return self.intentos_restantes <= 0


class AhorcadoVista:
    """CAPA DE PRESENTACIÓN (VISTA): Maneja la salida gráfica por consola CLI."""

    MONOS = {
        6: "\n  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
        5: "\n  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        4: "\n  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        3: "\n  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
        2: "\n  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
        1: "\n  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
        0: "\n  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",
    }

    @staticmethod
    def limpiar_pantalla():
        os.system("cls" if os.name == "nt" else "clear")

    @classmethod
    def renderizar_juego(cls, modelo: AhorcadoModelo, mensaje: str = ""):
        cls.limpiar_pantalla()
        print("=== JUEGO DEL AHORCADO (INGENIERÍA DE SOFTWARE) ===")
        print(cls.MONOS[modelo.intentos_restantes])
        print(f"\nPalabra actual:  {modelo.palabra_enmascarada}")
        print(f"Intentos restantes: {modelo.intentos_restantes}")
        print(
            f"Letras utilizadas:  {', '.join(sorted(modelo.letras_intentadas))}"
        )
        if mensaje:
            print(f"\n[Aviso]: {mensaje}")


class AhorcadoControlador:
    """CAPA DE LÓGICA (CONTROLADOR): Orquesta el flujo de control y las reglas."""

    def __init__(self):
        self.modelo = AhorcadoModelo()
        self.vista = AhorcadoVista()

    def solicitar_letra_valida(self) -> str:
        while True:
            entrada = input("\nIntroduce una letra: ").strip().upper()
            if len(entrada) != 1 or not entrada.isalpha():
                self.vista.renderizar_juego(
                    self.modelo, "Error: Inserta un único carácter alfabético."
                )
            elif entrada in self.modelo.letras_intentadas:
                self.vista.renderizar_juego(
                    self.modelo, f"Ya has intentado la letra '{entrada}'."
                )
            else:
                return entrada

    def ejecutar_partida(self):
        while not self.modelo.ha_ganado() and not self.modelo.ha_perdido():
            self.vista.renderizar_juego(self.modelo)
            letra_valida = self.solicitar_letra_valida()
            self.modelo.registrar_intento(letra_valida)

        self.vista.limpiar_pantalla()
        if self.modelo.ha_ganado():
            print("¡Felicidades! Has ganado la partida de forma lógica. 🎉")
            print(f"La palabra secreta era: {self.modelo.palabra_secreta}")
        else:
            print(self.vista.MONOS[0])
            print("GAME OVER. Has sido ahorcado. 💀")
            print(f"La palabra correcta era: {self.modelo.palabra_secreta}")


if __name__ == "__main__":
    juego = AhorcadoControlador()
    juego.ejecutar_partida()
