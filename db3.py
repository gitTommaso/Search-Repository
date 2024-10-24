import os
import sqlite3

def elenca_cartelle(percorso):
    lista_cartelle = []

    for root, dirs, files in os.walk(percorso):
        for dir in dirs:
            lista_cartelle.append(os.path.join(root, dir))

    return lista_cartelle



def crea_database(nome_db, lista_cartelle):
    conn = sqlite3.connect(nome_db)
    c = conn.cursor()

    c.execute('''CREATE TABLE cartelle
             (nome_cartella TEXT PRIMARY KEY NOT NULL)''')

    for cartella in lista_cartelle:
        c.execute("INSERT INTO cartelle (nome_cartella) VALUES (?)",
                 (cartella,))

    conn.commit()
    conn.close()

# Ask the user for the path
percorso = input("Inserisci il percorso della cartella: ")

nome_db = "cartelle.db"

lista_cartelle = elenca_cartelle(percorso)
crea_database(nome_db, lista_cartelle)
