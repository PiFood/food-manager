import pickle
import time
while 21:
    foodinput = raw_input("What is the food? ")
    foodinput = foodinput.lower()
    def Calculator(name, sving_size, sving_size_unit, calories, fat):
        print "It is a(n) " + name + " with " + str(sving_size) + str(sving_size_unit) + " as the serving size, " + str(calories) + " calories, and " + str(fat) + "g of total fat."
    
    if len(foodinput) > 0 and foodinput.isalpha():
        
    #FritoLay        
        #Cheetos
            elif foodinput == "cheetos":
                Calculator("cheetos", 1, " oz (28g/about 21 pieces)", 150, 10)
            elif foodinput == "cheetos puffs":
                Calculator("cheetos puffs", 1, " oz (28g/about 21 pieces)", 150, 10)
        #Doritos
            elif foodinput == "doritos nacho cheese":
                Calculator("doritos nacho cheese", 1, " oz (28g/about 11 pieces)", 140, 8)
            elif foodinput == "doritos cool ranch":
                Calculator("doritos cool ranch", 1, " oz (28g/about 11 pieces)", 150, 8)
        #Lay's
            elif foodinput == "lays barbecue":
                Calculator("lays barbecue", 1, " oz (28g/about 15 pieces)", 160, 10)
            elif foodinput == "lays classic":
                Calculator("lays classic", 1, " oz (28g/about 15 pieces)", 160, 10)
    #General Fruits    
            if foodinput == "apple":
                Calculator("apple", 1, " fruit", 95, 0.3)
            elif foodinput == "guava":
                Calculator("guava", 1, " fruit", 450, 38)
            elif foodinput == "pear":
                Calculator("pear", 1, " fruit", 450, 35)
        else:
            print "Can't recognize."
    
    else:
        print "Empty. Please enter a food."
