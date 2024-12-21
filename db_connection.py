import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class MySQLDatabase:
    def __init__(self):
        # Initialize connection details from environment variables
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")
        self.conn = None

    def connect(self):
        """Connects to the MySQL database using the provided credentials."""
        try:
            # Establish connection to the database
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.conn.is_connected():
                print("✅ Connected to MySQL Database")
                return self.conn
        except Error as e:
            print(f"❌ Error while connecting to MySQL: {e}")
            return None

    def close(self):
        """Closes the database connection."""
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("🔌 Connection closed")
