# Ce fichier constitu les codes pour la création de la base de données
# Son utilisation sera dans le fichier main.py
import sqlite3 as sq

def connect_to_db():
    """Cette fonction créee la connexion à la base de données"""
    bd_ecole = sq.connect("base_de_données/itp.db")
    return bd_ecole


def creation_table():
    db = connect_to_db()
    cur = db.cursor()
    table = """CREATE TABLE IF NOT EXISTS eleves(id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, postnom TEXT, prenom TEXT, 
    sexe TEXT, classe TEXT, option TEXT, date_inscription TEXT, nom_tuteur TEXT, num_tuteur TEXT, montant_paye REAL,
    date_payement TEXT, code_recu INTEGER)"""
    cur.execute(table)


if __name__ == '__main__':
    con = connect_to_db()
    con
    creation_table()