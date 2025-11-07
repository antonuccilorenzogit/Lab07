from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        self._lista_musei= []


    def get_museo(self):
        self._lista_musei = []
        cnx = ConnessioneDB.get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM museo")
            for row in cursor:
                museo = Museo(row['id'],row['nome'],row['tipologia'])
                self._lista_musei.append(museo)
            cursor.close()
            cnx.close()
            return self._lista_musei
        else:
            print('Connessione non riuscita')
            return None



