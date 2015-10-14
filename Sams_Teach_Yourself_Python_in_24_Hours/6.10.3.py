inventory = ['pepperoni',
        'sausage',
        'cheese',
        'peppers']

item1 = raw_input("Please give me a topping: ")
if item1 in inventory:
    print "we have {} ." .format(item1)
    toppings = [item1]
else:
    print "sorry, we don't have{} ." .format(item1)
    toppings = []

item2 = raw_input("Please give me one more topping: ")
if item2 in inventory:
    print "we have {} ." .format(item2)
    toppings.append(item2)
else:
    print "sorry, we don't have {} ." .format(item2)
    toppings = toppings + []

print "Here are your toppings: \n{}" .format(toppings)
