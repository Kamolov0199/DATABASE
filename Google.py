import sqlite3 as sql

boglanish = sql.connect("Google.db")

chat = boglanish.cursor()

chat.execute("""
CREATE TABLE IF NOT EXISTS Tropic(
    ism TEXT,
    qayerda chiqarilgan TEXT,
    srog INTEGER
)                                          
""")

chat.execute("""
CREATE TABLE IF NOT EXISTS Pepsi(
    tami TEXT,
    nimadan tayyorlanishi TEXT,
    Qancha vaqt saqlanishi INTEGER
)                                          
""")

chat.execute("""
CREATE TABLE IF NOT EXISTS Fanta(
    rangi TEXT,
    kimyoviy reaksiyalari TEXT,
    sonlari INTEGER
)                                          
""")