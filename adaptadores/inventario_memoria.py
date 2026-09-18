from puertos.inventario_port import InventarioPort
from nucleo.modelo import Solicitud

class InventarioMemoria(InventarioPort):
    def __init__(self):
        # Datos iniciales requeridos
        self.inventario = {
            "portátil": 2,
            "tableta": 1
        }
        self.solicitudes = []

    def obtener_cantidad(self, equipo: str) -> int:
        return self.inventario.get(equipo, 0)

    def restar_cantidad(self, equipo: str, cantidad: int) -> None:
        if equipo in self.inventario:
            self.inventario[equipo] -= cantidad

    def registrar_solicitud(self, solicitud: Solicitud) -> None:
        self.solicitudes.append(solicitud)

    def obtener_todo_inventario(self) -> dict:
        return self.inventario.copy()

    def obtener_todas_solicitudes(self) -> list:
        return self.solicitudes.copy()