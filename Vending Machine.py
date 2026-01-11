#dictionary with codes, names, and price
products = {
    '101' :{'name': 'Blueberry Lemon Cake', 'price':15},
    '102' :{'name': 'Honey Cake', 'price':15},
    '103' :{'name': 'Tiramisu', 'price':15},
    '104' :{'name': 'Chocolate Mouse Cake', 'price':15},
    '105' :{'name': 'Red Velvet Cake', 'price':12},
    '106' :{'name': 'Carrot Cake', 'price':12},
    '107' :{'name': 'Mango Peach Cake', 'price':15},
    '108' :{'name': 'Chocolate Pistachio Cake', 'price':12},
    '109' :{'name': 'Matcha Cake', 'price': 15},
    '110' :{'name': 'Biscoff Lotus Cheesecake', 'price':15},
    '111' :{'name': 'Cookies and Cream Cheesecake', 'price':15},
    '112' :{'name': 'Cookies', 'price':6},
    '113' :{'name': 'Brownies', 'price':6},
    '114' :{'name': 'Water', 'price':2},
    '115' :{'name': 'Latte', 'price':8},
    '116' :{'name': 'Spanish Latte ', 'price':10},
    '117' :{'name': 'Caramel Macchiato', 'price':10},
    '118' :{'name': 'Cappuccino', 'price':8},
    '119' :{'name': 'Americano', 'price':8},
    '120' :{'name': 'Pistachio Latte', 'price':10}
}

def dmenu():
    for key, product in products.items():
        print(f"{key}. {product['name']:<30} {product['price']}SR")
        #format and displays the product menu

def addcart(cart, item ,price):
    cart.append({'item':  item, 'price': price})
    return sumtotal(cart)
    #adds the product to cart

def sumtotal(cart):
    total = 0
    for item in cart:
        total += item['price']
    return total
    #run through each item and sum the prices

def dcart(cart):
    if len(cart)== 0:
        print('Your cart is empty.')
    else:
        print('__________________________')
        print('Your cart:')
        for pro, item in enumerate(cart):
            print(f'{pro+1}. {item['item']} - {item['price']}SR')
        total = sumtotal(cart)
        print('Total:', total,'SR')
        print('__________________________')
"""
displays the contents of the cart with numerical numbers 
 and calculate the total fo the items in the cart
"""

def remove(cart, code):
    if code in products:
        product_name = products[code]['name']
        for item in cart:
            if item['item'] == product_name:
                cart.remove(item)
                print('__________________________')
                print(product_name, 'removed from cart')
                return True
        print('_______________________________')
        print(product_name, 'not found in cart') 
        return False
    else:
        print('__________________________')
        print('Invalid code.')
        return False

#it checks the item in the cart before being removed

    
def main():
    cart = [] #empty cart
    print('Welcome to Bake & Break!')
    print('_________________________________________________')
    print('Commands:')
    print('- To add an item enter the product code(101-120)')
    print('- to remove an item. Type "remove [code]"')
    print('- Type "purchase" to checkout')
    print('_________________________________________________')

    dmenu()
    print('________________________________________________')
#displays commands and menu for users
    while True: 
        dcart(cart)
        #displays the contents of the cart

        userin = input('Enter product code or command: ').strip().lower()
        #gets input and turns it into lowercase also stripping whitespace
        if userin == 'purchase':
            if len(cart) == 0:
                print('___________________________________________________________')
                print('Your cart is empty! Purchase a product before you checkout')
            else:
                print('CHECKOUT')
                for item in cart:
                    print(item['item'], item['price'], 'SR')
                total = sumtotal(cart)
                print('Total:', total, 'SR')
                print('_______________________________________')
                #checks whether the cart is empty before proceeding to payment

                while True:
                    print('-To cancel the purchase. Type "cancel"')
                    print('_______________________________________')
                    payment = input('Enter the amount of money:')

                    if payment == 'cancel':
                        print('__________________________')
                        print('Purchase cancelled')
                        return
                    else:
                        if payment.replace('.','', 1).isdigit():
                            payment = float(payment)
                            if payment >= total:
                                change = payment - total
                                print('________________________________________________________________________')
                                print(f'Your change is {change}SR')
                                print('Thank your for purchasing. Please collect your purchase in the dispenser')
                                return
                            else:
                                print('_________________________________________________')
                                print('Insufficient. Returning Money....')
                        else:
                            print('_________________________________')
                            print('Invalid amount. Please try again')
                """
                validates payment and gives option to cancel the purchase
                Makes sure the payment is in numerical value
                Gives change 
                determines insufficient payment and error
                """
        elif userin.startswith('remove'):
            part = userin.split()
            if len(part) == 2:
                code = part[1]
                remove(cart,code)
            else:
                print('______________________________________')
                print('Error! Please try again "remove[code]"')
                #handles item removal and errors
                
        elif userin in products:
            product = products[userin]
            new_total = addcart(cart, product['name'], product['price'])
            print('______________________________________________')
            print(product['name'], 'added to cart')
            #handles adding product to the cart
        
        else:
            print('______________________________________________')
            print('Invalid! Please enter a code or type a command')
            #handles errors
if __name__ == '__main__':
    main()

