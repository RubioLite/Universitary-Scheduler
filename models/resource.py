class Resource:
    def __init__(self, id, name, attributes=None):
        """
        Representa un recurso en el sistema.

        :param id: Identificador único para el recurso
        :param name: Nombre del recurso (ej. "Sala de Conferencias A")
        :param attributes: Dict de atributos adicionales (ej. {'type': 'room', 'capacity': 100})
        """
        self.id = id
        self.name = name
        self.attributes = attributes or {}

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'attributes': self.attributes
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['id'], data['name'], data.get('attributes', {}))