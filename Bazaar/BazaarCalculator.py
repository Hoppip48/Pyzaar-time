from Apirequest import *
import decimal

"""-------------------------------------------------------------------------"""

##### Starting variables ####

#while(True):
budget = input("Enter budget: ")
if(budget == "0"):  
    budget = 10**7
    bazaarbuyin = "0"
    bazaarsellin = "0"
else:
    bazaarbuyin = input("Enter buy price: ")
    bazaarsellin = input("Enter sell price: ") 
print("\n")
if(bazaarbuyin == "0"):
    bazaarbuy = float(bazaardatabuy())+0.1
else:
    bazaarbuy = float(bazaarbuyin)
if(bazaarsellin == "0"):
    bazaarsell = float(bazaardatasell())-0.1
else:
    bazaarsell = float(bazaarsellin)
decimalbuy = decimal.Decimal('%.1f' % (bazaarbuy))
decimalsell = decimal.Decimal('%.1f' % (bazaarsell))
    
##### Starting variables ####

"""-------------------------------------------------------------------------"""

    #### Calculator ####

quantità = int(float(budget)/float(bazaarbuy))
buytot = float(bazaarbuy)*float(quantità)
selltot = float(bazaarsell)*float(quantità)
tasse = float(selltot)/100
bazaarguadagno = float(selltot) - float(buytot) - float(tasse)
percentuale = float(bazaarguadagno)/float(budget)*100
minvendita =  float(bazaarbuy) + float(bazaarbuy)/99

#### Calculator ####

"""-------------------------------------------------------------------------"""
#### decimal-inator ####

decimalbuytot = decimal.Decimal('%.1f' % (buytot))
decimalselltot = decimal.Decimal('%.1f' % (selltot))
decimaltasse = decimal.Decimal('%.1f' % (tasse))
decimalbazaarguadagno = decimal.Decimal('%.1f' % (bazaarguadagno))
decimalpercentuale = decimal.Decimal('%.1f' % (percentuale))
decimalminvendita = decimal.Decimal('%.1f' % (minvendita))

#### decimal-inator ####

"""-------------------------------------------------------------------------"""

#### Printer ####

def printbazaar():
    if(bazaarbuyin == "0" or bazaarsellin == "0"):
        print("buy price: ", decimalbuy)
        print("sell price: ", decimalsell,"\n")
    if(quantità>1024):
        print("quantità troppo elevata, ci potrebbe volere troppo per riceverlo","\n")
    print("quantità per arrivare a", budget,": ", quantità,"\n")
    print("minimo prezzo per vendere: ", decimalminvendita,"\n")
    print("taxes: ", decimaltasse,"\n")
    print("total buy: ", float(decimalbuytot),"\n")
    if(bazaarguadagno > 0):
        print("guadagno totale: ", decimalselltot,"\n")
        print("guadagno effettivo: ", decimalbazaarguadagno,"\n")
    else:
        print("not stonks (", decimalbazaarguadagno,")","\n") 
printbazaar()
print("percentuale di guadagno rispetto al budget: ", decimalpercentuale,"%")
#input()

#### Printer ####

