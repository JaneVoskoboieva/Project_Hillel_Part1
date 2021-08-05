import sqlite3


def create_database():
    """Function for creating database"""
    connection = sqlite3.connect('blog.sqlite3')
    cursor = connection.cursor()
    sql = """CREATE TABLE IF NOT EXISTS records (
    id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    Title TEXT,
    Description TEXT)"""
    cursor.execute(sql)
    connection.commit()
    connection.close()
    return cursor


def all_records():
    """Function for showing up all records from the blog"""
    connection = sqlite3.connect('blog.sqlite3')
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM records""")
    all_records = cursor.fetchall()
    return all_records


def add_record(title, description):
    """Function for adding records to the blog
    required:
    title - text
    description - text"""
    connection = sqlite3.connect('blog.sqlite3')
    cursor = connection.cursor()
    sql = f'INSERT INTO records (Title, Description) VALUES ("{title}", "{description}")'
    cursor.execute(sql)
    connection.commit()
    connection.close()
    return None


def edit_record(identifier, title, description):
    """Function edit records
    required:
    identifier - integer
    title - text
    description - text"""
    connection = sqlite3.connect('blog.sqlite3')
    cursor = connection.cursor()
    sql = f"UPDATE records SET Title = {title}, Description = {description} WHERE id = {identifier}"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    return None


def delete_record(identifier):
    """Function deletes record
    required:
    identifier - integer"""

    connection = sqlite3.connect('blog.sqlite3')
    cursor = connection.cursor()
    sql = "DELETE FROM records WHERE id = {identifier}"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    return None
