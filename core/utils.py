from datetime import datetime, timedelta

def intervals_overlap(start1, end1, start2, end2):
    """
    Verifica si dos intervalos de tiempo se superponen.

    :param start1: Inicio del primer intervalo (datetime)
    :param end1: Fin del primer intervalo (datetime)
    :param start2: Inicio del segundo intervalo (datetime)
    :param end2: Fin del segundo intervalo (datetime)
    :return: True si se superponen, False en caso contrario
    """
    return start1 < end2 and start2 < end1

def is_resource_available(resource_id, start, end, events):
    """
    Verifica si un recurso está disponible durante el intervalo de tiempo dado.

    :param resource_id: ID del recurso
    :param start: Fecha y hora de inicio
    :param end: Fecha y hora de fin
    :param events: Lista de objetos Event
    :return: True si disponible, False si hay conflicto
    """
    for event in events:
        if resource_id in event.resources and intervals_overlap(event.start_time, event.end_time, start, end):
            return False
    return True

def parse_datetime(date_str):
    """
    Analiza una cadena de fecha y hora en formato ISO.

    :param date_str: Cadena como '2023-10-01T10:00:00'
    :return: Objeto datetime
    """
    try:
        return datetime.fromisoformat(date_str)
    except ValueError:
        raise ValueError(f"Formato de fecha y hora inválido: {date_str}. Use formato ISO como '2023-10-01T10:00:00'")

def format_datetime(dt):
    """
    Format datetime to ISO string.

    :param dt: Objeto de fecha y hora
    :return: Cadena con formato ISO
    """
    return dt.isoformat()