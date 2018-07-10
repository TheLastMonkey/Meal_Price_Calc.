#!/usr/bin/env python3

import os
import time

'''setup'''
os.system("clear")
item_list = []
total = 0


class Item:
    '''Get item data and do a little math'''
    def __init__(self, name, cost, amount_as_sold, amount_used):
        self.name = name
        self.cost = cost
        self.amount_as_sold = amount_as_sold
        self.amount_used = amount_used
        self.price_per_oz = (self.cost / self.amount_as_sold)
        self.total_item = (self.amount_used * self.price_per_oz)

    @classmethod
    def from_input(cls):
        '''input for class'''
        try:
            return cls(
                input('Item Name: '),
                float(input('Cost: ')),
                float(input('Net Weight as sold: ')),
                float(input('Amount you used: ')))
        except ValueError as e:
            print(e)
            print("that's not a number dumb-dumb")
            print('FOR YOUR INSOLENCE YOU WILL BE SENT BACK TO THE MAIN MENU!!!')
            time.sleep(3)
            main()


def display_items():
    '''Display the list of items and the data'''
    for index, item in enumerate(item_list, start=1):
        print('Item ', index,
              '{0.name}         '
              'Item Price : ${3:,.2f}        '
              'At a Price pre oz of : {1:,.4f}         '
              'Subtotal ${2:,.2f}'.format(
                  item, item.price_per_oz, item.total_item, item.cost))
    return


def grand_total(total):
    '''loops the items totals adding them'''
    global item_list
    for item in range(len(item_list)):       #  is more pythoic than count loop
        total += item_list[item].total_item
    return total


def show_total_screen():
    '''Shows the total screen'''
    os.system("clear")
    item_total_text_menu = 'Total Price List'
    print(item_total_text_menu.center(100, '_'))
    display_items()
    print('')
    grand_total(total)
    print('Your total is:  ', '${:,.2f}\n'.format(grand_total(total)))
    print(100 * '_')
    go_to_main = input('Press [Enter] for Menu     [Q]uit: ')
    os.system("clear")
    if go_to_main == '':
        main()
    elif go_to_main == 'q':
        os.system("clear")
        print('GOOD BYE')
        quit()
    else:
        main()


def main():
    """Main Menu selection structure """
    os.system("clear")
    global item_list, total
    add_more = True
    menu_text = 'Main Menu'
    print(menu_text.center(30, '_'))
    print('Welcome! Please pick an action')
    print("""
1. [A]dd Items
2. [T]otal
3. [Q]uit""")
    print(30 * '_')
    main_action = input("Input # or Letter: ")
    if main_action in ('1', 'a', ''):
        os.system("clear")
        global item_list, total
        while add_more is True:
            item_list.append(Item.from_input())
            os.system("clear")
            item_list_text_menu = 'Item Price List'
            print(item_list_text_menu.center(100, '_'))
            display_items()
            print('\nYour total is:  ', '${:,.2f}\n'.format(grand_total(total)))
            print(100 * '_')
            add_more = input('ADD More Press [Enter]     [M]ain Menu    [T]otal    [Q]uit  :')
            os.system("clear")
            if add_more == '':
                add_more = True
            elif add_more == 'm':
                main()
            elif add_more == 't':
                show_total_screen()
            elif add_more == 'q':
                os.system("clear")
                print('GOOD BYE')
                quit()
            else:
                main()

    elif main_action in ('2', 't'):
        show_total_screen()
    elif main_action in ('3', 'q'):
        os.system("clear")
        print('quitting')
        quit()
    else:
        main()


main()
