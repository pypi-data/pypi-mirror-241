import ibm_db


def generate_dummy_data():
    data = [
        ("Alice", 25, "alice@example.com", "123 Main St"),
        ("Bob", 30, "bob@example.com", "456 Elm St"),
        ("Charlie", 22, "charlie@example.com", "789 Oak St"),
        ("David", 35, "david@example.com", "101 Maple Ave"),
        ("Eva", 28, "eva@example.com", "202 Pine Rd"),
        ("Frank", 40, "frank@example.com", "123 Main St"),
        ("Grace", 29, "grace@example.com", "456 Elm St"),
        ("Hank", 27, "hank@example.com", "789 Oak St"),
        ("Ivy", 32, "ivy@example.com", "101 Maple Ave"),
        ("Jack", 26, "jack@example.com", "202 Pine Rd"),
    ]

    return data


def create_schema(conn, schema_name):
    create_schema_query = f"CREATE SCHEMA {schema_name}"

    try:
        stmt = ibm_db.exec_immediate(conn, create_schema_query)
        print(f"Schema {schema_name} created successfully.", stmt)
    except Exception as e:
        print(f"Error: {e}")


def create_table(conn, schema_name):
    create_table_query = f'''
        CREATE TABLE {schema_name}.dummy_data (
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            name VARCHAR(100),
            age INTEGER,
            email VARCHAR(100),
            address VARCHAR(200)
        )
    '''

    try:
        stmt = ibm_db.exec_immediate(conn, create_table_query)
        print("Table created successfully.", stmt)
    except Exception as e:
        print(f"Error: {e}")


def insert_data(conn, schema_name):
    data = generate_dummy_data()
    insert_query = f"INSERT INTO {schema_name}.dummy_data (name, age, email, address) VALUES (?, ?, ?, ?)"

    try:
        for row in data:
            stmt = ibm_db.prepare(conn, insert_query)
            ibm_db.execute(stmt, tuple(row))
        print("Data inserted successfully.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    USER = "db2dev"
    PASSWORD = "Welcome4$"
    DB = "testdb"
    HOST = "localhost"
    PORT = "50000"
    PROTOCOL = "TCPIP"
    SCHEMA_NAME = "testschema"

    conn_string = (
        f"DATABASE={DB};"
        f"HOSTNAME={HOST};"
        f"PORT={PORT};"
        f"PROTOCOL={PROTOCOL};"
        f"UID={USER};"
        f"PWD={PASSWORD};"
    )

    conn = ibm_db.connect(conn_string, "", "")
    if conn:
        create_schema(conn, SCHEMA_NAME)
        create_table(conn, SCHEMA_NAME)
        insert_data(conn, SCHEMA_NAME)
        ibm_db.close(conn)
