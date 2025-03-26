import mysql.connector
from mysql.connector import Error
import os

try:
    # Establish connection
    conn = mysql.connector.connect(
        host="localhost",       # or your server's address
        user="root",            # MySQL username
        password=os.getenv("MYSQL_PASSWORD"),  # Use environment variable
        database="mydatabasepython"
    )

    if conn.is_connected():
        print("Connected successfully!")

        # Create table
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                age INT NOT NULL,
                department VARCHAR(255) NOT NULL
            )
        ''')
        print("Table created successfully.")

except Error as e:
    print(f"Error: {e}")

finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Connection closed.")
