
from datetime import datetime
class Ristorante:
    def __init__(self,nome):
        self.nome = nome
        self.prenotazioni = []
    #Aggiungere nuove prenotazioni.

    def aggiungi_prenotazione(self,nuova_prenotazione):
        if nuova_prenotazione not in self.prenotazioni:
            self.prenotazioni.append(nuova_prenotazione)
            print('prenotazione aggiunta')
        else:
            print(f'prenotazione gia presente {nuova_prenotazione}')
    #Cancellare una prenotazione.
    def cancellare_prenotazione(self,prenotazione_da_rimuovere):
        if prenotazione_da_rimuovere in self.prenotazioni:
            self.prenotazioni.remove(prenotazione_da_rimuovere)
            print('prenotazione tolta')
        else:
            print(f'prenotazione non presente {prenotazione_da_rimuovere}')
    
    #Cercare prenotazioni per nome del cliente o data.

    def cerca_prenotazioni(self,cliente,data):
        prenotazioni_stesso_data_o_cliente = []
        if cliente != None:
            for n in self.prenotazioni:
                if cliente == n.nome_cliente:
                    prenotazioni_stesso_data_o_cliente.append(n)
        if data != None:
            for d in self.prenotazioni:
                
                if data == d.data_ora:
                    prenotazioni_stesso_data_o_cliente.append(d)
        return prenotazioni_stesso_data_o_cliente
    #Visualizzare tutte le prenotazioni.
    def visualizzare_tutte_prenotazioni(self):
        for p in self.prenotazioni:
            print(p)
    
 


        


class Prenotazioni:
    def __init__(self,nome_cliente,data_ora,anno,numero_di_persone,stato):
        self.nome_cliente = nome_cliente
        self.data_ora = data_ora
        self.numero_di_persone = numero_di_persone
        self.stato = stato

    def __str__(self):
        return f'nome cliente:{self.nome_cliente} data ora:{self.data_ora} numero di persone:{self.numero_di_persone} stato:{self.stato}'

ristorante = Ristorante('Monsce')
prenotazioni1 = Prenotazioni('James Cook',datetime.now().strftime('%Y-%m-%d %H:%M'),2,'confermata',2)
prenotazioni2 = Prenotazioni('Robinson Cappelli',datetime.now().strftime('%Y-%m-%d %H:%M'),4,' attesa',4)
prenotazioni3 = Prenotazioni('Sancho Sanchi',datetime.now().strftime('%Y-%m-%d %H:%M'),7,'confermata',9)
prenotazioni4 = Prenotazioni("Lorenz Pezzolesi",datetime.now().strftime('%Y-%m-%d %H:%M'),85,'confermata',8)
print('---------')
ristorante.aggiungi_prenotazione(prenotazioni1)
ristorante.aggiungi_prenotazione(prenotazioni2)
ristorante.aggiungi_prenotazione(prenotazioni3)
ristorante.aggiungi_prenotazione(prenotazioni4)


print('---------')
#ristorante.cancellare_prenotazione(prenotazioni1)

lista_prenotazioni = ristorante.cerca_prenotazioni('James Cook',None)
for p in lista_prenotazioni:
    print(p)

print('---------')
ristorante.visualizzare_tutte_prenotazioni()

