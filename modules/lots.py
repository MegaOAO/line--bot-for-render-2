from random import choice

def get_lots():
    lots_list = []
    lots = ["大吉","吉","中吉","小吉","小兇","兇","大凶"]
    for t in ["table"]:
        x = choice (lots)
        lots_list.append(x)
        break
    return lots_list