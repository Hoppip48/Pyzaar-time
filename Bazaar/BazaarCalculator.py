import requests
import decimal
    

while(True):
    print("\n \t \t \t \t Attendere...")
    #### Lists inizializator ####
    products = ["Wood","Ore1","Ore2","Ore3","Ore4","Jerry","Super1","Super2","Super3","Super4","Mob1","Mob2","Crop1","Crop2","Slayer"]
    itemsdata = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14"]
    percperc = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14"]
    best = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    perc = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    buy = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    sell = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    #### Lists iniziaalizator ####
    #### Best Wood ####
    print("\n \n \t \t \t Calculating Best Wood Type...")
    wood = ["0","1","2","3","4","5"]
    woodtypes = ["Oak","Spruce","Birch","Dark oak","Jungle","Acacia"]
    woodbuy = [0,1,2,3,4,5]
    woodsell = [0,1,2,3,4,5]
    woodlist = [0,1,2,3,4,5]
    wood[0] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_OAK_LOG").json()
    wood[1] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_SPRUCE_LOG").json()
    wood[2] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_BIRCH_LOG").json()
    wood[3] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_DARK_OAK_LOG").json()
    wood[4] =  requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_JUNGLE_LOG").json()
    wood[5] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_ACACIA_LOG").json()
    for i in range(len(wood)):
        woodbuy[i] = wood[i]["product_info"]["buy_summary"][0]["pricePerUnit"]
        woodsell[i] = wood[i]["product_info"]["sell_summary"][0]["pricePerUnit"]
        woodlist[i] = (float(woodsell[i])-float(woodbuy[i])-float(woodsell[i])/100)/float(woodbuy[i])*100
    for i in range(len(wood)):
        for j in range(len(wood)):
            if(woodlist[i]<woodlist[j]):
                bestwood = wood[j]
                products[0] = woodtypes[j]
    #### Best Wood ####
    #### Best Slayer ####
    print("\n \n \t \t \t Calculating Best Slayer Drop...")
    slayer = ["0","1","2","3","4","5"]
    slayertypes = ["Revenant Flesh","Viscera","Tarantula Web","Silk","Wolf Tooth","Golden Tooth"]
    slayerbuy = [0,1,2,3,4,5]
    slayersell = [0,1,2,3,4,5]
    slayerlist = [0,1,2,3,4,5]
    slayer[0] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=REVENANT_FLESH").json()
    slayer[1] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=REVENANT_VISCERA").json()
    slayer[2] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=TARANTULA_WEB").json()
    slayer[3] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=TARANTULA_SILK").json()
    slayer[4] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=WOLF_TOOTH").json()
    slayer[5] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=GOLDEN_TOOTH").json()
    for i in range(len(slayer)):
        slayerbuy[i] = slayer[i]["product_info"]["buy_summary"][0]["pricePerUnit"]
        slayersell[i] = slayer[i]["product_info"]["sell_summary"][0]["pricePerUnit"]
        slayerlist[i] = (float(slayersell[i])-float(slayerbuy[i])-float(slayersell[i])/100)/float(slayerbuy[i])*100
    for i in range(len(slayer)):
        for j in range(len(slayer)):
            if(slayerlist[i]<slayerlist[j]):
                bestslayer = slayer[j]
                products[14] = slayertypes[j]
    #### Best Slayer ####
    ####  Best Ores #####
    print("\n \n \t \t \t  Calculating Best 4 Ores...")
    Ores = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
    Oretypes = ["Cobblestone","Coal","Iron","Gold","Redstone","Lapis","Diamond","Emerald","Obsidian","Flint","Glowstone","Ice","Quartz","Snow","Mithril","Starfall","Titanium"]
    bestore = ["0","1","2","3"]
    orebuy = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    oresell = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    Orelist = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    Ores[0] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_COBBLESTONE").json()
    Ores[1] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_COAL").json()
    Ores[2] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_IRON").json()
    Ores[3] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_GOLD").json()
    Ores[4] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_REDSTONE").json()
    Ores[5] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_LAPIS_LAZULI").json()
    Ores[6] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_DIAMOND").json()
    Ores[7] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_EMERALD").json()
    Ores[8] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_OBSIDIAN").json()
    Ores[9] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_FLINT").json()
    Ores[10] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_GLOWSTONE_DUST").json()
    Ores[11] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_ICE").json()
    Ores[12] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_QUARTZ").json()
    Ores[13] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_SNOW_BLOCK").json()
    Ores[14] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=REFINED_MITHRIL").json()
    Ores[15] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=STARFALL").json()
    Ores[16] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=REFINED_TITANIUM").json()
    for i in range(len(Ores)):
        orebuy[i] = Ores[i]["product_info"]["buy_summary"][0]["pricePerUnit"]
        oresell[i] = Ores[i]["product_info"]["sell_summary"][0]["pricePerUnit"]
        Orelist[i] = (float(oresell[i])-float(orebuy[i])-float(oresell[i])/100)/float(orebuy[i])*100
    for i in range(len(Ores)):
        for j in range(len(Ores)):
            if(Orelist[i]>Orelist[j]):
                cumdemon = Ores[i]
                Ores[i] = Ores[j]
                Ores[j] = cumdemon
                x = Orelist[i]
                Orelist[i] = Orelist[j]
                Orelist[j] = x
                y = Oretypes[i]
                Oretypes[i] = Oretypes[j]
                Oretypes[j] = y
                z = orebuy[i]
                orebuy[i] = orebuy[j]
                orebuy[j] = z
                q = oresell[i]
                oresell[i] = oresell[j]
                oresell[j] = q
    for i in range(len(bestore)):
        bestore[i]=Ores[i]
        products[i+1]=Oretypes[i]
    #### Best Ores #####
    #### Best Crops ####
    print("\n \n \t \t \t  Calculating Best 2 Crops...")
    Crops = ["0","1","2","3","4","5","6","7","8","9"]
    Croptypes = ["Carrot","Potato","Pumpkin","Sugar","Leather","Rabbit Foot","Rabbit Hide","Pork","Nether Wart","Wheat"]
    bestcrop = ["0","1"]
    cropbuy = [0,1,2,3,4,5,6,7,8,9]
    cropsell = [0,1,2,3,4,5,6,7,8,9]
    croplist = [0,1,2,3,4,5,6,7,8,9]
    Crops[0] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_CARROT").json()  
    Crops[1] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_POTATO").json()
    Crops[2] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=POLISHED_PUMPKIN").json()
    Crops[3] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_SUGAR").json()
    Crops[4] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_LEATHER").json()    
    Crops[5] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_RABBIT_FOOT").json()
    Crops[6] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_RABBIT_HIDE").json()
    Crops[7] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_PORK").json()
    Crops[8] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=TIGHTLY_TIED_HAY_BALE").json()
    Crops[9] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=MUTANT_NETHER_STALK").json()
    for i in range(len(Crops)):
        cropbuy[i] = Crops[i]["product_info"]["buy_summary"][0]["pricePerUnit"]
        cropsell[i] = Crops[i]["product_info"]["sell_summary"][0]["pricePerUnit"]
        croplist[i] = (float(cropsell[i])-float(cropbuy[i])-float(cropsell[i])/100)/float(cropbuy[i])*100
    for i in range(len(Crops)):
        for j in range(len(Crops)):
            if(croplist[i]>croplist[j]):
                cumdemon = Crops[i]
                Crops[i] = Crops[j]
                Crops[j] = cumdemon
                x = croplist[i]
                croplist[i] = croplist[j]
                croplist[j] = x
                y = Croptypes[i]
                Croptypes[i] = Croptypes[j]
                Croptypes[j] = y
                z = cropbuy[i]
                cropbuy[i] = cropbuy[j]
                cropbuy[j] = z
                q = cropsell[i]
                cropsell[i] = cropsell[j]
                cropsell[j] = q
    for i in range(len(bestcrop)):
        bestcrop[i]=Crops[i]
        products[i+12]=Croptypes[i]
    #### Best Crops ####    
    ### Best Drops ####
    print("\n \n \t \t \t  Calculating Best 2 Drops...")
    Drops = ["0","1","2","3","4","5","6","7","8"]
    Droptypes = ["Rotten Flesh","Bone","String","Ender Pearl","Blaze Powder","Griffon","Claw","Shark Fin","White shark tooth"]
    bestdrop = ["0","1"]
    dropbuy = [0,1,2,3,4,5,6,7,8]
    dropsell = [0,1,2,3,4,5,6,7,8]
    droplist = [0,1,2,3,4,5,6,7,8]
    Drops[0] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_ROTTEN_FLESH").json()  
    Drops[1] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_BONE").json()
    Drops[2] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_STRING").json()
    Drops[3] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_ENDER_PEARL").json() 
    Drops[4] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_BLAZE_POWDER").json()
    Drops[5] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=GRIFFIN_FEATHER").json()
    Drops[6] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_ANCIENT_CLAW").json()
    Drops[7] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_SHARK_FIN").json()
    Drops[8] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=GREAT_WHITE_SHARK_TOOTH").json()
    for i in range(len(Drops)):
        dropbuy[i] = Drops[i]["product_info"]["buy_summary"][0]["pricePerUnit"]
        dropsell[i] = Drops[i]["product_info"]["sell_summary"][0]["pricePerUnit"]
        droplist[i] = (float(dropsell[i])-float(dropbuy[i])-float(dropsell[i])/100)/float(dropbuy[i])*100
    for i in range(len(Drops)):
        for j in range(len(Drops)):
            if(droplist[i]>droplist[j]):
                cumdemon = Drops[i]
                Drops[i] = Drops[j]
                Drops[j] = cumdemon
                x = droplist[i]
                droplist[i] = droplist[j]
                droplist[j] = x
                y = Droptypes[i]
                Droptypes[i] = Droptypes[j]
                Droptypes[j] = y
                z = dropbuy[i]
                dropbuy[i] = dropbuy[j]
                dropbuy[j] = z
                q = dropsell[i]
                dropsell[i] = dropsell[j]
                dropsell[j] = q
    for i in range(len(bestdrop)):
        bestdrop[i]=Drops[i]
        products[i+10]=Droptypes[i]
    #### Best Drops ####
    #### Best Jerry ####
    print("\n \n \t \t \tCalculating Best jerry...")
    jerrys = ["0","1","2","3"]
    jerrytypes = ["Jerry green","Jerry blue","Jerry purple","Jerry gold"]
    jerryjson = ["JERRY_BOX_GREEN","JERRY_BOX_BLUE","JERRY_BOX_PURPLE","JERRY_BOX_GOLDEN"]
    bestjerry = ["0"]
    jerrybuy = [0,1,2,3]
    jerrysell = [0,1,2,3]
    jerrylist = [0,1,2,3]
    for i in range(len(jerrys)):
        jerrys[i] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId="+jerryjson[i]).json()
    for i in range(len(jerrys)):
        jerrybuy[i] = jerrys[i]["product_info"]["buy_summary"][0]["pricePerUnit"]
        jerrysell[i] = jerrys[i]["product_info"]["sell_summary"][0]["pricePerUnit"]
        jerrylist[i] = (float(jerrysell[i])-float(jerrybuy[i])-float(jerrysell[i])/100)/float(jerrybuy[i])*100
    for i in range(len(jerrys)):
        for j in range(len(jerrys)):
            if(jerrylist[i]<jerrylist[j]):
                bestjerry = jerrys[j]
                products[5] = jerrytypes[j]  
    #### Best Jerry ####
    ### Best Super Enchanted ####
    print("\n \n \t \t \tCalculating Best 4 Other Items...")
    Supers = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","15","16","17"]
    Supertypes = ["Baked Potato","Golden Carrot","Sugar Cane","Coal Block","Gold Block","Lapis Block","Redstone Block","Glowstone Block","Packed Ice","Blaze Rod","Redstone Lamp","Compactor","Summoning Eye","Catalyst","White gift","Purple Candy","Grilled Pork","Refined Mineral","RECOMBOBULATOR","Booster Cookie","Ticket"]
    bestsuper = ["0","1","2","3"]
    superbuy = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    supersell = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,1718,19,20,21]
    Superlist = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,1718,19,20,21]
    supersjson = ["ENCHANTED_BAKED_POTATO","ENCHANTED_GOLDEN_CARROT","ENCHANTED_SUGAR_CANE","ENCHANTED_COAL_BLOCK","ENCHANTED_GOLD_BLOCK","ENCHANTED_LAPIS_LAZULI_BLOCK","ENCHANTED_REDSTONE_BLOCK","ENCHANTED_GLOWSTONE","ENCHANTED_PACKED_ICE","ENCHANTED_BLAZE_ROD","ENCHANTED_REDSTONE_LAMP","SUPER_COMPACTOR_3000","SUMMONING_EYE","CATALYST","WHITE_GIFT","PURPLE_CANDY","ENCHANTED_GRILLED_PORK","REFINED_MINERAL","RECOMBOBULATOR_3000","BOOSTER_COOKIE","JACOBS_TICKET"]   
    for i in range(len(Supers)):
        Supers[i] = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId="+supersjson[i]).json()
    for i in range(len(Supers)):
        superbuy[i] = Supers[i]["product_info"]["buy_summary"][0]["pricePerUnit"]
        supersell[i] = Supers[i]["product_info"]["sell_summary"][0]["pricePerUnit"]
        Superlist[i] = (float(supersell[i])-float(superbuy[i])-float(supersell[i])/100)/float(superbuy[i])*100
    for i in range(len(Supers)):
        for j in range(len(Supers)):
            if(Superlist[i]>Superlist[j]):
                cumdemon = Supers[i]
                Supers[i] = Supers[j]
                Supers[j] = cumdemon
                x = Superlist[i]
                Superlist[i] = Superlist[j]
                Superlist[j] = x
                y = Supertypes[i]
                Supertypes[i] = Supertypes[j]
                Supertypes[j] = y
                z = superbuy[i]
                superbuy[i] = superbuy[j]
                superbuy[j] = z
                q = supersell[i]
                supersell[i] = supersell[j]
                supersell[j] = q
    for i in range(4):
        bestsuper[i]=Supers[i]
        products[i+6]=Supertypes[i]
    #### Best Super Enchanted ####
    #### Api requester ####
    print("\n \n \t \t \t  Extracting Data From Hypixel API... \n \n")
    itemsdata[0] = bestwood
    itemsdata[1] = bestore[0]
    itemsdata[2] = bestore[1]
    itemsdata[3] = bestore[2]
    itemsdata[4] = bestore[3]
    itemsdata[5] = bestjerry
    itemsdata[6] = bestsuper[0]
    itemsdata[7] = bestsuper[1]
    itemsdata[8] = bestsuper[2]
    itemsdata[9] = bestsuper[3]
    itemsdata[10] = bestdrop[0]
    itemsdata[11] = bestdrop[1]
    itemsdata[12] = bestcrop[0]
    itemsdata[13] = bestcrop[1]
    itemsdata[14] = bestslayer
    #### API requester ####
    #### Bazaar data grabber ####
    for i in range(len(itemsdata)):
        buy[i] = itemsdata[i]["product_info"]["buy_summary"][0]["pricePerUnit"]
        sell[i] = itemsdata[i]["product_info"]["sell_summary"][0]["pricePerUnit"]
    #### Bazaar data grabber ####
    #### Best inizializator ####
    for i in range(len(itemsdata)):
        best[i] = float(sell[i])-float(buy[i])-float(sell[i])/100
        perc[i] = float(best[i])/float(buy[i])*100
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
    def ProfitList():
        for i in range(len(itemsdata)):
            percperc[i] = decimal.Decimal('%.1f' % (perc[i]))
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
            arraystringlist += str(percperc[i])
            arraystringlist += "% \n \n"
        return arraystringlist
    print(ProfitList())
    #### Price List ####
    #### itemchooser ####
    numberchungus = int(input("choose item number: "))-1    
    if(numberchungus == -1):
        print("\n---------------------------------------------------------------\n")
        continue
    yourproduct = itemsdata[0]
    yproduct = products[0]
    for i in range(len(itemsdata)):
        if(int(numberchungus)==i):
            yproduct = products[i]
            yourproduct = itemsdata[i]
    print("product choosen: ",yproduct,"\n")
    finalproduct=yourproduct
    #### itemchooser ####
    #### Bazaar item data ####
    def bazaardatabuy():
        bazaarHighetsPriceBuy = finalproduct["product_info"]["buy_summary"][0]["pricePerUnit"]
        return bazaarHighetsPriceBuy
    def bazaardatasell():
        bazaarLowestPriceSell = finalproduct["product_info"]["sell_summary"][0]["pricePerUnit"]
        return bazaarLowestPriceSell
    #### Bazaar item data ####
####Bazaar Calculator ####
    #### Variables ####
    bazaardatasell()
    bq = input("insert budget/quantity (0/1): ")
    if(bq == "0"):  
        budget = input("Enter budget: ")
        if(budget == "0"):  
            budget = 2.5*(10**7)
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
#### Bazaar Calculator ####
