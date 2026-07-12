from maritime_service import (
    get_all_vessels,
    get_all_ports,
    get_active_voyages,
    get_all_cargo,
    get_vessels_by_type,
    get_all_voyages,
    list_vessel_types,
    voyage_report,
    get_voyages_from_port,
    update_voyage_status,
    delete_voyage,
    create_voyage_with_cargo
)
ROUTES = {
    "show vessels": get_all_vessels,
    "show ports": get_all_ports,
    "show cargo": get_all_cargo,
    "show active voyages": get_active_voyages,
    #"show vessels by type": get_vessels_by_type,  Cant include since it contain parameter
    "show all voyages": get_all_voyages,
    #"show vessels of container": get_vessels_by_type_without_param, Cant include since it contain parameter
    "show vessel types": list_vessel_types,
    "show voyage report": voyage_report
    #"show voyages from port": get_voyages_from_port  Cant include since it contain parameter
}

"""def execute_command(question):

    question = question.lower().strip()

    if question in ROUTES:
        return ROUTES[question]()

    return "Command not found."""


def execute_command(question):

    question = question.lower().strip()

    # Dynamic commands (parameters)
    if question.startswith("show voyages from"):

        port = question.replace("show voyages from", "").strip()

        return get_voyages_from_port(port)    
    
    elif question.startswith("show vessels of"):

        vessel_type = question.replace("show vessels of", "").strip()

        mapping = {
            "container": "Container",
            "tanker": "Tanker",
            "bulk carrier": "Bulk Carrier",
            "ro-ro": "Ro-Ro"
        }

        if vessel_type in mapping:
            return get_vessels_by_type(mapping[vessel_type])

        return "Unknown vessel type."

    elif question.startswith("update voyage"):

        try:
            parts = question.split()

            voyage_id = int(parts[2])

            status = parts[3].capitalize()
            return update_voyage_status(voyage_id, status)
        except (IndexError, ValueError):
            return "Usage: update voyage <voyage_id> <status>"
    
    elif question.startswith("delete voyage"):
        try:

            parts = question.split()

            voyage_id = int(parts[2])

            return delete_voyage(voyage_id)

        except (IndexError, ValueError):
            return "Usage: delete voyage <voyage_id>"
    # Fixed commands
    elif question in ROUTES:

        return ROUTES[question]()

    return "Command not found."