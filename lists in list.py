import math
food_name_list = []
price_list = []
price_pre_ozlist = []
unit_weight_list = []
amount_used_list = []
amount_used_price_list = []


item_num = 0
price_pre_oz = 0
amount_used_price = 0

def getitems():
    globals()
    global food_name_list, item_num, price_list, unit_weight, amount_used
    done = False
    while done == False:

        item =input('add item name or type done: ')

        if item == "done":
            done = True
            print("Your item list # is... ", item_num)
            print(' '.join(food_name_list))
            print(price_list)
            total= sum(price_list)
            print("Total is",total)
            math_price_pre_oz()

        else:
            food_name_list.append(item)
            item_num = item_num + 1
            price = int(float(input("Whats is price?: ")))
            price_list.append(price)
            unit_weight= int(float(input("whats the unit weight in oz?: ")))
            unit_weight_list.append(unit_weight)
            amount_used= int(float(input("how much did you use by weight in oz?: ")))
            amount_used_list.append(amount_used)



def math_price_pre_oz():
    globals()
    #global food_name_list, item_num, price_list, unit_weight, amount_used, price_pre_oz, price_pre_ozlist
    i = 0
    while i < item_num:
        price_pre_oz = price_list[i] / unit_weight_list[i]
        i = i + 1
        price_pre_ozlist.append(price_pre_oz)

    print("price or oz is list is...", price_pre_ozlist)
    math_price_of_meal()


def math_price_of_meal():
    globals()
    #global food_name_list, item_num, price_list, unit_weight, amount_used,amount_used_list, price_pre_oz, price_pre_ozlist, amount_used_price_list,amount_used_price
    i = 0
    while i < item_num:
        amount_used_price = price_pre_ozlist[i] * amount_used_list[i]
        i = i + 1
        amount_used_price_list.append(amount_used_price)
    print("amount used price list is", amount_used_price_list)
    lastsum()

def lastsum():
    globals()
    #global food_name_list, item_num, price_list, unit_weight, amount_used, amount_used_list, price_pre_oz, price_pre_ozlist, amount_used_price_list, amount_used_price
    last_sum = sum(amount_used_price_list)
    print(last_sum)


getitems()