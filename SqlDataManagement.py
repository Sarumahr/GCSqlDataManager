import sqlite3 as sql
from sqlite3 import Error

def ExecuteQuery(conn, query, object):
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


def CreateConnection(db_file):
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

def CreateCondition(conn, condition):
    """
    Create a new condition into the GC_CONDITION table
    :param conn:
    :param condition:
    :return: condition id
    """
    query = ''' INSERT INTO GC_CONDITION(id,cond_code,cond_text)
                VALUES(?,?,?) '''
    return ExecuteQuery(conn, query, condition)

def CreatePublisher(conn, publisher):
    """
    Create a new publisher into the GC_PUBLISHER table
    :param conn:
    :param publisher:
    :return: publisher id 
    """
    query = ''' INSERT INTO GC_PUBLISHER(id,name,date)
                VALUES(?,?,?)'''
    return ExecuteQuery(conn, query, publisher)

def CreateLanguage(conn, language):
    """
    Create a new language into the GC_LANGUAGE table
    :param conn:
    :param language:
    :return: language id
    """
    query = ''' INSERT INTO GC_LANGUAGE(id,lang_code,lang_text)
                VALUES(?,?,?)'''
    return ExecuteQuery(conn, query, language)

def CreateConsole(conn, console):
    """
    Create a new console into the GC_CONSOLE table
    :param conn:
    :param console:
    :return console id:
    """
    query = ''' INSERT INTO GC_CONSOLE(id,upc,name,area,publisher,release_date,image,cond_pack,cond_book,cond_console,price,price_history)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?)'''
    return ExecuteQuery(conn, query, console)

def CreateGame(conn, game):
    """
    Create a new game into the GC_GAME table
    :param conn:
    :param game:
    :return: game id
    """
    query = ''' INSERT INTO GC_GAME(id,upc,name,edition,lang,area,publisher,release_date,image,usk,console,players,storage,cond_shell,cond_book,cond_disk,price,price_history)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
    return ExecuteQuery(conn, query, game)

def CreatePriceHistory(conn, price_history):
    """
    Create a new price_history into the GC_PRICE_HISTORY table
    :param conn:
    :param price_history:
    :return: price_history id
    """
    query = ''' INSERT INTO GC_PRICE_HISTORY(id,date,game,shop,price)
                VALUES(?,?,?,?,?)'''
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