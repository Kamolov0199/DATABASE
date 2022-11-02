import sqlite3 as sql

boglanish = sql.connect("Odamlar.db")

Infor = boglanish.cursor()

Infor.execute("""
CREATE TABLE IF NOT EXISTS Studentlar(
    ism TEXT,
    familiya TEXT,
    yosh INTEGER
)                                          
""")

Infor.execute("""
CREATE TABLE IF NOT EXISTS Programistlar(
    ishi TEXT,
    ish turi TEXT,
    yashash joyi INTEGER
)                                          
""")

Infor.execute("""
CREATE TABLE IF NOT EXISTS Bekorchilar(
    qilar ishi yoq TEXT,
    Tochnayoq TEXT,
    yoqda INTEGER
)                                          
""")