from database.database import Database


class PortRepository:

    def __init__(self):
        self.db = Database()


    def get_all_ports(self):

        query = """
        SELECT *
        FROM ports
        """

        return self.db.query(query)