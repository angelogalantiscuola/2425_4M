class Automobile:
    def __init__(self,targa:str,modello:str,categoria:str):
        self._targa = targa
        self._modello = modello
        self._categoria = categoria
        self.disponibile = True

class AgenziaNoleggio:
    def __init__(self,lista_auto:list):
        self._lista_auto = lista_auto
        self._lista_auto_noleggiate = []
    
    def aggiungi_auto(self,Automobile):
        trovata = False

        for auto in self._lista_auto:  
            if auto._targa == Automobile._targa:
                trovata = True
                break
        if trovata == True:
            raise ValueError("ERRORE AUTO NON TROVATA")
        self._lista_auto.append(Automobile)

    def noleggia_auto(self,Automobile):
        trovata = False

        for auto in self._lista_auto:  
            if auto._targa == Automobile._targa:
                trovata = True
                Automobile.disponibile = False
                self._lista_auto_noleggiate.append(Automobile)
                self._lista_auto.remove(Automobile)
                break
            
        if trovata == False:
            raise ValueError("ERRORE AUTO NON TROVATA")

    def visualizza_auto_disponibili(self):
        i = 0
        for auto in self._lista_auto:
            i = i + 1
            print(f"auto disponibile {i};\n{auto._targa},{auto._modello},{auto._categoria}\n")

    def visualizza_auto_noleggiate(self):
        i = 0
        for auto in self._lista_auto_noleggiate:
            i = i + 1
            print(f"auto noleggiata {i};\n{auto._targa},{auto._modello},{auto._categoria}\n")
