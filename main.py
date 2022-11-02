import sqlite3 as sql

boglanish = sql.connect("susys.db")

malumot = boglanish.cursor()

malumot.execute("""
CREATE TABLE IF NOT EXISTS oddiy(
    Nexia3 TEXT,
    Gentra TEXT,
    Nexia1 INTEGER
)                                          
""")

malumot.execute("""
CREATE TABLE IF NOT EXISTS Sport(
    Lambarghini TEXT,
    Ferari TEXT,
    Bugatti INTEGER
)                                          
""")

malumot.execute("""
CREATE TABLE IF NOT EXISTS Urtacha(
    Tesla TEXT,
    Sakura TEXT,
    GTR INTEGER
)                                          
""")