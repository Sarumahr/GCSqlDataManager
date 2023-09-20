import sqlite3 as sql
from sqlite3 import Error
from sqlite3 import Connection

def CreateInsert(tableName: str, rows: tuple) -> str:
    mark = []
    for val in rows:
        mark.append('?')
    query = f'''
        INSERT INTO {tableName}({','.join(rows)}) VALUES({','.join(mark)})
    '''
    return query

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

def CreateCondition(conn: Connection, condition: tuple) -> int:
    """
    Create a new condition into the GC_CONDITION table
    :param conn:
    :param condition:
    :return: condition id
    """
    TABLENAME = "GC_CONDITION"
    ROWS = ('id', 'cond_code', 'cond_text')
    query = CreateInsert(TABLENAME, ROWS)
    return ExecuteQuery(conn, query, condition)

def CreatePublisher(conn: Connection, publisher: tuple) -> int:
    """
    Create a new publisher into the GC_PUBLISHER table
    :param conn:
    :param publisher:
    :return: publisher id 
    """
    TABLENAME = "GC_PUBLISHER"
    ROWS = ('id', 'name', 'date')
    query = CreateInsert(TABLENAME, ROWS)
    return ExecuteQuery(conn, query, publisher)

def CreateLanguage(conn: Connection, language: tuple) -> int:
    """
    Create a new language into the GC_LANGUAGE table
    :param conn:
    :param language:
    :return: language id
    """
    TABLENAME = "GC_LANGUAGE"
    ROWS = ('id', 'lang_code', 'lang_text')
    query = CreateInsert(TABLENAME, ROWS)
    return ExecuteQuery(conn, query, language)

def CreateConsole(conn: Connection, console: tuple) -> int:
    """
    Create a new console into the GC_CONSOLE table
    :param conn:
    :param console:
    :return console id:
    """
    TABLENAME = "GC_CONSOLE"
    ROWS = ('id', 'upc', 'name', 'area', 'publisher', 'release_date', 'image', 'cond_pack', 'cond_book', 'cond_console', 'price', 'price_history')
    query = CreateInsert(TABLENAME, ROWS)
    return ExecuteQuery(conn, query, console)

def CreateGame(conn: Connection, game: tuple) -> int:
    """
    Create a new game into the GC_GAME table
    :param conn:
    :param game:
    :return: game id
    """
    TABLENAME = "GC_GAME"
    ROWS = ('id', 'upc', 'name', 'edition', 'lang', 'area', 'publisher', 'release_date', 'image', 'usk', 'console', 'players', 'storage', 'cond_shell', 'cond_book', 'cond_disk', 'price', 'price_history')
    query = CreateInsert(TABLENAME, ROWS)
    return ExecuteQuery(conn, query, game)

def CreatePriceHistory(conn: Connection, price_history: tuple) -> int:
    """
    Create a new price_history into the GC_PRICE_HISTORY table
    :param conn:
    :param price_history:
    :return: price_history id
    """
    TABLENAME = "GC_PRICE_HISTORY"
    ROWS = ('id', 'date', 'game', 'shop', 'price')
    query = CreateInsert(TABLENAME, ROWS)
    return ExecuteQuery(conn, query, price_history)

def main():
    database = r""

    conn = CreateConnection(database)
    with conn:
        language = (2, 'en', 'englisch')
        lang_id = CreateLanguage(conn, language)
        print(lang_id)

if __name__ == '__main__':
    main()
