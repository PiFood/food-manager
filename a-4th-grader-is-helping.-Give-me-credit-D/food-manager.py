import pickle
import time
while 21:
    foodinput = raw_input("What is the food: ")
    foodinput = foodinput.lower()
    def Calculator(name, sving_size, sving_size_unit, fat, calories):
        print "It is a(n) " + name + " with " + str(sving_size) + str(sving_size_unit) + " as the serving size and " + str(fat) + "g" + " of fat and with " + str(calories) + " calories."
    
    if len(foodinput) > 0 and foodinput.isalpha():
        if foodinput == "apple":
            Calculator("apple", 1, fruit, 30, 300)
        elif foodinput == "pear":
            Calculator("pear", 2, fruit, 35, 450)
        else:
            print "Can't recognize."
    
    else:
        print "Empty. Please enter a food."
