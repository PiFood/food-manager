import pickle
import time
while 21:
    foodinput = raw_input("What is the food: ")
    foodinput = foodinput.lower()
    def Calculator(name, sving_size, sving_size_unit, fat, calories):
        print "It is a(n) " + name + " with " + str(sving_size) + str(sving_size_unit) + " as the serving size, " + str(calories) + " calories, and " + str(fat) + "g of total fat."
    
    if len(foodinput) > 0 and foodinput.isalpha():
        if foodinput == "apple":
            Calculator("apple", 1, " fruit", 0.3, 95)
        elif foodinput == "guava":
            Calculator("guava", 1, " fruit", 38, 450)
        elif foodinput == "pear":
            Calculator("pear", 1, " fruit", 35, 450)
        #cheetos
        elif foodinput == "cheetos":
            Calculator("cheetos", 1, " oz (28g/about 21 pieces)", 10, 150)
        else:
            print "Can't recognize."
    
    else:
        print "Empty. Please enter a food."
