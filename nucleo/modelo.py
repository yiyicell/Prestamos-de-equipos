class Solicitud:
    def __init__(self, estudiante: str, equipo: str, cantidad: int):
        self.estudiante = estudiante
        self.equipo = equipo
        self.cantidad = cantidad
        self.estado = "Pendiente"