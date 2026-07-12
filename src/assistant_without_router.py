from maritime_service import (
    get_all_vessels,
    get_all_ports,
    get_active_voyages,
    get_all_cargo,
    get_vessels_by_type,
    get_all_voyages,
    get_vessels_by_type_without_param,
    list_vessel_types,
    voyage_report,
    get_voyages_from_port
)

while True:

    question = input("\nAsk: ")

    #vessel_type = input("Type: ")

    if question.lower() == "exit":
        break

    elif question.startswith("show voyages from"):

        port = question.replace("show voyages from", "").strip()
        print(port)
        print(get_voyages_from_port(port))

    elif "container" in question:
        print(get_vessels_by_type("Container"))

    elif "tanker" in question:
        print(get_vessels_by_type("Tanker"))

    elif "bulk" in question:
        print(get_vessels_by_type("Bulk Carrier"))

    elif "ro-ro" in question:
        print(get_vessels_by_type("Ro-Ro"))

    elif "vessel" in question.lower():
        print(get_all_vessels())
    
    elif "report" in question.lower():
        print(voyage_report())

    elif "port" in question.lower():
        print(get_all_ports())

    elif "active voyage" in question.lower():
        print(get_active_voyages())
    
    elif "voyage" in question.lower():
        print(get_all_voyages())

    elif "cargo" in question.lower():
        print(get_all_cargo()) 

    elif "type" in question.lower():
        print(list_vessel_types())   
    
    
    
    #elif vessel_type is not None: #Tanker exmaple by param 
        #print(get_vessels_by_type(vessel_type))

    #elif "container" in question.lower():
        #print(get_vessels_by_type_without_param("Container"))
    else:       
        print("I don't understand")