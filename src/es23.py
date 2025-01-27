from datetime import date
class Utente:
    def __init__(self,profilo:tuple):
        self._profilo = profilo
        self._lista_seguiti = []
        self._album_creati = []
        self._lista_foto = []

    def carica_foto(self,Foto):
        if type(Foto) != str and type(Foto) != int and type(Foto) != float and type(Foto) != bool and type(Foto) != tuple:
            self._lista_foto.append(Foto)
        else:
            raise ValueError("ERRORE CARICA_FOTO")
        
    def segui_utente(self,Utente):
        if type(Utente) != str and type(Utente) != int and type(Utente) != float and type(Utente) != bool and type(Utente) != tuple:
            self._lista_seguiti.append(Utente)
        else:
            raise ValueError("ERRORE SEGUI_UTENTE")
        
class Foto:
    def __init__(self,id:str,titolo:str,descrizione:str,quando_creata:date,autore:Utente,a_che_album_appartiene):
        self._id = id
        self._titolo = titolo
        self._descrizione = descrizione
        self._quando_creata = quando_creata
        self._autore = autore
        self._a_che_album_appartiene = a_che_album_appartiene

    def metti_in_un_album(self,album):
        album._lista_foto.append(self)

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id):
        if type(id) == str:
            self._id = id

    @property
    def titolo(self):
        return self._titolo
    @titolo.setter
    def titolo(self,titolo):
        if type(titolo) == str:
            self._titolo = titolo
    
    @property
    def descrizione(self):
        return self._descrizione
    @descrizione.setter
    def descrizione(self,descrizione):
        if type(descrizione) == str:
            self._descrizione = descrizione

    @property
    def quando_creata(self):
        return self._quando_creata
    @quando_creata.setter
    def quando_creata(self,quando_creata):
        if type(quando_creata) == date:
            self._quando_creata = quando_creata


    @property
    def autore(self):
        return self._autore
    @autore.setter
    def autore(self,autore):
        if type(autore) != str and type(autore) != int and type(autore) != float and type(autore) != bool and type(autore) != tuple:
            self._autore = autore

    @property
    def a_che_album_appartiene(self):
        return self._a_che_album_appartiene
    @a_che_album_appartiene.setter
    def a_che_album_appartiene(self,a_che_album_appartiene):
        if type(a_che_album_appartiene) == str:
            self._a_che_album_appartiene = a_che_album_appartiene


class Album:
    def __init__(self,titolo:str,descrizione:str,autore:Utente,lista_foto:list):
        self._titolo = titolo
        self._descrizione = descrizione
        self._autore = autore
        self._lista_foto = lista_foto

class Commento:
    def __init__(self,chi_lo_ha_postato:Utente,dove_e_stato_postato:Foto):
        self._chi_lo_ha_postato = chi_lo_ha_postato
        self._dove_e_stato_postato = dove_e_stato_postato

fabio = Utente(("fabio","bila"))
oggi = date.today
album_foto_mare = Album("foto al mare","",fabio,[])
foto1 = Foto(5345355,"foto di fabio al mare","che bello il mare",oggi,fabio,None)
foto1.metti_in_un_album(album_foto_mare)