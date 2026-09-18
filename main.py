from adaptadores.inventario_memoria import InventarioMemoria
from adaptadores.consola import NotificadorConsola
from nucleo.servicio_prestamos import ServicioPrestamos

def ejecutar_pruebas_aceptacion():
    # 1. Instanciación de adaptadores
    repo_memoria = InventarioMemoria()
    notificador_ui = NotificadorConsola()
    
    # 2. Inyección al núcleo
    servicio = ServicioPrestamos(repo_memoria, notificador_ui)
    
    print("--- INICIANDO PRUEBAS DE ACEPTACIÓN ---")
    
    # Caso 1: Inventario inicial
    print("\n[Caso: Inventario inicial]")
    servicio.mostrar_inventario_inicial()
    
    # Caso 2: Solicitud aprobada
    print("\n[Caso: Solicitud aprobada]")
    servicio.procesar_solicitud(estudiante="Ana", equipo="portátil", cantidad=1)
    
    # Caso 3: Solicitud rechazada
    print("\n[Caso: Solicitud rechazada]")
    servicio.procesar_solicitud(estudiante="Juan", equipo="tableta", cantidad=2)
    
    # Caso 4: Reporte final
    print("\n[Caso: Reporte final]")
    servicio.generar_reporte_final()

if __name__ == "__main__":
    ejecutar_pruebas_aceptacion()