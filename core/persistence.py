import json
from models import Event, Resource, Constraint

def save_data(events, resources, constraints, filename='data/data.json'):
    """
    Guarda el estado actual en un archivo JSON.

    :param events: Lista de objetos Event
    :param resources: Lista de objetos Resource
    :param constraints: Lista de objetos Constraint
    :param filename: Archivo donde guardar
    """
    data = {
        'events': [event.to_dict() for event in events],
        'resources': [resource.to_dict() for resource in resources],
        'constraints': [constraint.to_dict() for constraint in constraints]
    }
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_data(filename='data/data.json'):
    """
    Carga datos desde un archivo JSON.

    :param filename: Archivo desde donde cargar
    :return: listas (events, resources, constraints)
    """
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        events = [Event.from_dict(item) for item in data.get('events', [])]
        resources = [Resource.from_dict(item) for item in data.get('resources', [])]
        constraints = [Constraint.from_dict(item) for item in data.get('constraints', [])]
        return events, resources, constraints
    except FileNotFoundError:
        # Devolver listas vacías si el archivo no existe
        return [], [], []
    except json.JSONDecodeError:
        raise ValueError(f"JSON inválido en {filename}")