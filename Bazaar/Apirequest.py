import requests


"""------------------------------------------------------------------------"""

#### API requester ####

golddata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_GOLD").json()
potatodata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_BAKED_POTATO").json()
sugarcanedata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_SUGAR_CANE").json()
glowstonedata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_GLOWSTONE_DUST").json()
catalystdata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=CATALYST").json()
lampdata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_REDSTONE_LAMP").json()
zombiedata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_ROTTEN_FLESH").json()
leatherdata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_ROTTEN_FLESH").json()
lapisdata = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=7dd8f258-dac1-489c-a673-20a7522619a6&productId=ENCHANTED_LAPIS_LAZULI").json()

#### API requester ####

"""------------------------------------------------------------------------"""

#### Bazaar data grabber ####

goldbuy = golddata["product_info"]["buy_summary"][0]["pricePerUnit"]
goldsell = golddata["product_info"]["sell_summary"][0]["pricePerUnit"]
potatobuy = potatodata["product_info"]["buy_summary"][0]["pricePerUnit"]
potatosell = potatodata["product_info"]["sell_summary"][0]["pricePerUnit"]
sugarcanebuy = sugarcanedata["product_info"]["buy_summary"][0]["pricePerUnit"]
sugarcanesell = sugarcanedata["product_info"]["sell_summary"][0]["pricePerUnit"]
glowstonebuy = glowstonedata["product_info"]["buy_summary"][0]["pricePerUnit"]
glowstonesell = glowstonedata["product_info"]["sell_summary"][0]["pricePerUnit"]
catalystbuy = catalystdata["product_info"]["buy_summary"][0]["pricePerUnit"]
catalystsell = catalystdata["product_info"]["sell_summary"][0]["pricePerUnit"]
lampbuy = lampdata["product_info"]["buy_summary"][0]["pricePerUnit"]
lampsell = lampdata["product_info"]["sell_summary"][0]["pricePerUnit"]
zombiebuy = zombiedata["product_info"]["buy_summary"][0]["pricePerUnit"]
zombiesell = zombiedata["product_info"]["sell_summary"][0]["pricePerUnit"]
leatherbuy = leatherdata["product_info"]["buy_summary"][0]["pricePerUnit"]
leathersell = leatherdata["product_info"]["sell_summary"][0]["pricePerUnit"]
lapisbuy = lapisdata["product_info"]["buy_summary"][0]["pricePerUnit"]
lapissell = lapisdata["product_info"]["sell_summary"][0]["pricePerUnit"]

#### Bazaar data grabber ####

"""------------------------------------------------------------------------"""

#### Best inizializator ####

bestgold = float(goldsell)-float(goldbuy)-float(goldsell)/100
bestpotato = float(potatosell)-float(potatobuy)-float(potatosell)/100
bestsugarcane = float(sugarcanesell)-float(sugarcanebuy)-float(sugarcanesell)/100
bestglowstone = float(glowstonesell)-float(glowstonebuy)-float(glowstonesell)/100
bestcatalyst = float(catalystsell)-float(catalystbuy)-float(catalystsell)/100
bestlamp = float(lampsell)-float(lampbuy)-float(lampsell)/100
bestzombie = float(zombiesell)-float(zombiebuy)-float(zombiesell)/100
bestleather = float(leathersell)-float(leatherbuy)-float(leathersell)/100
bestlapis = float(lapissell)-float(lapisbuy)-float(lapissell)/100
perc = [
        float(bestgold)/float(goldbuy)*100,
        float(bestpotato)/float(potatobuy)*100,
        float(bestsugarcane)/float(sugarcanebuy)*100,
        float(bestglowstone)/float(glowstonebuy)*100,
        float(bestcatalyst)/float(catalystbuy)*100,
        float(bestlamp)/float(lampbuy)*100,
        float(bestzombie)/float(zombiebuy)*100,
        float(bestleather)/float(leatherbuy)*100,
        float(bestlapis)/float(lapisbuy)*100,
        ]

#### Best inizializator ####

"""------------------------------------------------------------------------"""

#### Best chooser ####

def chooser():
    if(max(perc)==perc[0]):
        product = "E-Gold"
        bestproduct = golddata
    elif(max(perc)==perc[1]):
        product = "E-B-Potato"
        bestproduct = potatpdata
    elif(max(perc)==perc[2]):
        product = "E-Sugar-Cane"
        bestproduct = sugarcanedata
    elif(max(perc)==perc[3]):
        product = "E-Glowstone-Dust"
        bestproduct = glowstonedata
    elif(max(perc)==perc[4]):
        product = "E-Catalyst"
        bestproduct = catalystdata
    elif(max(perc)==perc[5]):
        product = "E-Redstone-Lamp"
        bestproduct = lampdata
    elif(max(perc)==perc[6]):
        product = "E-Rotten-Flesh"
        bestproduct = zombiedata
    elif(max(perc)==perc[7]):
        product = "E-Leather"
        bestproduct = leatherdata
    elif(max(perc)==perc[8]):
        product = "E-Lapis"
        bestproduct = lapisdata
    return product
bestproduct = chooser()

#### Best chooser ####

"""------------------------------------------------------------------------"""

#### Bazaar item data ####

def bazaardatabuy():
    bazaarHighetsPriceBuy = bestproduct["product_info"]["buy_summary"][0]["pricePerUnit"]
    return bestproductbuy

def bazaardatasell():
    bazaarLowestPriceSell = bestproduct["product_info"]["sell_summary"][0]["pricePerUnit"]
    return bestproductsell

#### Bazaar item data ####

