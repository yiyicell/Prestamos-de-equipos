# Declaración de Uso de Inteligencia Artificial y Decisiones Arquitectónicas

- **Herramienta utilizada:** Gemini.
- **La usamos para:** Diseñar la estructura base de directorios, definir los contratos (puertos) e implementar la lógica de negocio aislada.
- **Partes apoyadas por IA:** Generación del código fuente en Python puro (sin uso de librerías de terceros), redacción de la justificación técnica y diseño del diagrama de dependencias de seis bloques.
- **Verificaciones realizadas por el equipo:** Ejecución de las pruebas para validar los casos de aceptación exigidos en la matriz, y auditoría del código para garantizar que el núcleo (caso de uso) se mantiene totalmente agnóstico a los detalles de infraestructura.
- **Decisiones arquitectónicas asumidas por el equipo:**
  1. Centralizar la orquestación y la inyección de dependencias de forma exclusiva en el archivo `main.py`.
  2. Implementar los puertos mediante clases abstractas nativas para simular contratos estrictos.
  3. Gestionar la persistencia del inventario mediante diccionarios en memoria (RAM), cumpliendo con el alcance del problema sin depender de bases de datos externas.
