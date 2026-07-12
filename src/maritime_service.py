from database import Database

from config import DATABASE_PATH

from validators import validate_status

from logger import logger

db = Database(DATABASE_PATH)

#db = Database("data/maritime.db")


def get_all_vessels():
    return db.query("""
        SELECT *
        FROM vessels
    """)


def get_all_ports():
    return db.query("""
        SELECT *
        FROM ports
    """)

def get_all_voyages():
    return db.query("""
        SELECT *
        FROM voyages
    """)

def get_active_voyages():
    return db.query("""
        SELECT *
        FROM voyages
        WHERE status = 'Active'
    """)

def get_voyages_from_port(port_name):

    sql = """
    SELECT
        v.voyage_id,
        ve.vessel_name,
        p1.port_name AS departure_port,
        p2.port_name AS arrival_port,
        v.departure_date,
        v.arrival_date,
        v.status

    FROM voyages v

    JOIN vessels ve
        ON v.vessel_id = ve.vessel_id

    JOIN ports p1
        ON v.departure_port_id = p1.port_id

    JOIN ports p2
        ON v.arrival_port_id = p2.port_id

    WHERE LOWER(p1.port_name) LIKE LOWER(?)
    """

    return db.query(sql, (f"%{port_name}%",))

def get_all_cargo():
    return db.query("""
        SELECT *
        FROM cargo
    """)

def get_vessels_by_type_without_param(vessel_type):

    return db.query(f"""
        SELECT *
        FROM vessels
        WHERE vessel_type = '{vessel_type}'
    """)

def get_vessels_by_type(vessel_type):

    sql = """
        SELECT *
        FROM vessels
        WHERE vessel_type = ?
    """

    return db.query(sql, (vessel_type,))

def list_vessel_types():
    sql = """
    SELECT DISTINCT vessel_type
    FROM vessels
    ORDER BY vessel_type
    """

    return db.query(sql)

def voyage_report_old():

    return db.query("""
        SELECT
            v.voyage_id,
            ve.vessel_name,
            p1.port_name AS departure_port,
            p2.port_name AS arrival_port,
            v.status

        FROM voyages v

        JOIN vessels ve
            ON v.vessel_id = ve.vessel_id

        JOIN ports p1
            ON v.departure_port_id = p1.port_id

        JOIN ports p2
            ON v.arrival_port_id = p2.port_id
    """)

def voyage_report():

    sql = """
    SELECT

        ve.vessel_name,

        p1.port_name AS Departure,

        p2.port_name AS Arrival,

        v.departure_date,

        v.arrival_date,

        v.status

    FROM voyages v

    JOIN vessels ve
        ON v.vessel_id = ve.vessel_id

    JOIN ports p1
        ON v.departure_port_id = p1.port_id

    JOIN ports p2
        ON v.arrival_port_id = p2.port_id

    ORDER BY departure_date
    """

    return db.query(sql)

def add_voyage(
    vessel_id,
    departure_port_id,
    arrival_port_id,
    departure_date,
    arrival_date,
    status
):

    sql = """
    INSERT INTO voyages
    (
        vessel_id,
        departure_port_id,
        arrival_port_id,
        departure_date,
        arrival_date,
        status
    )

    VALUES (?, ?, ?, ?, ?, ?)
    """

    return db.execute(
        sql,
        (
            vessel_id,
            departure_port_id,
            arrival_port_id,
            departure_date,
            arrival_date,
            status
        )
    )

def update_voyage_status(voyage_id, status):

    validate_status(status)

    sql = """
    UPDATE voyages
    SET status = ?
    WHERE voyage_id = ?
    """

    return db.execute(
        sql,
        (status, voyage_id)
    )

def delete_voyage(voyage_id):

    sql = """
    DELETE FROM voyages
    WHERE voyage_id = ?
    """

    rows = db.execute(sql, (voyage_id,))

    if rows == 0:
        return f"Voyage {voyage_id} not found."

    return f"Voyage {voyage_id} deleted successfully."

def create_voyage_with_cargo(
    vessel_id,
    departure_port_id,
    arrival_port_id,
    departure_date,
    arrival_date,
    status,
    cargo_type,
    weight_tons
):

    conn = db.get_connection()

    try:

        cursor = conn.cursor()

        # Insert Voyage
        cursor.execute("""
            INSERT INTO voyages(
                vessel_id,
                departure_port_id,
                arrival_port_id,
                departure_date,
                arrival_date,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            vessel_id,
            departure_port_id,
            arrival_port_id,
            departure_date,
            arrival_date,
            status
        ))

        # Get newly created voyage_id
        voyage_id = cursor.lastrowid

        # Insert Cargo
        cursor.execute("""
            INSERT INTO cargo(
                voyage_id,
                cargo_type,
                weight_tons
            )
            VALUES (?, ?, ?)
        """, (
            voyage_id,
            cargo_type,
            weight_tons
        ))

        conn.commit()

        logger.info("Voyage and Cargo created successfully.")

        return voyage_id

    except Exception as e:

        conn.rollback()

        logger.error(e)

        raise