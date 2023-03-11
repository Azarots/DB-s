import sqlite3

conn = sqlite3.connect("Paskaita10.db")
c = conn.cursor()

with conn:
    c.execute(''' CREATE TABLE IF NOT EXISTS DARBUOTOJAI (
        pavadinimas TEXT,
        destytojas TEXT,
        trukme INTEGER
    )
    ''')

with conn:
    c.execute('''
    INSERT INTO DARBUOTOJAI (pavadinimas, destytojas, trukme)
    VALUES ('Vadyba', 'Domantas', 40),
           ('Python', 'Donatas', 80),
           ('Java', 'Tomas', 80)
    ''')

with conn:
    c.execute('''
    SELECT * FROM DARBUOTOJAI
    WHERE trukme > 50
    ''')
    print("Lectures with duration greater than 50:")
    print(c.fetchall())

with conn:
    c.execute('''
    UPDATE DARBUOTOJAI
    SET pavadinimas = 'Python programavimas'
    WHERE pavadinimas = 'Python'
    ''')

with conn:
    c.execute('''
    DELETE FROM DARBUOTOJAI
    WHERE destytojas = 'Tomas'
    ''')

    c.execute('''
    SELECT * FROM DARBUOTOJAI
    ''')
    print("All lectures:")
    print(c.fetchall())
