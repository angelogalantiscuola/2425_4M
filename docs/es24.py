from datetime import date
class Film:
    def __init__(self,titolo:str,regista:str,anno_uscita:date,genere:str,rating:float):
        self._titolo = titolo
        self._regista = regista
        self._anno_uscita = anno_uscita
        self._genere = genere
        self._rating = rating

    @property
    def titolo(self):
        return self._titolo
    @titolo.setter
    def titolo(self,titolo):
        if type(titolo) == str:
            self._titolo = titolo

    @property
    def regista(self):
        return self._regista
    @regista.setter
    def regista(self,regista):
        if type(regista) == str:
            self._regista = regista

    @property
    def anno_uscita(self):
        return self._anno_uscita
    @anno_uscita.setter
    def anno_uscita(self,anno_uscita):
        if type(anno_uscita) == date:
            self._anno_uscita = anno_uscita

    @property
    def genere(self):
        return self._genere
    @genere.setter
    def genere(self,genere):
        if type(genere) == str:
            self._genere = genere

    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self,rating):
        if type(rating) == float:
            self._rating = rating


class Libreria:
    def __init__(self,lista_film:list):
        self._lista_film = lista_film
    
    def aggiungi_film(self,film):
        self._lista_film.append(film)
    
    def cerca_film_titolo_o_registra(self,cosa_cercata,si_o_no:bool):
        if si_o_no == True:
            #cerca titolo
            trovato = False
            for film in self._lista_film:
                if film._titolo == cosa_cercata:
                    trovato = True
                    break
            if trovato == True:
                print("film trovato")
            else:
                raise ValueError("ERRORE FILM NON TROVATO")
        else:
            #cerca regista
            trovato = False
            for film in self._lista_film:
                if film._regista == cosa_cercata:
                    trovato = True
                    break
            if trovato == True:
                print("regista trovato")
            else:
                raise ValueError("ERRORE REGISTA NON TROVATO")
    
    def stampa_tutti_film(self):
        for film in self._lista_film:
            print(f"NOME:{film._titolo},REGISTA:{film._regista}, ANNO DI USCITA:{film._anno_uscita}, GENERE:{film._genere}, RATING:{film._rating}.")
    
    def media_valutazione_tutti_film(self):
        rating_tot = 0
        i = 0
        for film in self._lista_film:
            i = i + 1
            rating_tot = film._rating + rating_tot
        media = rating_tot / i
        print(f"la media di tutti i film è {media}")
oggi = date.today
film1 = Film("bho1","mio padre1",oggi,"fabio",8)           
film2 = Film("bho2","mio padre2",oggi,"fabio",3.4)
film3 = Film("bho3","mio padre3",oggi,"fabio",5)
film4 = Film("bho4","mio padre4",oggi,"fabio",8)
film5 = Film("bho5","mio padre5",oggi,"fabio",9)
libreria = Libreria([film1,film2,film3,film4])
libreria.aggiungi_film(film5)
libreria.cerca_film_titolo_o_registra("mio padre1",False)
libreria.stampa_tutti_film()
libreria.media_valutazione_tutti_film()
