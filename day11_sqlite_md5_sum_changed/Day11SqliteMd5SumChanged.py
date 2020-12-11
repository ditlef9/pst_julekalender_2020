# Filename: Day11SqliteMd5SumChanged.py
# Author: S Ditlefsen
# License: http://opensource.org/licenses/gpl-license.php GNU Public License

# Assignment:
#
import hashlib
import sqlite3



class Day11SqliteMd5SumChanged:
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~ Day 11 ~~~~~~~~~~~~~~~~~~~~~~~~')

    """ Create connection """
    def create_connection(db_file):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except sqlite3.Error as e:
            print(e)

        return conn

    """ Print rows """
    def print_rows(conn, table):
        print("\n-----------")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM " + table)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        x=0
        for row in records:
            get_first_name = row[0]
            get_last_name = row[1]
            get_md5 = row[2]

            print(str(x) + "\t" + get_first_name + "\t" + get_last_name + "\t" + get_md5)

            x=x+1
        cursor.close()

    """ Checkpoint """
    def checkpoint(conn):
        print("\n-----------")
        print("Checkpoint")
        print("PRAGMA wal_autocheckpoint = 0")
        print("PRAGMA wal_checkpoint(PASSIVE)")
        cursor = conn.cursor()
        cursor.execute("PRAGMA wal_autocheckpoint = 0")
        cursor.execute("PRAGMA wal_checkpoint(PASSIVE)")
        cursor.close()


    """ Check md5sum in rows """
    def check_md5sum_in_rows(conn, table):
        print("\n-----------")
        print("Checking table: " + table)

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM " + table)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Checking each row")
        x = 0
        for row in records:
            get_first_name = row[0]
            get_last_name = row[1]
            get_md5 = row[2]
            get_md5_size = len(get_md5)

            check_string = get_first_name + get_last_name;
            check_md5 = hashlib.md5(check_string.encode('utf-8')).hexdigest()

            if(get_md5 != check_md5):
                print("Md5 sum mismatch: " + str(x) + "\t" + get_first_name + "\t" + get_last_name + "\t" + get_md5 + "\t" + str(get_md5_size) + "\t" + check_md5)
                print("SELECT * FROM " + table + " WHERE formavn='" + get_first_name + "'")

            x = x+1
        cursor.close()


    """ Check for needle in rows """
    def check_for_needle_in_rows(conn, table, needle):
        print("\n-----------")
        print("Checking for needle " + needle + " in: " + table)

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM " + table + " WHERE fornavn LIKE '%" + needle + "%' OR etternavn LIKE '%" + needle + "%' OR md5 LIKE '%" + needle + "%'")
        records = cursor.fetchall()
        print("Query= SELECT * FROM " + table + " WHERE fornavn LIKE '%" + needle + "%' OR etternavn LIKE '%" + needle + "%' OR md5 LIKE '%" + needle + "%'")
        print("Total rows are:  ", len(records))
        print("Checking each row")
        x = 0
        for row in records:
            get_first_name = row[0]
            get_last_name = row[1]
            get_md5 = row[2]
            get_md5_size = len(get_md5)

            check_string = get_first_name + get_last_name;
            check_md5 = hashlib.md5(check_string.encode('utf-8')).hexdigest()

            print("Needle found: " + str(x) + "\t" + get_first_name + "\t" + get_last_name + "\t" + get_md5 + "\t" + str(get_md5_size) + "\t" + check_md5)
            print("SELECT * FROM " + table + " WHERE formavn='" + get_first_name + "'")


            x = x+1
        cursor.close()


    """ Scrip start """

    # Connect
    db_file = "./day11_sqlite_md5_sum_changed/liste.db"
    conn = create_connection(db_file)

    # Sync db
    #checkpoint(conn)

    # Print rows
    #print_rows(conn, "slemme")
    #print_rows(conn, "snille")

    # Check md5 sum
    check_md5sum_in_rows(conn, "slemme")
    check_md5sum_in_rows(conn, "snille")

    # Find needle
    check_for_needle_in_rows(conn, "slemme", "}")
    check_for_needle_in_rows(conn, "snille", "}")
    check_for_needle_in_rows(conn, "slemme", "{")
    check_for_needle_in_rows(conn, "snille", "{")
    check_for_needle_in_rows(conn, "slemme", "PST")
    check_for_needle_in_rows(conn, "snille", "PST")