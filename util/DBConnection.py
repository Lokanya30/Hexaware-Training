import mysql.connector
import configparser

class DBConnection:
    connection = None

    @staticmethod
    def get_connection(config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        
        db_config = {
            'host': config['DATABASE']['host'],
            'user': config['DATABASE']['user'],
            'password': config['DATABASE']['password'],
            'database': config['DATABASE']['database']
        }
        
        try:
            if DBConnection.connection is None:
                DBConnection.connection = mysql.connector.connect(**db_config)
                print("Database connection established successfully!")
            return DBConnection.connection
        except mysql.connector.Error as err:
            print(f"Error connecting to database: {err}")
            raise
