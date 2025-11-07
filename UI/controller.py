import flet as ft
from UI.view import View
from model.model import Model
from UI.alert import AlertManager
'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popola_musei(self):
        lista_musei= self._model.get_musei()
        self._view._dd_musei.options.append(ft.dropdown.Option(key="Nessun filtro",text="Nessun filtro"))
        for museo in lista_musei:
            self._view._dd_musei.options.append(ft.dropdown.Option(key=museo.id, text=museo.nome))

    def popola_epoca(self):
        lista_epoca= self._model.get_epoche()
        self._view._dd_epoca.options.append(ft.dropdown.Option(key="Nessun filtro",text="Nessun filtro"))
        for epoca in lista_epoca:
            self._view._dd_epoca.options.append(ft.dropdown.Option(key=epoca, text=epoca))


    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA ARTEFATTI
    def handler_artefatti_button(self,e):
        self.museo_selezionato = self._view._dd_musei.value
        self.epoca_selezionato = self._view._dd_epoca.value
        self._view._artefatti_list.clean()

        lista_artefatti= self._model.get_artefatti_filtrati(self.museo_selezionato, self.epoca_selezionato)
        if len(lista_artefatti) == 0:
            alt = AlertManager(self._view.page)
            alt.show_alert('Non è stata trovata alcuna corrispondenza')
        for artefatto in lista_artefatti:
            self._view._artefatti_list.controls.append(ft.Text(f'{artefatto.nome}'))


        self._view.update()
