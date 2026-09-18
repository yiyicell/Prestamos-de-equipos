from abc import ABC, abstractmethod
from nucleo.modelo import Solicitud

class InventarioPort(ABC):
    @abstractmethod
    def obtener_cantidad(self, equipo: str) -> int:
        pass

    @abstractmethod
    def restar_cantidad(self, equipo: str, cantidad: int) -> None:
        pass

    @abstractmethod
    def registrar_solicitud(self, solicitud: Solicitud) -> None:
        pass

    @abstractmethod
    def obtener_todo_inventario(self) -> dict:
        pass

    @abstractmethod
    def obtener_todas_solicitudes(self) -> list:
        pass