import sqlite3

def buildKits():
    # Create table
    conn = sqlite3.connect('codeforgood.db')
    c = conn.cursor()
    c.execute("INSERT INTO kits VALUES (1, 'Name', 3, 'Infants', 'mardi Gras','','', 'digital', 'stuff, stuff, csv stuff', 0)")
    conn.commit()
    conn.close()

def is_number(s):
    try:
        int(s)
        return int(s)
    except ValueError:
        return -1

def connectKits():
    conn = sqlite3.connect('codeforgood.db')
    c = conn.cursor()
    temp = '*'
    c.execute("SELECT "+temp+ " FROM kits")
    print(list(map(lambda x: x[0], c.description)))
    for row in c:
        print(row[0])
    conn.close()

def Main():
    connectKits()

Main()