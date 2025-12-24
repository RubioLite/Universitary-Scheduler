from datetime import datetime

class Event:
    def __init__(self, name, start_time, end_time, resources):
        """
        Representa un evento en el sistema de gestión de eventos universitarios.

        :param name: Nombre del evento (ej. "Seminario de Matemáticas")
        :param start_time: Fecha y hora de inicio del evento
        :param end_time: Fecha y hora de fin del evento
        :param resources: Lista de IDs de recursos requeridos para el evento
        """
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.resources = resources  # list of str (resource IDs)

    def to_dict(self):
        return {
            'name': self.name,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'resources': self.resources
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['name'],
            datetime.fromisoformat(data['start_time']),
            datetime.fromisoformat(data['end_time']),
            data['resources']
        )