import pickle
import time
while 21:
    foodinput = raw_input("What is the food: ")
    foodinput = foodinput.lower()
    def Calculator(name, sving_size, fat, calories):
        print "It is a(n)" + name + " with a serving size of = " + str(sving_size) + "g" + " Fat = " + str(fat) + " Calories = " + str(calories)
    
    if len(foodinput) > 0 and foodinput.isalpha():
        if foodinput == "apple":
            Calculator("Apple", 1, 30, 300)
        elif foodinput == "pear":
            Calculator("pear", 2, 35, 450)
        else:
            print "Can't recognize."
    
    else:
        print "Empty. Please enter a food."
