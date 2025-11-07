from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        self._lista_artefatti=[]

    def get_artefatto(self):
        self._lista_artefatti= []
        cnx = ConnessioneDB.get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM artefatto")
            for row in cursor:
                artefatto = Artefatto(row['id'],row['nome'],row['tipologia'],row['epoca'], row['id_museo'])
                self._lista_artefatti.append(artefatto)
            cursor.close()
            cnx.close()
            return self._lista_artefatti
        else:
            print('Connessione non riuscita')
            return None