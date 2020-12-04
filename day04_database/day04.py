# Filename: day04.py
# Author: S Ditlefsen
# License: http://opensource.org/licenses/gpl-license.php GNU Public License


# About class:
#   Creates a SQLite database
#   Runs commands

# Assignment:
#   Vi i mellomledergruppa er svært interessert i måltall, og ledelsen ønsker en rapport snarest på summen av kolonnen Maaltall fra og med 2020 til og med 2040. Kan du svare meg med denne summen, omkranset av PST{ og } når du finner ut av det?
import os
import sqlite3
from sqlite3 import Error

class Day04:
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~ Day 04 ~~~~~~~~~~~~~~~~~~~~~~~~')


    """- Create connection -----------------------------------"""
    def create_connection(db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn


    """- Run SQL files from folder ---------------------------"""
    def run_sql_files_from_folder(db_file, conn, directory):
        for filename in os.listdir(directory):
            if filename.endswith(".sql") :
                file = os.path.join(directory, filename)

                # Read SQL
                sql_commands = repr(open(file, 'r').read())

                # Remove start " and '
                if sql_commands.startswith('"'):
                    sql_commands = sql_commands[1:]
                if sql_commands.startswith("'"):
                    sql_commands = sql_commands[1:]

                # Remove end  " and '
                if sql_commands.endswith('"'):
                    sql_commands = sql_commands[:-1]
                if sql_commands.endswith("'"):
                    sql_commands = sql_commands[:-1]

                # Replace line shift
                sql_commands = sql_commands.replace("", "")

                print("\n" + file)
                print(sql_commands)

                try:
                    c = conn.cursor()
                    c.execute(sql_commands)
                except Error as e:
                    print("SQL error: ")
                    print(e)

                continue
            else:
                continue

    """- Scriptstart -----------------------------------------"""

    # Connect to database
    db_file = r"./day04_database/pythonsqlite.db"
    conn = create_connection(db_file)

    # Run SQL
    run_sql_files_from_folder(db_file, conn, "./day04_database/sql")