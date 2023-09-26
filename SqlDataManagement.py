import sqlite3 as sql
from sqlite3 import Error
from sqlite3 import Connection
import constants as c

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
        row_id = CreateDatabaseEntry(conn, c.GC_LANGUAGE_TABLE, c.GC_LANGUAGE_ROWS, c.EXAMPLE_LANGUAGE)
        print(row_id)

if __name__ == '__main__':
    main()
