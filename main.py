import sqlite3
from config import DATABASE

class DB_Manager:
    def __init__(self, database=DATABASE):
        self.database = database

    def create_tables(self):
        create_projects_table = """
        CREATE TABLE IF NOT EXISTS projects (
            project_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            project_name TEXT NOT NULL,
            description TEXT,
            url TEXT,
            status_id INTEGER,
            FOREIGN KEY(status_id) REFERENCES status(status_id)
        );
        """

        create_status_table = """
        CREATE TABLE IF NOT EXISTS status (
            status_id INTEGER PRIMARY KEY,
            status_name TEXT NOT NULL
        );
        """



        connection = sqlite3.connect(self.database)
        with connection:
            connection.execute(create_projects_table)
            connection.execute(create_status_table)
            connection.commit()
