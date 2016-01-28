import pickle
import time
while 21:
    foodinput = raw_input("What is the food: ")
    foodinput = foodinput.lower()
    def Calculator(name, sving_size, fat, calories):
        print "It is " + name + " Serving = " + str(sving_size) + "g" + " Fat = " + str(fat) + " Calories = " + str(calories)
    Calculator("apple", 1, 30, 300)
        

    if len(foodinput) == 0:
        print "Empty. Please enter a food."
    else:
         print "Successful!"  
