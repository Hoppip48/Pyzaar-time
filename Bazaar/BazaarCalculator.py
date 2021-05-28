import requests
import decimal
    


while(True):
    print("\n \t \t \t \t Attendere...")
    #### Lists inizializator ####
    json = requests.get("https://api.hypixel.net/skyblock/bazaar?key=a7c61bba-d7ef-4049-8f42-bc53d6b8d747").json()
    woodjson = ["ENCHANTED_OAK_LOG","ENCHANTED_SPRUCE_LOG","ENCHANTED_BIRCH_LOG","ENCHANTED_DARK_OAK_LOG","ENCHANTED_JUNGLE_LOG","ENCHANTED_ACACIA_LOG"]
    orejson = ["ENCHANTED_COBBLESTONE","ENCHANTED_COAL","ENCHANTED_IRON","ENCHANTED_GOLD","ENCHANTED_REDSTONE","ENCHANTED_LAPIS_LAZULI","ENCHANTED_DIAMOND","ENCHANTED_EMERALD","ENCHANTED_OBSIDIAN","ENCHANTED_FLINT","ENCHANTED_GLOWSTONE_DUST","ENCHANTED_ICE","ENCHANTED_QUARTZ","ENCHANTED_SNOW_BLOCK","ENCHANTED_MITHRIL","STARFALL","REFINED_TITANIUM"]
    jerryjson = ["JERRY_BOX_GREEN","JERRY_BOX_BLUE","JERRY_BOX_PURPLE","JERRY_BOX_GOLDEN"]
    superjson = ["ENCHANTED_BAKED_POTATO","ENCHANTED_GOLDEN_CARROT","ENCHANTED_SUGAR_CANE","ENCHANTED_COAL_BLOCK","ENCHANTED_GOLD_BLOCK","ENCHANTED_LAPIS_LAZULI_BLOCK","ENCHANTED_REDSTONE_BLOCK","ENCHANTED_GLOWSTONE","ENCHANTED_PACKED_ICE","ENCHANTED_BLAZE_ROD","ENCHANTED_REDSTONE_LAMP","SUPER_COMPACTOR_3000","SUMMONING_EYE","CATALYST","WHITE_GIFT","PURPLE_CANDY","ENCHANTED_GRILLED_PORK","REFINED_MINERAL","RECOMBOBULATOR_3000","BOOSTER_COOKIE","JACOBS_TICKET"]
    dropjson = ["ENCHANTED_ROTTEN_FLESH","ENCHANTED_BONE","ENCHANTED_STRING","ENCHANTED_ENDER_PEARL","ENCHANTED_BLAZE_POWDER","GRIFFIN_FEATHER","ENCHANTED_ANCIENT_CLAW","ENCHANTED_SHARK_FIN","GREAT_WHITE_SHARK_TOOTH"]
    cropjson = ["ENCHANTED_CARROT","ENCHANTED_POTATO","ENCHANTED_PUMPKIN","ENCHANTED_SUGAR","ENCHANTED_LEATHER","ENCHANTED_RABBIT_FOOT","ENCHANTED_RABBIT_HIDE","ENCHANTED_PORK","TIGHTLY_TIED_HAY_BALE","MUTANT_NETHER_STALK"]
    slayerjson = ["REVENANT_VISCERA","TARANTULA_SILK","WOLF_TOOTH","GOLDEN_TOOTH"]
    wood = ["Oak","Spruce","Birch","Dark oak","Jungle","Acacia"]
    ores = ["Cobblestone","Coal","Iron","Gold","Redstone","Lapis","Diamond","Emerald","Obsidian","Flint","Glowstone","Ice","Quartz","Snow","Mithril","Starfall","Titanium"]
    jerrys = ["Jerry green","Jerry blue","Jerry purple","Jerry gold"]
    supers = ["Baked Potato","Golden Carrot","Sugar Cane","Coal Block","Gold Block","Lapis Block","Redstone Block","Glowstone Block","Packed Ice","Blaze Rod","Redstone Lamp","Compactor","Summoning Eye","Catalyst","White gift","Purple Candy","Grilled Pork","Refined Mineral","RECOMBOBULATOR","Booster Cookie","Ticket"]     
    drops = ["Rotten Flesh","Bone","String","Ender Pearl","Blaze Powder","Griffon","Claw","Shark Fin","White shark tooth"]
    crops = ["Carrot","Potato","Pumpkin","Sugar","Leather","Rabbit Foot","Rabbit Hide","Pork","Nether Wart","Wheat"]
    slayer = ["Viscera","Silk","Wolf Tooth","Golden Tooth"]
    ### Empty ###
    products = []
    itemsdata = []
    best = []
    perc = []
    buy = []
    sell = []   
    woodbuy = []
    woodsell = []
    woodlist = []        
    orebuy = []
    oresell = []
    orelist = []
    jerrybuy = []
    jerrysell = []
    jerrylist = []        
    superbuy = []
    supersell = []
    superlist = []
    dropbuy = []
    dropsell = []
    droplist = []
    cropbuy = []
    cropsell = []
    croplist = []
    slayerbuy = []
    slayersell = []
    slayerlist = []
    ### Empty ###
    #### Lists iniziaalizator ####
    #### Best Wood ####
    print("\n \n \t \t \t Calculating Best Wood Type...")
    for i in range(len(wood)):
        woodbuy.append(json["products"][woodjson[i]]["sell_summary"][0]["pricePerUnit"])
        woodsell.append(json["products"][woodjson[i]]["buy_summary"][0]["pricePerUnit"])
        woodlist.append((float(woodsell[i])-float(woodbuy[i])-float(woodsell[i])/100)/float(woodbuy[i])*100)
    for i in range(len(wood)):
        for j in range(len(wood)):
            if(woodlist[i]>woodlist[j]):
                ez = woodlist[j]
                woodlist[j] = woodlist[i]
                woodlist[i] = ez
                ez = woodjson[j]
                woodjson[j] = woodjson[i]
                woodjson[i] = ez
                ez = wood[j]
                wood[j] = wood[i]
                wood[i] = ez
    itemsdata.append(woodjson[0])
    products.append(wood[0])
    #### Best Wood ###
    ####  Best Ores #####
    print("\n \n \t \t \t  Calculating Best 4 Ores...")
    for i in range(len(ores)):
        orebuy.append(json["products"][orejson[i]]["sell_summary"][0]["pricePerUnit"])
        oresell.append(json["products"][orejson[i]]["buy_summary"][0]["pricePerUnit"])
        orelist.append((float(oresell[i])-float(orebuy[i])-float(oresell[i])/100)/float(orebuy[i])*100) 
    for i in range(len(ores)):
        for j in range(len(ores)):
            if(orelist[i]>orelist[j]):
                cumdemon = ores[i]
                ores[i] = ores[j]
                ores[j] = cumdemon
                x = orelist[i]
                orelist[i] = orelist[j]
                orelist[j] = x
                y = orejson[i]
                orejson[i] = orejson[j]
                orejson[j] = y
    for i in range(4):
        itemsdata.append(orejson[i])
        products.append(ores[i])
    #### Best Ores #####
    #### Best Jerry ####
    print("\n \n \t \t \tCalculating Best jerry...")
    for i in range(len(jerrys)):
        jerrybuy.append(json["products"][jerryjson[i]]["sell_summary"][0]["pricePerUnit"])
        jerrysell.append(json["products"][jerryjson[i]]["buy_summary"][0]["pricePerUnit"])
        jerrylist.append((float(jerrysell[i])-float(jerrybuy[i])-float(jerrysell[i])/100)/float(jerrybuy[i])*100)
    for i in range(len(jerrys)):
        for j in range(len(jerrys)):
            if(jerrylist[i]>jerrylist[j]):
                ez = jerrylist[j]
                jerrylist[j] = jerrylist[i]
                jerrylist[i] = ez
                ez = jerryjson[j]
                jerryjson[j] = jerryjson[i]
                jerryjson[i] = ez
                ez = jerrys[j]
                jerrys[j] = jerrys[i]
                jerrys[i] = ez
    itemsdata.append(jerryjson[0])
    products.append(jerrys[0])  
    #### Best Jerry ####
    ### Best Super Enchanted ####
    print("\n \n \t \t \tCalculating Best 4 Other Items...")
    for i in range(len(supers)):
        superbuy.append(json["products"][superjson[i]]["sell_summary"][0]["pricePerUnit"])
        supersell.append(json["products"][superjson[i]]["buy_summary"][0]["pricePerUnit"])
        superlist.append((float(supersell[i])-float(superbuy[i])-float(supersell[i])/100)/float(superbuy[i])*100)
    for i in range(len(supers)):
        for j in range(len(supers)):
            if(superlist[i]>superlist[j]):
                cumdemon = supers[i]
                supers[i] = supers[j]
                supers[j] = cumdemon
                x = superlist[i]
                superlist[i] = superlist[j]
                superlist[j] = x
                y = superjson[i]
                superjson[i] = superjson[j]
                superjson[j] = y
    for i in range(4):
        itemsdata.append(superjson[i])
        products.append(supers[i])
    #### Best Super Enchanted ####
    ### Best Drops ####
    print("\n \n \t \t \t  Calculating Best 2 Drops...")
    for i in range(len(drops)):
        dropbuy.append(json["products"][dropjson[i]]["sell_summary"][0]["pricePerUnit"])
        dropsell.append(json["products"][dropjson[i]]["buy_summary"][0]["pricePerUnit"])
        droplist.append((float(dropsell[i])-float(dropbuy[i])-float(dropsell[i])/100)/float(dropbuy[i])*100)
    for i in range(len(drops)):
        for j in range(len(drops)):
            if(droplist[i]>droplist[j]):
                cumdemon = drops[i]
                drops[i] = drops[j]
                drops[j] = cumdemon
                x = droplist[i]
                droplist[i] = droplist[j]
                droplist[j] = x
                y = dropjson[i]
                dropjson[i] = dropjson[j]
                dropjson[j] = y
    for i in range(2):
        itemsdata.append(dropjson[i])
        products.append(drops[i])
    #### Best Drops ####
    #### Best Crops ####
    print("\n \n \t \t \t  Calculating Best 2 Crops...")
    for i in range(len(crops)):
        cropbuy.append(json["products"][cropjson[i]]["sell_summary"][0]["pricePerUnit"])
        cropsell.append(json["products"][cropjson[i]]["buy_summary"][0]["pricePerUnit"])
        croplist.append((float(cropsell[i])-float(cropbuy[i])-float(cropsell[i])/100)/float(cropbuy[i])*100)
    for i in range(len(crops)):
        for j in range(len(crops)):
            if(croplist[i]>croplist[j]):
                cumdemon = crops[i]
                crops[i] = crops[j]
                crops[j] = cumdemon
                x = croplist[i]
                croplist[i] = croplist[j]
                croplist[j] = x
                y = cropjson[i]
                cropjson[i] = cropjson[j]
                cropjson[j] = y
    for i in range(2):
        itemsdata.append(cropjson[i])
        products.append(crops[i])
    #### Best Crops ####    
    #### Best Slayer ####
    print("\n \n \t \t \t Calculating Best Slayer Drop... \n \n")
    for i in range(len(slayer)):
        slayerbuy.append(json["products"][slayerjson[i]]["sell_summary"][0]["pricePerUnit"])
        slayersell.append(json["products"][slayerjson[i]]["buy_summary"][0]["pricePerUnit"])
        slayerlist.append((float(slayersell[i])-float(slayerbuy[i])-float(slayersell[i])/100)/float(slayerbuy[i])*100)
    for i in range(len(slayer)):
        for j in range(len(slayer)):
            if(slayerlist[i]>slayerlist[j]):
                cumdemon = slayer[i]
                slayer[i] = slayer[j]
                slayer[j] = cumdemon
                x = slayerlist[i]
                slayerlist[i] = slayerlist[j]
                slayerlist[j] = x
                y = slayerjson[i]
                slayerjson[i] = slayerjson[j]
                slayerjson[j] = y
    itemsdata.append(slayerjson[0])
    products.append(slayer[0])
    #### Best Slayer ####
    #### Bazaar data grabber ####
    for i in range(len(itemsdata)):
        buy.append(json["products"][itemsdata[i]]["sell_summary"][0]["pricePerUnit"])
        sell.append(json["products"][itemsdata[i]]["buy_summary"][0]["pricePerUnit"])
    #### Bazaar data grabber ####
    #### Best inizializator ####
    for i in range(len(itemsdata)):
        best.append(float(sell[i])-float(buy[i])-float(sell[i])/100)
        perc.append(float(best[i])/float(buy[i])*100)
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
            arraystringlist += " : "
            arraystringlist += "buy("
            arraystringlist += str(buy[i])
            arraystringlist += ") : "
            arraystringlist += "sell("
            arraystringlist += str(sell[i])
            arraystringlist += ") : "
            arraystringlist += str(perc[i])
            arraystringlist += "% \n \n"
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
            print("buy price: ", decimalbuy)
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
    #mammt prima era 430 righe
#### Bazaar Calculator ####
