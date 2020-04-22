import requests
import decimal

"""------------------------------------------------------------------------"""

#### API requester ####

golddata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_GOLD").json()
goldblockdata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_GOLD_BLOCK").json()
potatodata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_BAKED_POTATO").json()
sugarcanedata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_SUGAR_CANE").json()
glowstonedata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_GLOWSTONE_DUST").json()
glowstoneblockdata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_GLOWSTONE").json()
catalystdata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=CATALYST").json()
lampdata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_REDSTONE_LAMP").json()
zombiedata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_ROTTEN_FLESH").json()
leatherdata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_ROTTEN_FLESH").json()
flintdata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_FLINT").json()
lapisdata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_LAPIS_LAZULI").json()
lapisblockdata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_LAPIS_LAZULI_BLOCK").json()

#### API requester ####

"""------------------------------------------------------------------------"""

#### Bazaar data grabber ####

buy = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
sell = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
buy[0] = golddata["product_info"]["buy_summary"][0]["pricePerUnit"]
sell[0] = golddata["product_info"]["sell_summary"][0]["pricePerUnit"]
buy[1] = goldblockdata["product_info"]["buy_summary"][0]["pricePerUnit"]
sell[1] = goldblockdata["product_info"]["sell_summary"][0]["pricePerUnit"]
buy[2] = potatodata["product_info"]["buy_summary"][0]["pricePerUnit"]
sell[2] = potatodata["product_info"]["sell_summary"][0]["pricePerUnit"]
buy[3] = sugarcanedata["product_info"]["buy_summary"][0]["pricePerUnit"]
sell[3] = sugarcanedata["product_info"]["sell_summary"][0]["pricePerUnit"]
buy[4] = glowstonedata["product_info"]["buy_summary"][0]["pricePerUnit"]
sell[4] = glowstonedata["product_info"]["sell_summary"][0]["pricePerUnit"]
buy[5] = glowstoneblockdata["product_info"]["buy_summary"][0]["pricePerUnit"]
sell[5] = glowstoneblockdata["product_info"]["sell_summary"][0]["pricePerUnit"]
buy[6] = catalystdata["product_info"]["buy_summary"][0]["pricePerUnit"]
sell[6] = catalystdata["product_info"]["sell_summary"][0]["pricePerUnit"]
buy[7] = lampdata["product_info"]["buy_summary"][0]["pricePerUnit"]
sell[7] = lampdata["product_info"]["sell_summary"][0]["pricePerUnit"]
buy[8] = zombiedata["product_info"]["buy_summary"][0]["pricePerUnit"]
sell[8] = zombiedata["product_info"]["sell_summary"][0]["pricePerUnit"]
buy[9] = leatherdata["product_info"]["buy_summary"][0]["pricePerUnit"]
sell[9] = leatherdata["product_info"]["sell_summary"][0]["pricePerUnit"]
buy[10] = flintdata["product_info"]["buy_summary"][0]["pricePerUnit"]
sell[10] = flintdata["product_info"]["sell_summary"][0]["pricePerUnit"]
buy[11] = lapisdata["product_info"]["buy_summary"][0]["pricePerUnit"]
sell[11] = lapisdata["product_info"]["sell_summary"][0]["pricePerUnit"]
buy[12] = lapisblockdata["product_info"]["buy_summary"][0]["pricePerUnit"]
sell[12] = lapisblockdata["product_info"]["sell_summary"][0]["pricePerUnit"]

#### Bazaar data grabber ####

"""------------------------------------------------------------------------"""

#### Best inizializator ####

best = [0,1,2,3,4,5,6,7,8,9,10,11,12]
best[0] = float(sell[0])-float(buy[0])-float(sell[0])/100
best[1] = float(sell[1])-float(buy[1])-float(sell[1])/100
best[2] = float(sell[2])-float(buy[2])-float(sell[2])/100
best[3] = float(sell[3])-float(buy[3])-float(sell[3])/100
best[4] = float(sell[4])-float(buy[4])-float(sell[4])/100
best[5] = float(sell[5])-float(buy[5])-float(sell[5])/100
best[6] = float(sell[6])-float(buy[6])-float(sell[6])/100
best[7] = float(sell[7])-float(buy[7])-float(sell[7])/100
best[8] = float(sell[8])-float(buy[8])-float(sell[8])/100
best[9] = float(sell[9])-float(buy[9])-float(sell[9])/100
best[10] = float(sell[10])-float(buy[10])-float(sell[10])/100
best[11] = float(sell[11])-float(buy[11])-float(sell[11])/100
best[12] = float(sell[12])-float(buy[12])-float(sell[12])/100
perc = [
        float(best[0])/float(buy[0])*100,
        float(best[1])/float(buy[1])*100,
        float(best[2])/float(buy[2])*100,
        float(best[3])/float(buy[3])*100,
        float(best[4])/float(buy[4])*100,
        float(best[5])/float(buy[5])*100,
        float(best[6])/float(buy[6])*100,
        float(best[7])/float(buy[7])*100,
        float(best[8])/float(buy[8])*100,
        float(best[9])/float(buy[9])*100,
        float(best[10])/float(buy[10])*100,
        float(best[11])/float(buy[11])*100,
        float(best[12])/float(buy[12])*100
        ]

#### Best inizializator ####

"""------------------------------------------------------------------------"""

#### Best chooser ####

product = ""
if(max(perc)==perc[0]):
    product = "Gold"
    bestproduct = golddata
elif(max(perc)==perc[1]):
    product = "Gold Block"
    bestproduct = goldblockdata
elif(max(perc)==perc[2]):
    product = "Potato"
    bestproduct = potatodata
elif(max(perc)==perc[3]):
    product = "Sugar Cane"
    bestproduct = sugarcanedata
elif(max(perc)==perc[4]):
    product = "Glowstone"
    bestproduct = glowstonedata
elif(max(perc)==perc[5]):
    bestproduct = glowstoneblockdata
elif(max(perc)==perc[6]):
    product = "Catalyst"
    bestproduct = catalystdata
elif(max(perc)==perc[7]):
    product = "Redstone Lamp"
    bestproduct = lampdata
elif(max(perc)==perc[8]):
    product = "Rotten Flesh"
    bestproduct = zombiedata
elif(max(perc)==perc[9]):
    product = "Leather"
    bestproduct = leatherdata
elif(max(perc)==perc[10]):
    product = "Flint"
    bestproduct = flintdata
elif(max(perc)==perc[11]):
     product = "Lapis"
     bestproduct = lapisdata
elif(max(perc)==perc[12]):
    product = "Lapis Block"
    bestproduct = lapisblockdata
print("Best item: ", product,"\n")

#### Best chooser ####

"""------------------------------------------------------------------------"""

#### Price List ####

def ProfitList():
    productlist = [
        "gold",
        "gold block",
        "baked potato",
        "sugarcane",
        "glowstone dust",
        "glowstone block",
        "catalyst",
        "lamp",
        "zombie",
        "leather",
        "flint",
        "lapis",
        "lapis block"
        ]
    percperc = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
    for i in range(13):
        percperc[i] = decimal.Decimal('%.1f' % (perc[i]))
    arraystringlist = ""
    for i in range(13):
        arraystringlist += str(i+1)
        arraystringlist += ") "
        arraystringlist += str(productlist[i])
        arraystringlist += " : "
        arraystringlist += "buy("
        arraystringlist += str(buy[i])
        arraystringlist += ") : "
        arraystringlist += "sell("
        arraystringlist += str(sell[i])
        arraystringlist += ") : "
        arraystringlist += str(percperc[i])
        arraystringlist += "% \n \n"
    print(arraystringlist)
    return arraystringlist
ProfitList()

#### Price List ####

"""------------------------------------------------------------------------"""

#### itemchooser ####

def itemchooser():
    numberchungus = int(input("choose item number: "))-1
    yourproduct = bestproduct
    yproduct = product
    if(int(numberchungus)==0):
        yproduct = "Gold"
        yourporoduct = golddata
    elif(int(numberchungus)==1):
        yproduct = "Gold Block"
        yourproduct = goldblockdata
    elif(int(numberchungus)==2):
        yproduct = "Potato"
        yourproduct = potatodata
    elif(int(numberchungus)==3):
        yproduct = "Sugar Cane"
        yourproduct = sugarcanedata
    elif(int(numberchungus)==4):
        yproduct = "Glowstone Dust"
        yourproduct = glowstonedata
    elif(int(numberchungus)==5):
        yproduct = "Glowstone Block"
        yourproduct = glowstoneblockdata
    elif(int(numberchungus)==6):
        yproduct = "Catalyst"
        yourproduct = catalystdata
    elif(int(numberchungus)==7):
        yproduct = "Redstone Lamp"
        yourproduct = lampdata
    elif(int(numberchungus)==8):
        yproduct = "Rotten Flesh"
        yourproduct = zombiedata
    elif(int(numberchungus)==9):
        yproduct = "Leather"
        yourproduct = leatherdata
    elif(int(numberchungus)==10):
        yproduct = "Flint"
        yourproduct = flintdata
    elif(int(numberchungus)==11):
        yproduct = "Lapis"
        yourproduct = lapisdata
    elif(int(numberchungus)==12):
        yproduct = "Lapis Block"
        yourproduct = lapisblockdata
    print("product choosen: ",yproduct,"\n")
    return yourproduct
finalproduct = itemchooser()

#### itemchooser ####

"""------------------------------------------------------------------------"""

#### Bazaar item data ####

def bazaardatabuy():
    bazaarHighetsPriceBuy = finalproduct["product_info"]["buy_summary"][0]["pricePerUnit"]
    return bazaarHighetsPriceBuy

def bazaardatasell():
    bazaarLowestPriceSell = finalproduct["product_info"]["sell_summary"][0]["pricePerUnit"]
    return bazaarLowestPriceSell

#### Bazaar item data ####

