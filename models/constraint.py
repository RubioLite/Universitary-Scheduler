class Constraint:
    def __init__(self, type, resources, description):
        """
        Representa una restricción en el uso de recursos.

        :param type: 'co_requisite' o 'mutual_exclusion'
        :param resources: Lista de IDs de recursos involucrados en la restricción
        :param description: Descripción legible por humanos de la restricción
        """
        self.type = type
        self.resources = resources
        self.description = description

    def to_dict(self):
        return {
            'type': self.type,
            'resources': self.resources,
            'description': self.description
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['type'], data['resources'], data['description'])