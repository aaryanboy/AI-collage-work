import mysql.connector

# Establish connection
conn = mysql.connector.connect(
    host="localhost",       # or your server's address
    user="root",    # MySQL username
    password="", # MySQL password
    database="mydatabasepython"  # Database name
)

print("Connected successfully!")
dxv