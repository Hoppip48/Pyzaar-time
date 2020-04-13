import requests
from Apirequest import bazaardatabuy
from Apirequest import bazaardatasell

"""-------------------------------------------------------------------------"""

##### Starting variables ####

budget = input("inserisci budget: ")
bazaarbuy = bazaardatabuy()
bazaarsell = bazaardatasell()

##### Starting variables ####

"""-------------------------------------------------------------------------"""

#### Calculator ####

quantità = int(float(budget)/float(bazaarbuy))
buytot = float(bazaarbuy)*float(quantità)
selltot = float(bazaarsell)*float(quantità)
tasse = float(selltot)/100
bazaarguadagno = float(selltot) - float(buytot) - float(tasse)
percentuale = int(int(bazaarguadagno)/int(budget)*100)

#### Calculator ####

"""-------------------------------------------------------------------------"""

#### Printer ####

def printbazaar():
    print("\n","quantità per arrivare a", budget,": ", quantità)
    print("\n","spesa totale: ", buytot)
    print("\n","tasse: ", tasse)
    if(bazaarguadagno > 0):
        print("guadagno: ", bazaarguadagno)
    else:
        print("not stonks (", bazaarguadagno,")") 
    print("\n", "% di guadagno rispetto al budget: ", percentuale,"%")
printbazaar()

#### Printer ####
