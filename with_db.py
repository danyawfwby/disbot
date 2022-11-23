import sqlite3

def exec_sql(*args):
    try:
        sqlite_connection = sqlite3.connect("Discord.db")
        cursor = sqlite_connection.cursor()
        cursor.execute(*args)
        names = []
        values = cursor.fetchall()
        if(len(values)):
            names = [description[0] for description in cursor.description]
        sqlite_connection.commit()
        cursor.close()
        return names, values
    except sqlite3.Error as error:
        print("Ошибка в работе с базой данных: ", error)



def create_table():
    try:
        sqlite_connection = sqlite3.connect("Discord.db")
        sqlite_create_table_query = '''CREATE TABLE if not exists "users" (
                        	"id"	INTEGER NOT NULL DEFAULT 1 UNIQUE,
                            "discord_id"	INTEGER NOT NULL DEFAULT 0 UNIQUE,
                            "coins"	INTEGER NOT NULL DEFAULT 0,
                            "warns"	INTEGER NOT NULL DEFAULT 0,
                            "name"	TEXT NOT NULL DEFAULT 'ПОМИДОР',
                            "is_verify"	INTEGER NOT NULL DEFAULT 0,
                            "lvl"	INTEGER NOT NULL DEFAULT 0,
                            "referer"	INTEGER NOT NULL DEFAULT 0,
                            "cps"	REAL NOT NULL DEFAULT 1,
                    PRIMARY KEY("id" AUTOINCREMENT)
                );'''

        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка в работе с базой данных: ", error)