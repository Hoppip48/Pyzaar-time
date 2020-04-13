import requests

#### API requests ####

hypixelParams = {
    "key": "7dd8f258-dac1-489c-a673-20a7522619a6",
    "productId": "ENCHANTED_REDSTONE_BLOCK"
}
hypixelbazardata = requests.get("https://api.hypixel.net/skyblock/bazaar/product", hypixelParams).json()

#### API requests ####

"""------------------------------------------------------------------------"""


#### Bazaar item data ####

def bazaardatabuy():
    bazaarHighetsPriceBuy = hypixelbazardata["product_info"]["buy_summary"][0]["pricePerUnit"]
    return bazaarHighetsPriceBuy

def bazaardatasell():
    bazaarLowestPriceSell = hypixelbazardata["product_info"]["sell_summary"][0]["pricePerUnit"]
    return bazaarLowestPriceSell

#### Bazaar item data ####
