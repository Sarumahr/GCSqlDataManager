import sqlite3 as sql
from sqlite3 import Error
from sqlite3 import Connection

GC_CONDITION_ROWS = ('id', 'cond_code', 'cond_text')
GC_CONDITION_TABLE = "GC_CONDITION"
GC_PUBLISHER_ROWS = ('id', 'name', 'date')
GC_PUBLISHER_TABLE = "GC_PUBLISHER"
GC_LANGUAGE_ROWS = ('id', 'lang_code', 'lang_text')
EXAMPLE_LANGUAGE = (2, 'en', 'englisch')
GC_LANGUAGE_TABLE = "GC_LANGUAGE"
GC_CONSOLE_ROWS = ('id', 'upc', 'name', 'area', 'publisher', 'release_date', 'image', 'cond_pack', 'cond_book', 'cond_console', 'price', 'price_history')
GC_CONSOLE_TABLE = "GC_CONSOLE"
GC_GAME_ROWS = ('id', 'upc', 'name', 'edition', 'lang', 'area', 'publisher', 'release_date', 'image', 'usk', 'console', 'players', 'storage', 'cond_shell', 'cond_book', 'cond_disk', 'price', 'price_history')
GC_GAME_TABLE = "GC_GAME"
GC_PRICE_HISTORY_ROWS = ('id', 'date', 'game', 'shop', 'price')
GC_PRICE_HISTORY_TABLE = "GC_PRICE_HISTORY"

def CreateConnection(db_file: str) -> Connection:
    """ Create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sql.connect(db_file)
    except Error as e:
        print(e)
    return conn

def CreateInsert(tableName: str, rows: tuple) -> str:
    """
    Creates insert SQL query 
    :param tableName:
    :param rows:
    :return: query
    """
    mark = []
    for val in rows:
        mark.append('?')
    query = f'''
        INSERT INTO {tableName}({','.join(rows)}) VALUES({','.join(mark)})
    '''
    return query

def CreateDatabaseEntry(conn: Connection, table: str, rows: tuple, entry: tuple) -> int:
    """
    Create a new entry into the given table
    :param conn:
    :param entry:
    :return: entry id
    """
    query = CreateInsert(table, rows)
    return ExecuteQuery(conn, query, entry)

def ExecuteQuery(conn: Connection, query: str, object: tuple) -> int:
    """ 
    Execute the given query into the database
    :param conn:
    :param query:
    :param object:
    :return: last id of the given table
    """
    cur = conn.cursor()
    cur.execute(query, object)
    conn.commit()
    return cur.lastrowid 

def main():
    database = r""

    conn = CreateConnection(database)
    with conn:
        row_id = CreateDatabaseEntry(conn, GC_LANGUAGE_TABLE, GC_LANGUAGE_ROWS, EXAMPLE_LANGUAGE)
        print(row_id)

if __name__ == '__main__':
    main()
