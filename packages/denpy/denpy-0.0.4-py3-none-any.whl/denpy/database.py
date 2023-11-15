import sqlite3
import inspect

def get(table: str, value: str, where: str = None, fetchone: bool = True) -> str | None:

    # Get database file path
    path = inspect.getmodule(inspect.currentframe().f_back).__file__.split('\\')
    path.pop(-1)
    path.pop(-1)
    path.append('database.db')
    path = '\\'.join(path)

    # Connect with database
    database = sqlite3.connect(path)
    cursor = database.cursor()

    # Get data
    if where is None:
        if fetchone is True:
            item = cursor.execute(f'SELECT {value} FROM {table}').fetchone()
        else:
            item = cursor.execute(f'SELECT {value} FROM {table}').fetchall()
    else:
        if fetchone is True:
            item = cursor.execute(f'SELECT {value} FROM {table} WHERE ? = ?', (where.split(' = ')[0], where.split(' = ')[1])).fetchone()
        else:
            item = cursor.execute(f'SELECT {value} FROM {table} WHERE ? = ?', (where.split(' = ')[0], where.split(' = ')[1])).fetchall()

    # Disconnect database
    cursor.close()
    database.close()

    # Returning the data
    if item is None:
        return None
    else:
        return item[0]


def insert(table: str, parameter: list, values: list):

    # Get database file path
    path = inspect.getmodule(inspect.currentframe().f_back).__file__.split('\\')
    path.pop(-1)
    path.pop(-1)
    path.append('database.db')
    path = '\\'.join(path)

    # Connect with database
    database = sqlite3.connect(path)
    cursor = database.cursor()

    # Insert data
    cursor.execute(f'INSERT INTO {table}({", ".join(parameter)}) VALUES({", ".join(values)})')

    # Overwrite data & disconnect database
    database.commit()
    cursor.close()
    database.close()


def edit(table: str, parameter: str, value: str, where: str = None):

    # Get database file path
    path = inspect.getmodule(inspect.currentframe().f_back).__file__.split('\\')
    path.pop(-1)
    path.pop(-1)
    path.append('database.db')
    path = '\\'.join(path)

    # Connect with database
    database = sqlite3.connect(path)
    cursor = database.cursor()

    # Edit data
    if where is None:
        cursor.execute(f'UPDATE {table} SET ? = ?', (parameter, value))
    else:
        cursor.execute(f'UPDATE {table} SET ? = ? WHERE ? = ?', (parameter, value, where.split(' = ')[0], where.split(' = ')[1]))

    # Overwrite data & disconnect database
    database.commit()
    cursor.close()
    database.close()


def delete(table: str, value: str = None, where: str = None):

    # Get database file path
    path = inspect.getmodule(inspect.currentframe().f_back).__file__.split('\\')
    path.pop(-1)
    path.pop(-1)
    path.append('database.db')
    path = '\\'.join(path)

    # Connect with database
    database = sqlite3.connect(path)
    cursor = database.cursor()

    # Delete data
    if where is None:
        if value is None:
            cursor.execute(f'DELETE FROM {table}')
        else:
            cursor.execute(f'DELETE {value} FROM {table}')
    else:
        if value is None:
            cursor.execute(f'DELETE FROM {table} WHERE ? = ?', (where.split(' = ')[0], where.split(' = ')[1]))
        else:
            cursor.execute(f'DELETE {value} FROM {table} WHERE ? = ?', (where.split(' = ')[0], where.split(' = ')[1]))

    # Overwrite data & disconnect database
    database.commit()
    cursor.close()
    database.close()
