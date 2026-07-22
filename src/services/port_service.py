from repositories.port_repository import PortRepository


class PortService:

    def __init__(self):
        self.repository = PortRepository()


    def show_ports(self):

        ports = self.repository.get_all_ports()

        return ports.to_string(index=False)