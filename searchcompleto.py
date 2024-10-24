import sqlite3
import os


def cerca_cartelle(stringa_di_ricerca):
    nome_db = "cartelle.db"
    conn = sqlite3.connect(nome_db)
    c = conn.cursor()
    # Effettua una ricerca parziale insensibile alle maiuscole e minuscole
    c.execute("SELECT * FROM cartelle WHERE nome_cartella LIKE ? COLLATE NOCASE LIMIT 30",
              ('%' + stringa_di_ricerca + '%',))

    cartelle_trovate = c.fetchall()
    conn.close()  # Chiudi la connessione al database

    if len(cartelle_trovate) == 0:
        print("Nessuna cartella trovata")
    else:
        # Restituisce una lista numerata delle cartelle trovate
        for i, cartella in enumerate(cartelle_trovate, start=1):
            print(f"{i}. {cartella[0]}")

    return cartelle_trovate


def apri_cartella(percorso):
    os.startfile(percorso)


# Ciclo infinito per consentire all'utente di fare quante ricerche vuole
while True:
    # Prendere la stringa di ricerca in input
    stringa_di_ricerca = input("Inserisci la stringa di ricerca (per uscire, digita 'exit'): ")

    # Interrompi il ciclo se l'utente vuole uscire
    if stringa_di_ricerca.lower() == 'exit':
        break

    # Chiamare la funzione di ricerca con la stringa di ricerca
    cartelle_trovate = cerca_cartelle(stringa_di_ricerca)

    # Chiedere all'utente di selezionare un'opzione (se esistono opzioni)
    if cartelle_trovate:  # Solo se ci sono cartelle trovate
        try:
            scelta = int(input("Seleziona una cartella da aprire (per tornare al menu, digita '0'): "))
            if scelta == 0:
                continue  # Torna al menu

            # Controlla se la scelta è valida
            if 1 <= scelta <= len(cartelle_trovate):
                percorso = cartelle_trovate[scelta - 1][0]  # Ottieni il percorso della cartella
                apri_cartella(percorso)  # Apri la cartella
            else:
                print("Scelta non valida. Riprova.")

        except ValueError:
            print("Scelta non valida. Riprova.")
