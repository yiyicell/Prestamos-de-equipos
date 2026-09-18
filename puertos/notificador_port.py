from abc import ABC, abstractmethod

class NotificadorPort(ABC):
    @abstractmethod
    def enviar_notificacion(self, mensaje: str) -> None:
        pass
        
    @abstractmethod
    def mostrar_reporte_final(self, inventario: dict, solicitudes: list) -> None:
        pass