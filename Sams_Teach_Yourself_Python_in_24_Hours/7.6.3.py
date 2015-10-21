Total = 0.0
print "Welcome to the receipt program!"

while True:
    value = raw_input("Enter the value for the seat ['q' to quit]: ")

    if value == 'q':
        break
       
    if value.isalpha():
        print "I'm sorry, but {} isn't valid. Please try again.".format(value)
        continue

    value = float(value)
    Total = Total + value    

print "*****\nTotal: $ {}".format(Total)
    
    
