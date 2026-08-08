from repositories.port_repository import PortRepository


class PortService:

    def __init__(self):
        self.repository = PortRepository()

    def show_ports(self):

        ports = self.repository.get_all_ports()

        return ports.to_string(index=False)

    def search_ports(self, country):

        ports = self.repository.get_ports_by_country(country)

        if ports.empty:
            return f"No ports found for country: {country}"

        return ports.to_string(index=False)

    def get_port_statistics(self):

        ports = self.repository.get_all_ports()

        return {
            "total_ports": len(ports),
            "countries": ports["country"].nunique()
        }