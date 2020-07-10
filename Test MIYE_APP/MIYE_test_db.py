import pytest
import sqlite3


print("\nTest id and roomName in service table")
def test_service_table_1():
    conn = sqlite3.connect('database.db')
    # Connect to cursor
    curs = conn.cursor()
    # Show the values
    curs.execute('SELECT roomName FROM service WHERE id = 1')
    rows = curs.fetchone()
    assert 'roomName', 'Facial Massage'
def test_service_table_2():
    conn = sqlite3.connect('database.db')
    # Connect to cursor
    curs = conn.cursor()
    # Show the values
    curs.execute('SELECT roomName FROM service WHERE id = 2')
    rows = curs.fetchone()
    assert 'roomName', 'Swdenish'

print("\nTest id  and cost in service table")
def test_service_table_3():
    conn = sqlite3.connect('database.db')
    # Connect to cursor
    curs = conn.cursor()
    # Show the values
    curs.execute('SELECT cost FROM service WHERE id = 2')
    rows = curs.fetchone()
    assert 'cost', '300'

def test_service_table_4():
    conn = sqlite3.connect('database.db')
    # Connect to cursor
    curs = conn.cursor()
    # Show the values
    curs.execute('SELECT cost FROM service WHERE id = 4')
    rows = curs.fetchone()
    assert 'cost', '100'
