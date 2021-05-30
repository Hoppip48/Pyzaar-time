import requests
import decimal
    


while(True):
    print("\n  \n")
    #### Lists inizializator ####
    json = requests.get("https://api.hypixel.net/skyblock/bazaar?key=a7c61bba-d7ef-4049-8f42-bc53d6b8d747").json()
    woodjson = ["ENCHANTED_OAK_LOG","ENCHANTED_SPRUCE_LOG","ENCHANTED_BIRCH_LOG","ENCHANTED_DARK_OAK_LOG","ENCHANTED_JUNGLE_LOG","ENCHANTED_ACACIA_LOG"]
    orejson = ["ENCHANTED_COBBLESTONE","ENCHANTED_COAL","ENCHANTED_IRON","ENCHANTED_GOLD","ENCHANTED_REDSTONE","ENCHANTED_LAPIS_LAZULI","ENCHANTED_DIAMOND","ENCHANTED_EMERALD","ENCHANTED_OBSIDIAN","ENCHANTED_FLINT","ENCHANTED_GLOWSTONE_DUST","ENCHANTED_ICE","ENCHANTED_QUARTZ","ENCHANTED_SNOW_BLOCK","ENCHANTED_MITHRIL","STARFALL","REFINED_TITANIUM"]
    jerryjson = ["JERRY_BOX_GREEN","JERRY_BOX_BLUE","JERRY_BOX_PURPLE","JERRY_BOX_GOLDEN"]
    superjson = ["ENCHANTED_BAKED_POTATO","ENCHANTED_GOLDEN_CARROT","ENCHANTED_SUGAR_CANE","ENCHANTED_COAL_BLOCK","ENCHANTED_GOLD_BLOCK","ENCHANTED_LAPIS_LAZULI_BLOCK","ENCHANTED_REDSTONE_BLOCK","ENCHANTED_GLOWSTONE","ENCHANTED_PACKED_ICE","ENCHANTED_BLAZE_ROD","ENCHANTED_REDSTONE_LAMP","SUPER_COMPACTOR_3000","SUMMONING_EYE","CATALYST","WHITE_GIFT","PURPLE_CANDY","ENCHANTED_GRILLED_PORK","REFINED_MINERAL","RECOMBOBULATOR_3000","BOOSTER_COOKIE","JACOBS_TICKET"]
    dropjson = ["ENCHANTED_ROTTEN_FLESH","ENCHANTED_BONE","ENCHANTED_STRING","ENCHANTED_ENDER_PEARL","ENCHANTED_BLAZE_POWDER","GRIFFIN_FEATHER","ENCHANTED_ANCIENT_CLAW","ENCHANTED_SHARK_FIN","GREAT_WHITE_SHARK_TOOTH"]
    cropjson = ["ENCHANTED_CARROT","ENCHANTED_POTATO","ENCHANTED_PUMPKIN","ENCHANTED_SUGAR","ENCHANTED_LEATHER","ENCHANTED_RABBIT_FOOT","ENCHANTED_RABBIT_HIDE","ENCHANTED_PORK","TIGHTLY_TIED_HAY_BALE","MUTANT_NETHER_STALK"]
    slayerjson = ["REVENANT_VISCERA","TARANTULA_SILK","WOLF_TOOTH","GOLDEN_TOOTH"]
    woods = ["Oak","Spruce","Birch","Dark oak","Jungle","Acacia"]
    ores = ["Cobblestone","Coal","Iron","Gold","Redstone","Lapis","Diamond","Emerald","Obsidian","Flint","Glowstone","Ice","Quartz","Snow","Mithril","Starfall","Titanium"]
    jerrys = ["Jerry green","Jerry blue","Jerry purple","Jerry gold"]
    supers = ["Baked Potato","Golden Carrot","Sugar Cane","Coal Block","Gold Block","Lapis Block","Redstone Block","Glowstone Block","Packed Ice","Blaze Rod","Redstone Lamp","Compactor","Summoning Eye","Catalyst","White gift","Purple Candy","Grilled Pork","Refined Mineral","RECOMBOBULATOR","Booster Cookie","Ticket"]     
    drops = ["Rotten Flesh","Bone","String","Ender Pearl","Blaze Powder","Griffon","Claw","Shark Fin","White shark tooth"]
    crops = ["Carrot","Potato","Pumpkin","Sugar","Leather","Rabbit Foot","Rabbit Hide","Pork","Hay Bale","Mutant Wart"]
    slayers = ["Viscera","Silk","Wolf Tooth","Golden Tooth"]
    products = []
    itemsdata = []
    perc = []
    buy = []
    sell = []
    #### Lists iniziaalizator ####
    #### Mammt Simulator ####
    def BestCalculator(itemjson,item, n):
        percentage = []
        for i in range(len(itemjson)):
            theybuy = json["products"][itemjson[i]]["sell_summary"][0]["pricePerUnit"]
            isell = json["products"][itemjson[i]]["buy_summary"][0]["pricePerUnit"]
            percentage.append(((float(isell)-float(theybuy)-float(isell)/100)/float(theybuy))*100)
        for i in range(len(itemjson)):
            for j in range(len(itemjson)):
                if(percentage[i]>percentage[j]):
                    cumdemon = percentage[i]
                    percentage[i] = percentage[j]
                    percentage[j] = cumdemon
                    cumdemon = itemjson[i]
                    itemjson[i] = itemjson[j]
                    itemjson[j] = cumdemon
                    cumdemon = item[i]
                    item[i] = item[j]
                    item[j] = cumdemon
        for i in range(n):
            itemsdata.append(itemjson[i])
            products.append(item[i])
    BestCalculator(woodjson,woods,1)
    BestCalculator(orejson,ores,4)
    BestCalculator(jerryjson,jerrys,1)
    BestCalculator(superjson,supers,4)
    BestCalculator(dropjson,drops,2)
    BestCalculator(cropjson,crops,2)
    BestCalculator(slayerjson,slayers,1)
    #### Mammt Simulator ####
    #### Bazaar data grabber ####
    for i in range(len(itemsdata)):
        buy.append(json["products"][itemsdata[i]]["sell_summary"][0]["pricePerUnit"])
        sell.append(json["products"][itemsdata[i]]["buy_summary"][0]["pricePerUnit"])
    #### Bazaar data grabber ####
    #### Best inizializator ####
    for i in range(len(itemsdata)):
        ez = float(sell[i])-float(buy[i])-float(sell[i])/100
        perc.append(float(ez)/float(buy[i])*100)
    #### Best inizializator ####
    #### Best chooser ####
    for i in range(len(itemsdata)):
        for j in range(len(itemsdata)):
            if(perc[i]>perc[j]):
                cumdemon = itemsdata[i]
                itemsdata[i] = itemsdata[j]
                itemsdata[j] = cumdemon
                x = perc[i]
                perc[i] = perc[j]
                perc[j] = x
                y = products[i]
                products[i] = products[j]
                products[j] = y
                z = buy[i]
                buy[i] = buy[j]
                buy[j] = z
                q = sell[i]
                sell[i] = sell[j]
                sell[j] = q
    #### Best chooser ####
    #### Price List ####
    for i in range(len(itemsdata)):
        perc[i] = decimal.Decimal('%.1f' % (perc[i]))
    def ProfitList():
        arraystringlist = ""
        for i in range(len(itemsdata)):
            arraystringlist += str(i+1)
            arraystringlist += ") "
            arraystringlist += str(products[i])
            arraystringlist += ": "
            arraystringlist += "buy("
            arraystringlist += str(buy[i])
            arraystringlist += ") | "
            arraystringlist += "sell("
            arraystringlist += str(sell[i])
            arraystringlist += ") | "
            arraystringlist += str(perc[i])
            arraystringlist += "% \n \n"
            #arraystringlist +=  popolarità ,"\n \n"
        return arraystringlist
    print(ProfitList())
    #### Price List ####
    #### itemchooser ####
    numberchungus = int(input("choose item number: "))-1    
    if(numberchungus == -1):
        print("\n---------------------------------------------------------------\n")
        continue
    yourproduct = itemsdata[numberchungus]
    yproduct = products[numberchungus]
    print("product choosen: ",yproduct,"\n")
    finalproduct=yourproduct
    #### itemchooser ####
    #### Bazaar item data ####
    def bazaardatabuy():
        bazaarHighetsPriceBuy = json["products"][finalproduct]["sell_summary"][0]["pricePerUnit"]
        return bazaarHighetsPriceBuy
    def bazaardatasell():
        bazaarLowestPriceSell = json["products"][finalproduct]["buy_summary"][0]["pricePerUnit"]
        return bazaarLowestPriceSell
    #### Bazaar item data ####
####Bazaar Calculator ####
    #### Variables ####
    bq = input("insert budget/quantity (0/1): ")
    if(bq == "0"):  
        budget = input("Enter budget: ")
        if(budget == "0"):  
            budget = 1*(10**7)
            bazaarbuyin = "0"
            bazaarsellin = "0"
        else:
            bazaarbuyin = input("Enter buy price: ")
            bazaarsellin = input("Enter sell price: ")
    else:
        quantità = input("Enter quantity: ")
        if(quantità == "0"):  
            quantità = 1024
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
    #### Calculator ####
    if(bq=="0"):
        quantità = int(float(budget)/float(bazaarbuy))
    else:
        budget = float(quantità)*float(bazaarbuy)
    if(float(budget) > 10**3 and float(budget) < 10^6):
        stringbudget = str(int(int(budget)/10**3))+"k"
    elif(float(budget) > 10**6):
        stringbudget = str(int(int(budget)/10**6))+"M"
    else:
        stringbudget = budget
    buytot = float(bazaarbuy)*float(quantità)
    selltot = float(bazaarsell)*float(quantità)
    tasse = float(selltot)/100
    bazaarguadagno = float(selltot) - float(buytot) - float(tasse)
    percentuale = float(bazaarguadagno)/float(budget)*100
    minvendita =  float(bazaarbuy) + float(bazaarbuy)/99
    #### decimal-inator ####
    decimalbuytot = decimal.Decimal('%.1f' % (buytot))
    decimalselltot = decimal.Decimal('%.1f' % (selltot))
    decimaltasse = decimal.Decimal('%.1f' % (tasse))
    decimalbazaarguadagno = decimal.Decimal('%.1f' % (bazaarguadagno))
    decimalpercentuale = decimal.Decimal('%.1f' % (percentuale))
    decimalminvendita = decimal.Decimal('%.1f' % (minvendita))
    #### Printer ####
    def printbazaar():
        if(bazaarbuyin == "0" or bazaarsellin == "0"):
            print("\nbuy price: ", decimalbuy)
            print("sell price: ", decimalsell,"\n")
        if(int(quantità)>1024):
            print("quantità troppo elevata, ci potrebbe volere troppo per riceverlo","\n")
        if(bq=="0"):
            print("quantità per arrivare a", stringbudget,": ", quantità,"\n")
        else:
            print("prezzo per arrivare a",quantità,": ", stringbudget,"\n")
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
    input()
    print("---------------------------------------------------------------\n")
    #### Printer ####
#### Bazaar Calculator ####

#mammt prima era 340 righe
