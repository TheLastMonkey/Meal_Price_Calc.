import math
import os

list_o_dicts = []

item_dic = {}
loop_count = 0
x = True
c = 0
total = float(0)

os.system("clear")

def last_print():

    print('Number of Items is',loop_count)
    print('Total is', '${:,.2f}'.format(total))  # USD cash format


    #  print('${:,.2f}'.format(list_o_dicts[0]['item_cost_total']))


    stuff = {'mystuff': 'MY SHIT', 'yourshit': 'YOUR SHIT'}
    #  dict unpacking. ez to read and small
    print('see cuz {mystuff} is my shit and {yourshit} is your shit'.format(**stuff))

def list_print_loop():
    global c, loop_count, list_o_dicts, total
    c = 0
    total = float(0)
    while c < len(list_o_dicts):

        #  BAD fomating #  print("{}   {}{}   amount {}    per oz {}
        # total for item ${} ".format(list_o_dicts[c]['name'], '$', list_o_dicts[c]['cost'],
        # list_o_dicts[c]['amount'], list_o_dicts[c]['cost_per_oz'],list_o_dicts[c]['item_cost_total']))

        #  the right way...  #
        print('{0[name]}           {1}{0[cost]}   amount {0[amount]}    per oz {3:,.4f}'
              '     total for item ${2:,.2f} '.format(list_o_dicts[c], '$',list_o_dicts[c]['item_cost_total'],list_o_dicts[c]['cost_per_oz']))

        total += list_o_dicts[c]['item_cost_total']
        c += 1
        print()

def main():

    global x, c, item_dic, total, list_o_dicts, loop_count
    while x is True:

        item_dic['name'] = input('Name?')
        try:
            item_dic['cost'] = float(input('Cost?'))
        except ValueError as e:
            print(e)
            print('thats not a number dumb-dumb')
            break
            
        try:
            item_dic['amount'] = float(input('Unit Amount?'))
        except ValueError as e:
            print(e)
            print('thats not a number dumb-dumb')
            break
        try:
            item_dic['amount_used'] = float(input('Amount Used?'))
        except ValueError as e:
            print(e)
            print('thats not a number dumb-dumb')
            break
        # do meth
        item_dic['cost_per_oz'] = item_dic['cost'] / item_dic['amount']
        item_dic['item_cost_total'] = item_dic['cost_per_oz'] * item_dic['amount_used']

        list_o_dicts.append(dict(item_dic))        # .append(dict(the dict))  INPRORTAN  !!!
        loop_count += 1
        add_more = input('add more Y/N')
        if add_more == 'y':

            pass

        else:
            x = False
            os.system("clear")
            print('Your Meal'.center(80, '_'))
            print()
            list_print_loop()
            # print(list_o_dicts)

main()

last_print()
#print(item_dic)
#
#for key in item_dic.keys():
#    value = item_dic[key]
#    print(key, value)


# print(list_o_dicts)

# print(list_o_dicts[0]['name'],'$',list_o_dicts[0]['cost'],list_o_dicts[0]['amount'])  # how to get the data out of the list of dicts







