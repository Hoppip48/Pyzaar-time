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
    #### Lists iniziaalizator ####
    #### Mammt Simulator ####
    def BestCalculator(itemjson,item, n, b):
        percentage = []
        buy = []
        sell = []
        for i in range(len(itemjson)):
            buy.append(json["products"][itemjson[i]]["sell_summary"][0]["pricePerUnit"])
            sell.append(json["products"][itemjson[i]]["buy_summary"][0]["pricePerUnit"])
            percentage.append(((float(sell[i])-float(buy[i])-float(sell[i])/100)/float(buy[i]))*100)
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
                    cumdemon = buy[i]
                    buy[i] = buy[j]
                    buy[j] = cumdemon
                    cumdemon = sell[i]
                    sell[i] = sell[j]
                    sell[j] = cumdemon
        if(b):
            ProfitList(item, buy, sell, percentage)
        for i in range(n):
            itemsdata.append(itemjson[i])
            products.append(item[i])
    #### Mammt Simulator ####
    #### Price List ####
    def ProfitList(products, buy, sell, percentage):
        arraystringlist = ""
        for i in range(len(products)):
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
            arraystringlist += str(decimal.Decimal('%.1f' % (percentage[i])))
            arraystringlist += "% \n \n"
            #arraystringlist +=  popolarità ,"\n \n"
        print(arraystringlist)
    #### Price List ####
    #### Cat Calling ####
    BestCalculator(woodjson,woods,1,False)
    BestCalculator(orejson,ores,4,False)
    BestCalculator(jerryjson,jerrys,1,False)
    BestCalculator(superjson,supers,4,False)
    BestCalculator(dropjson,drops,2,False,)
    BestCalculator(cropjson,crops,2,False)
    BestCalculator(slayerjson,slayers,1,False)
    BestCalculator(itemsdata, products,0,True)
    #### Cat Calling ####
    #### itemchooser ####
    numberchungus = int(input("choose item number: "))-1    
    if(numberchungus == -1):
        print("\n---------------------------------------------------------------\n")
        continue
    productjson = itemsdata[numberchungus]
    product = products[numberchungus]
    print("product choosen: ",product,"\n")
    def bazaardatabuy():
        bazaarHighetsPriceBuy = json["products"][productjson]["sell_summary"][0]["pricePerUnit"]
        return bazaarHighetsPriceBuy
    def bazaardatasell():
        bazaarLowestPriceSell = json["products"][productjson]["buy_summary"][0]["pricePerUnit"]
        return bazaarLowestPriceSell
    #### itemchooser ####
#### Bazaar Calculator ####
    #### Variables ####
    bq = input("insert budget/quantity (0/1): ")
    if(bq == "0"):  
        budget = input("Enter budget: ")
        if(budget == "0"):  
            budget = 2*(10**7)
            bazaarbuy = "0"
            bazaarsell = "0"
        else:
            bazaarbuy = input("Enter buy price: ")
            bazaarsell = input("Enter sell price: ")
    else:
        quantità = input("Enter quantity: ")
        if(quantità == "0"):  
            quantità = 1024
            bazaarbuy = "0"
            bazaarsell = "0"
        else:
            bazaarbuy = input("Enter buy price: ")
            bazaarsell = input("Enter sell price: ")
    print("\n")
    if(bazaarbuy == "0"):
        bazaarbuy = float(bazaardatabuy())+0.1
    if(bazaarsell == "0"):
        bazaarsell = float(bazaardatasell())-0.1
    #### Variables ####
    #### Calculator ####
    if(bq=="0"):
        quantità = int(float(budget)/float(bazaarbuy))
    else:
        budget = float(quantità)*float(bazaarbuy)
    buytot = float(bazaarbuy)*float(quantità)
    selltot = float(bazaarsell)*float(quantità)
    tasse = float(selltot)/100
    bazaarguadagno = float(selltot) - float(buytot) - float(tasse)
    percentuale = float(bazaarguadagno)/float(budget)*100
    minvendita =  float(bazaarbuy) + float(bazaarbuy)/99
    if(float(budget) > 10**3 and float(budget) < 10^6):
        budget = str(int(int(budget)/10**3))+"k"
    elif(float(budget) > 10**6):
        budget = str(int(int(budget)/10**6))+"M"
    #### Calculator ####
    #### Printer ####
    def printbazaar():
        print("\nbuy price: ", decimal.Decimal('%.1f' % (bazaarbuy)))
        print("sell price: ", decimal.Decimal('%.1f' % (bazaarsell)),"\n")
        if(int(quantità)>1024):
            print("quantità troppo elevata, ci potrebbe volere troppo per riceverlo","\n")
        if(bq=="0"):
            print("quantità per arrivare a", budget,": ", quantità,"\n")
        else:
            print("prezzo per arrivare a",quantità,": ", budget,"\n")
        print("minimo prezzo per vendere: ", decimal.Decimal('%.1f' % (minvendita)),"\n")
        print("taxes: ", decimal.Decimal('%.1f' % (tasse)),"\n")
        print("spesa totale: ", float(decimal.Decimal('%.1f' % (buytot))),"\n")
        if(bazaarguadagno > 0):
            print("guadagno totale: ", decimal.Decimal('%.1f' % (selltot)),"\n")
            print("guadagno effettivo: ", decimal.Decimal('%.1f' % (bazaarguadagno)),"\n")
        else:
            print("not stonks (", decimal.Decimal('%.1f' % (bazaarguadagno)),")","\n") 
    printbazaar()
    print("percentuale di guadagno rispetto al budget: ", decimal.Decimal('%.1f' % (percentuale)),"%")
    input()
    print("---------------------------------------------------------------\n")
    #### Printer ####
#### Bazaar Calculator ####
    #mammt prima era 430 righe, poi 340, poi 210, ora 170. ez
