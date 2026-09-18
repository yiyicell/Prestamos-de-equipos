from puertos.notificador_port import NotificadorPort

class NotificadorConsola(NotificadorPort):
    def enviar_notificacion(self, mensaje: str) -> None:
        print(f"[Sistema] {mensaje}")

    def mostrar_reporte_final(self, inventario: dict, solicitudes: list) -> None:
        print("\n--- REPORTE FINAL ---")
        print("Inventario final:")
        for equipo, cantidad in inventario.items():
            print(f"  - {equipo.capitalize()}: {cantidad} unidad(es)")
        
        print("\nSolicitudes procesadas:")
        for req in solicitudes:
            print(f"  - {req.estudiante} solicitó {req.cantidad} {req.equipo}(s): {req.estado}")
        print("---------------------\n")