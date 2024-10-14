import mysql.connector

# RDS connection details
db_endpoint = 'my-db-instance.cj0a6wgyw7qi.ap-south-1.rds.amazonaws.com'  # Replace with your RDS endpoint
db_port = 3306  # MySQL default port
db_user = 'admin'
db_password = 'Cloud123'
db_name = 'testdb'

# Connect to the RDS instance
try:
    connection = mysql.connector.connect(
        host=db_endpoint,
        user=db_user,
        password=db_password,
        database=db_name,
        port=db_port
    )
    print("Connected to the RDS instance.")

    cursor = connection.cursor()

    # Create a table as an example
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS test_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )
    """)
    print("Table created successfully.")

    # Insert data into the table
    cursor.execute("INSERT INTO test_table (name) VALUES ('Ashish')")
    connection.commit()
    print("Data inserted successfully.")

    # Query data
    cursor.execute("SELECT * FROM test_table")
    for row in cursor.fetchall():
        print(row)

    # Close the connection
    cursor.close()
    connection.close()
    print("Connection closed.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
