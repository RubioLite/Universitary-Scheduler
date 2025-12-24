from datetime import datetime, timedelta
from models import Event
from .utils import is_resource_available
from .constraint_validation import validate_constraints

def plan_event(name, start, end, resources, events, constraints):
    """
    Intenta planificar un nuevo evento.

    :param name: Nombre del evento
    :param start: Fecha y hora de inicio
    :param end: Fecha y hora de fin
    :param resources: Lista de IDs de recursos
    :param events: Lista de objetos Event existentes
    :param constraints: Lista de objetos Constraint
    :return: (success, message)
    """
    # Verificar disponibilidad de recursos
    for res in resources:
        if not is_resource_available(res, start, end, events):
            return False, f"El recurso '{res}' no está disponible durante el tiempo especificado."

    # Verificar restricciones
    valid, msg = validate_constraints(resources, constraints)
    if not valid:
        return False, msg

    # Crear y agregar evento
    event = Event(name, start, end, resources)
    events.append(event)
    return True, "Evento planificado exitosamente."

def find_next_slot(duration, resources, events, constraints, start_from=None):
    """
    Encuentra el próximo espacio de tiempo disponible para un evento con duración y recursos dados.

    :param duration: timedelta para la duración del evento
    :param resources: Lista de IDs de recursos
    :param events: Lista de objetos Event existentes
    :param constraints: Lista de objetos Constraint
    :param start_from: datetime desde donde comenzar la búsqueda, por defecto ahora
    :return: (suggested_start, suggested_end) o (None, None) si no se encuentra espacio en tiempo razonable
    """
    if start_from is None:
        start_from = datetime.now()

    current = start_from
    max_search_days = 30  # Limitar búsqueda para evitar bucle infinito
    end_search = current + timedelta(days=max_search_days)

    while current < end_search:
        proposed_end = current + duration

        # Verificar disponibilidad de recursos
        conflict = False
        for res in resources:
            if not is_resource_available(res, current, proposed_end, events):
                conflict = True
                break

        if not conflict:
            # Verificar restricciones
            valid, _ = validate_constraints(resources, constraints)
            if valid:
                return current, proposed_end

        # Mover a la próxima hora
        current += timedelta(hours=1)

    return None, None  # No se encontró espacio