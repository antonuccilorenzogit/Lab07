from database.DB_connect import ConnessioneDB
from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO
'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        if epoca == 'Nessun filtro' and museo == 'Nessun filtro':
            lista_artefatti = self._artefatto_dao.get_artefatto()
            return lista_artefatti

        elif epoca == 'Nessun filtro' and museo != 'Nessun filtro':
            artefatti_filtrati= []
            lista_artefatti= self._artefatto_dao.get_artefatto()
            for artefatto in lista_artefatti:
                if artefatto.id_museo == museo:
                    artefatti_filtrati.append(artefatto)
            return artefatti_filtrati

        elif museo == 'Nessun filtro' and epoca != 'Nessun filtro':
            artefatti_filtrati = []
            lista_artefatti = self._artefatto_dao.get_artefatto()
            for artefatto in lista_artefatti:
                if artefatto.epoca == epoca:
                    artefatti_filtrati.append(artefatto)
            return artefatti_filtrati

        else:
            artefatti_filtrati = []
            lista_artefatti = self._artefatto_dao.get_artefatto()
            for artefatto in lista_artefatti:
                if artefatto.epoca == epoca and artefatto.id_museo == museo:
                    artefatti_filtrati.append(artefatto)
            return artefatti_filtrati




    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        insieme_epoche= set()
        if len(self._artefatto_dao._lista_artefatti)==0:
            lista_artefatti= self._artefatto_dao.get_artefatto()
            for artefatto in lista_artefatti:
                insieme_epoche.add(artefatto.epoca)
            return insieme_epoche
        else:
            lista_artefatti = self._artefatto_dao._lista_artefatti
            for artefatto in lista_artefatti:
                insieme_epoche.add(artefatto.epoca)
            return insieme_epoche



    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        if len(self._museo_dao._lista_musei) ==0:
            lista_musei= self._museo_dao.get_museo()
            return lista_musei
        else:
            lista_musei = self._museo_dao._lista_musei
            return lista_musei


