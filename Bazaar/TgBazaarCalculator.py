from telethon import TelegramClient, events, Button
import logging
import requests
import decimal
import asyncio

print("Attendere... \n")
#### Lists inizializator ####
def Inizializator():
    global json
    global names
    global namesjson
    global products
    global itemsdata
    json = requests.get("https://api.hypixel.net/skyblock/bazaar?key=a7c61bba-d7ef-4049-8f42-bc53d6b8d747").json()
    namesjson = [
        ["ENCHANTED_OAK_LOG","ENCHANTED_SPRUCE_LOG","ENCHANTED_BIRCH_LOG","ENCHANTED_DARK_OAK_LOG","ENCHANTED_JUNGLE_LOG","ENCHANTED_ACACIA_LOG"],
        ["ENCHANTED_COBBLESTONE","ENCHANTED_COAL","ENCHANTED_IRON","ENCHANTED_GOLD","ENCHANTED_REDSTONE","ENCHANTED_LAPIS_LAZULI","ENCHANTED_DIAMOND","ENCHANTED_EMERALD","ENCHANTED_OBSIDIAN","ENCHANTED_FLINT","ENCHANTED_GLOWSTONE_DUST","ENCHANTED_ICE","ENCHANTED_QUARTZ","ENCHANTED_SNOW_BLOCK","ENCHANTED_MITHRIL","STARFALL","REFINED_TITANIUM"],
        ["JERRY_BOX_GREEN","JERRY_BOX_BLUE","JERRY_BOX_PURPLE","JERRY_BOX_GOLDEN"],
        ["ENCHANTED_BAKED_POTATO","ENCHANTED_GOLDEN_CARROT","ENCHANTED_SUGAR_CANE","ENCHANTED_COAL_BLOCK","ENCHANTED_GOLD_BLOCK","ENCHANTED_LAPIS_LAZULI_BLOCK","ENCHANTED_REDSTONE_BLOCK","ENCHANTED_GLOWSTONE","ENCHANTED_PACKED_ICE","ENCHANTED_BLAZE_ROD","ENCHANTED_REDSTONE_LAMP","SUPER_COMPACTOR_3000","SUMMONING_EYE","CATALYST","WHITE_GIFT","PURPLE_CANDY","ENCHANTED_GRILLED_PORK","REFINED_MINERAL","RECOMBOBULATOR_3000","BOOSTER_COOKIE","JACOBS_TICKET"],
        ["ENCHANTED_ROTTEN_FLESH","ENCHANTED_BONE","ENCHANTED_STRING","ENCHANTED_ENDER_PEARL","ENCHANTED_BLAZE_POWDER","GRIFFIN_FEATHER","ENCHANTED_ANCIENT_CLAW","ENCHANTED_SHARK_FIN","GREAT_WHITE_SHARK_TOOTH"],
        ["ENCHANTED_CARROT","ENCHANTED_POTATO","ENCHANTED_PUMPKIN","ENCHANTED_SUGAR","ENCHANTED_LEATHER","ENCHANTED_RABBIT_FOOT","ENCHANTED_RABBIT_HIDE","ENCHANTED_PORK","TIGHTLY_TIED_HAY_BALE","MUTANT_NETHER_STALK"],
        ["REVENANT_VISCERA","TARANTULA_SILK","WOLF_TOOTH","GOLDEN_TOOTH"],
    ]
    names = [
        ["Oak","Spruce","Birch","Dark oak","Jungle","Acacia"],
        ["Cobblestone","Coal","Iron","Gold","Redstone","Lapis","Diamond","Emerald","Obsidian","Flint","Glowstone","Ice","Quartz","Snow","Mithril","Starfall","Titanium"],
        ["Jerry green","Jerry blue","Jerry purple","Jerry gold"],
        ["Baked Potato","Golden Carrot","Sugar Cane","Coal Block","Gold Block","Lapis Block","Redstone Block","Glowstone Block","Packed Ice","Blaze Rod","Redstone Lamp","Compactor","Summoning Eye","Catalyst","White gift","Purple Candy","Grilled Pork","Refined Mineral","RECOMBOBULATOR","Booster Cookie","Ticket"],
        ["Rotten Flesh","Bone","String","Ender Pearl","Blaze Powder","Griffon","Claw","Shark Fin","White shark tooth"],
        ["Carrot","Potato","Pumpkin","Sugar","Leather","Rabbit Foot","Rabbit Hide","Pork","Hay Bale","Mutant Wart"],
        ["Viscera","Silk","Wolf Tooth","Golden Tooth"],
    ]
    products = []
    itemsdata = []
#### Lists iniziaalizator ####
#### Mammt Simulator ####
def BestCalculator(itemjson,item, n, b):
    percentage = []
    popolarità = []
    buy = []
    sell = []
    for i in range(len(itemjson)):
        buy.append(json["products"][itemjson[i]]["sell_summary"][0]["pricePerUnit"])
        sell.append(json["products"][itemjson[i]]["buy_summary"][0]["pricePerUnit"])
        popolarità.append(json["products"][itemjson[i]][])
        percentage.append(((float(sell[i])-float(buy[i])-float(sell[i])/100)/float(buy[i]))*100)
    for i in range(len(itemjson)):
        for j in range(len(itemjson)):
            if percentage[i]>percentage[j]:
                percentage[i],percentage[j] = percentage[j],percentage[i]
                itemjson[i] , itemjson[j] = itemjson[j] , itemjson[i]
                item[i] , item[j] = item[j] , item[i]
                buy[i] , buy[j] = buy[j] , buy[i]
                sell[i] , sell[j] = sell[j] , sell[i]
    if b:
        return ProfitList(item, buy, sell, percentage, popolarità)
    for i in range(n):
        itemsdata.append(itemjson[i])
        products.append(item[i])
#### Mammt Simulator ####
#### Price List ####
def ProfitList(products, buy, sell, percentage, popolarità):
    longarraystringlist = []
    arraystringlist = []
    for i in range(len(products)):
        longarraystringlist.append(str(i+1)+") "+str(products[i])+": buy("+str(buy[i])+") | sell("+str(sell[i])+") | "+str(decimal.Decimal('%.1f' % (percentage[i])))+"%")
        arraystringlist.append(str(i + 1) + ") " + str(products[i]) + " | "+str(popolarità) + " | " +str(decimal.Decimal('%.1f' % (percentage[i]))) + "%")
        #arraystringlist +=  popolarità ,"\n \n"
    return arraystringlist
#### Price List ####
#### Printer ####
def printBazaar(bazaarbuy, bazaarsell, bq, quantità, budget, minvendita, tasse, buytot,selltot, bazaarguadagno, percentuale):
    odionapoli = ""
    odionapoli += "\n**" + product + "**\ncompra a: " + str(decimal.Decimal('%.1f' % (bazaarbuy)))+"\nvendi a: " + str(decimal.Decimal('%.1f' % (bazaarsell)))+"\n"
    if int(quantità)>1024:
        odionapoli +="quantità troppo elevata, ci potrebbe volere molto tempo per riceverlo\n"
    if bq== "0":
        odionapoli +="quantità per arrivare a "+ budget+": "+ str(quantità)+"\n"
    else:
        odionapoli += "prezzo per arrivare a "+str(quantità)+": "+ budget+"\n"
    odionapoli += "minimo prezzo per vendere: "+ str(decimal.Decimal('%.1f' % (minvendita)))+"\ntasse: "+ str(decimal.Decimal('%.1f' % (tasse)))+"\nspesa totale: "+ str(decimal.Decimal('%.1f' % (buytot)))+"\n"
    if bazaarguadagno > 0:
        odionapoli += "guadagno totale: "+ str(decimal.Decimal('%.1f' % (selltot)))+"\nguadagno effettivo: "+ str(decimal.Decimal('%.1f' % (bazaarguadagno)))+"\n"
    else:
        odionapoli += "not stonks ("+ str(decimal.Decimal('%.1f' % (bazaarguadagno)))+")\n"
    odionapoli += "percentuale di guadagno rispetto al budget: "+ str(decimal.Decimal('%.1f' % (percentuale)))+"%"
    return odionapoli
#### Printer ####
#### Bazaar data grabber####
def bazaardatabuy(pjson):
    bazaarHighetsPriceBuy = json["products"][pjson]["sell_summary"][0]["pricePerUnit"]
    return bazaarHighetsPriceBuy
def bazaardatasell(pjson):
    bazaarLowestPriceSell = json["products"][pjson]["buy_summary"][0]["pricePerUnit"]
    return bazaarLowestPriceSell
#### Bazaar data grabber ####
#### Cat Calling ####
def Caller():
    Inizializator()
    listlen = [1,4,1,4,2,2,1]
    for i in range(len(names)):
        BestCalculator(namesjson[i],names[i],listlen[i],False)
    return BestCalculator(itemsdata, products, 0, True)
#### Cat Calling ####
#### Bazaar Calculator ####
def BazaarCalculator(numberchungus):
    productjson = itemsdata[numberchungus]
    global product
    product = products[numberchungus]
    budget = 2*(10**7)
    bazaarbuy = float(bazaardatabuy(productjson))+0.1
    bazaarsell = float(bazaardatasell(productjson))-0.1
    quantità = int(float(budget)/float(bazaarbuy))
    buytot = float(bazaarbuy)*float(quantità)
    selltot = float(bazaarsell)*float(quantità)
    tasse = float(selltot)/100
    bazaarguadagno = float(selltot) - float(buytot) - float(tasse)
    percentuale = float(bazaarguadagno)/float(budget)*100
    minvendita =  float(bazaarbuy) + float(bazaarbuy)/99
    if 10**3 < float(budget) < 10^6:
        budget = str(int(int(budget)/10**3))+"k"
    elif float(budget) > 10**6:
        budget = str(int(int(budget)/10**6))+"M"
    return printBazaar(bazaarbuy, bazaarsell, "0",quantità, budget, minvendita, tasse, buytot,selltot, bazaarguadagno, percentuale)
#### Bazaar Calculator ####
#### Telegram Jr ####
logging.basicConfig(level=logging.WARNING)
id = input("(my.telegram.org) inserisci api id: ")
hashid = input("(my.telegram.org) inserisci api hash id: ")
client = TelegramClient("CHOROMATSU",id,hashid)
print("in ascolto")

@client.on(events.NewMessage())
async def Cum(event):
    #In un FILE sarebbe meglio
    print(event.sender.id, "/", event.sender.username, "; sent: ",event.text)

@client.on(events.NewMessage(pattern="/bazaar"))
async def Bottoni(event):
    buttonlist=Caller()
    global keyboard
    keyboard = [
            [Button.inline(buttonlist[0],b"1")],[Button.inline(buttonlist[1],b"2")],
            [Button.inline(buttonlist[2],b"3")],[Button.inline(buttonlist[3],b"4")],
            [Button.inline(buttonlist[4],b"5")],[Button.inline(buttonlist[5],b"6")],
            [Button.inline(buttonlist[6],b"7")],[Button.inline(buttonlist[7],b"8")],
            [Button.inline(buttonlist[8],b"9")],[Button.inline(buttonlist[9],b"10")],
            [Button.inline(buttonlist[10],b"11")],[Button.inline(buttonlist[11],b"12")],
            [Button.inline(buttonlist[12],b"13")],[Button.inline(buttonlist[13],b"14")],
            [Button.inline(buttonlist[14],b"15")]
    ]
    try:
        await client.send_message(event.chat_id, "Scegli un prodotto: ", buttons=keyboard)
    except:
        m = await client.get_messages(-1001173018200,ids=11583)
        await client.send_message(event.chat_id,m)

@client.on(events.CallbackQuery)
async def BottonPress(event):
    for i in range(len(keyboard)):
        if event.data == str(i+1).encode("utf-8"):
            await event.edit(BazaarCalculator(i))

def main():
    client.start()
    client.run_until_disconnected()

if __name__ == "__main__":
    main()

#### Telegram Jr ####
#mammt prima era 430 righe, poi 340, poi 210, poi 170
