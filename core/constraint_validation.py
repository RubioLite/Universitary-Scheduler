def validate_constraints(resources, constraints):
    """
    Valida si el conjunto dado de recursos viola alguna restricción.

    :param resources: Lista de IDs de recursos
    :param constraints: Lista de objetos Constraint
    :return: (is_valid, error_message) - True si válido, False y mensaje si inválido
    """
    for constraint in constraints:
        if constraint.type == 'co_requisite':
            # Si se usa algún recurso en la restricción, todos deben usarse
            used = [r for r in constraint.resources if r in resources]
            if used and len(used) != len(constraint.resources):
                return False, f"Violación de Co-requisito: {constraint.description}"
        elif constraint.type == 'mutual_exclusion':
            # No se puede usar más de un recurso de la lista
            used = [r for r in constraint.resources if r in resources]
            if len(used) > 1:
                return False, f"Violación de Exclusión Mutua: {constraint.description}"
    return True, ""