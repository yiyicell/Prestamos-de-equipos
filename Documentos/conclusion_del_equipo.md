Elegimos esta estructura porque la preocupación principal era aislar completamente las reglas de negocio de los detalles tecnológicos, garantizando que el sistema (el núcleo) tuviera alta independencia y pudiera escalar en el futuro sin riesgo de romper la lógica de los préstamos.

A cambio, asumimos una mayor complejidad inicial en el diseño, la necesidad de crear múltiples archivos y carpetas para separar responsabilidades, y la carga técnica de gestionar manualmente la inyección de dependencias a través de puertos abstractos.
