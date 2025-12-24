# Planificador de Eventos Universitario

## Resumen

Esta es una aplicación inteligente de planificación de eventos para gestionar eventos universitarios como clases, seminarios y actividades deportivas. Garantiza que no haya conflictos de recursos y respeta restricciones personalizadas en el uso de recursos, inspirada en sistemas como Indico para la gestión de eventos.

## Dominio

La aplicación modela un entorno universitario donde los eventos (clases, seminarios, deportes) requieren recursos (salas, equipos, personal) y deben adherirse a reglas de programación para prevenir superposiciones y hacer cumplir la compatibilidad.

### Eventos

- **Clases**: Sesiones académicas regulares en aulas.
- **Seminarios**: Conferencias invitadas o talleres que requieren equipos de presentación.
- **Deportes**: Eventos atléticos o prácticas en gimnasios.

### Recursos

- **Salas**: Aulas, auditorios, gimnasios (ej. "Sala A", "Gimnasio 1").
- **Equipos**: Proyectores, micrófonos, equipos deportivos (ej. "Proyector HD", "Conjunto de Micrófonos").
- **Personal**: Profesores, técnicos, entrenadores (ej. "Soporte Técnico", "Entrenador Johnson").

### Restricciones

El sistema implementa dos tipos de restricciones para asegurar una planificación realista y segura:

1. **Co-requisito (Inclusión)**: Los seminarios siempre requieren tanto un proyector como un técnico para una configuración y operación adecuadas.
   - Ejemplo: Usar "Proyector HD" en un seminario requiere también reservar "Soporte Técnico".

2. **Exclusión Mutua**: Ciertos recursos no pueden usarse juntos debido a problemas de compatibilidad.
   - Ejemplo: El "Proyector Avanzado" y el "Sistema de Sonido Antiguo" no pueden reservarse simultáneamente ya que son incompatibles.

## Características

- **Planificar Nuevos Eventos**: Verificar automáticamente la disponibilidad de recursos y violaciones de restricciones antes de programar.
- **Encontrar Espacios Disponibles**: Sugerir el próximo intervalo de tiempo disponible para un evento basado en recursos requeridos y restricciones.
- **Listar Eventos**: Ver todos los eventos programados con sus detalles (horarios, recursos).
- **Eliminar Eventos**: Remover eventos programados, liberando recursos.
- **Ver Horarios de Recursos**: Verificar el horario de reservas para cualquier recurso específico.
- **Persistencia de Datos**: Guardar y cargar todos los datos (eventos, recursos, restricciones) desde un archivo JSON.

## Instalación y Ejecución

1. Asegúrese de que Python 3.x esté instalado en su sistema.
2. Tkinter generalmente se incluye con las instalaciones de Python; si no, instálelo por separado (ej. `sudo apt-get install python3-tk` en Ubuntu).
3. Clone o descargue los archivos del proyecto.
4. Ejecute la aplicación: `python3 main.py`

## Uso

### Menú Principal

- **Listar Eventos**: Abre una ventana que muestra todos los eventos programados con nombres, horarios y recursos.
- **Agregar Evento**: Abre un formulario para crear un nuevo evento.
  - Ingrese nombre del evento, hora de inicio y fin en formato ISO (ej. 2023-10-01T14:00).
  - Seleccione los recursos requeridos de la lista.
  - Haga clic en "Agregar Evento" para programar (valida conflictos y restricciones).
  - Use "Encontrar Próximo Espacio" para auto-completar horarios basados en duración y recursos.
- **Eliminar Evento**: Seleccione un evento de la lista para removerlo.
- **Ver Horario de Recurso**: Ingrese ID de recurso para ver todos los eventos que lo usan.
- **Guardar Datos**: Guarde manualmente el estado actual (automático en operaciones exitosas).

### Manejo de Datos

- Los datos se cargan automáticamente desde `data.json` al inicio.
- Los cambios se guardan automáticamente después de operaciones exitosas.
- Si `data.json` no existe, la aplicación inicia con datos vacíos.

## Datos de Ejemplo

Se proporciona un archivo `data.json` de ejemplo con recursos y restricciones de muestra:

- Recursos: Sala A, Gimnasio 1, Proyector HD, Soporte Técnico, Proyector Avanzado, Sistema de Sonido Antiguo.
- Restricciones: Como se describe arriba.

## Implementación Técnica

- **Lenguaje**: Python 3
- **Interfaz Gráfica**: Tkinter para una interfaz simple y multiplataforma
- **Manejo de Tiempo**: Módulo `datetime` para intervalos y superposiciones
- **Almacenamiento de Datos**: Formato JSON para persistencia
- **Estructura Modular**:
  - `models/`: Carpeta de modelos
    - `event.py`: Clase Event
    - `resource.py`: Clase Resource
    - `constraint.py`: Clase Constraint
    - `models.py`: Importa todas las clases de modelos
  - `core/`: Lógica central
    - `utils.py`: Utilidades de tiempo y análisis
    - `constraint_validation.py`: Lógica de validación de restricciones
    - `scheduler.py`: Planificación de eventos y búsqueda de espacios
    - `persistence.py`: Funcionalidad de guardar/cargar
  - `interface/`: Interfaz de usuario
    - `main_gui.py`: Clase principal de la interfaz de usuario
    - `list_events.py`: Ventana de lista de eventos
    - `add_event.py`: Ventana de agregar evento
    - `edit_event.py`: Ventana de editar evento
    - `delete_event.py`: Ventana de eliminar evento
    - `view_schedule.py`: Ventana de ver horario de recurso
  - `data/`: Datos persistentes
    - `data.json`: Archivo de datos
  - `main.py`: Script de punto de entrada

## Manejo de Errores

La aplicación proporciona mensajes de error claros para:

- Formatos de fecha/hora inválidos
- Conflictos de recursos
- Violaciones de restricciones
- Entradas faltantes
- Problemas de carga de archivos

## Licencia

Este proyecto es para fines educativos y académicos.

## NOTAS

Si eres estudiante y estás viendo esto, siéntete libre de tomar ideas si es que lo ves necesario pero por favor, no copies directamente, sé creativo y haz las cosas por ti mismo.
