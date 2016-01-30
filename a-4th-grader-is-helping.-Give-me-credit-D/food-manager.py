import pickle
import time
while 21:
    foodinput = raw_input("What is the food? ")
    foodinput = foodinput.lower()
    def Calculator(name, sving_size, sving_size_unit, calories, total_fat, sat_fat, trans_fat):
        print "It is a(n) " + name + " with " + str(sving_size) + " " + str(sving_size_unit) + " as the serving size, " + str(calories) + " calories, and " + str(total_fat) + "g of total fat."
        print "This includes " + str(sat_fat) + "g of saturated fat and " + str(trans_fat) + "g of trans fat."
    
    if len(foodinput) > 0:
        
    #FritoLay        
        #Cheetos
        if foodinput == "cheetos crunchy":
                Calculator("Cheetos Crunchy", 1, "oz (28g/about 21 pieces)", 150, 10, 1.5, 0)
        elif foodinput == "cheetos puffs":
                Calculator("Cheetos Puffs", 1, "oz (28g/about 21 pieces)", 150, 10, 1.5, 0)
        #Doritos
        elif foodinput == "doritos cool ranch":
                Calculator("Doritos Cool Ranch", 1, "oz (28g/about 11 pieces)", 150, 8, 1, 0)
        elif foodinput == "doritos nacho cheese":
                Calculator("Doritos Nacho Cheese", 1, "oz (28g/about 11 pieces)", 140, 8, 1, 0)
        #Lay's
        elif foodinput == "lays barbecue":
                Calculator("Lay's Barbecue", 1, "oz (28g/about 15 pieces)", 160, 10, 1.5, 0)
        elif foodinput == "lays classic":
                Calculator("Lay's Classic", 1, "oz (28g/about 15 pieces)", 160, 10, 1.5, 0)
    
    #gen_Fruits    
        elif foodinput == "apple":
                Calculator("apple", 1, "fruit", 95, 0.3, 0.1, 0)
        elif foodinput == "guava":
                Calculator("guava", 1, "fruit", 38, 0.5, 0.1, 0)
        elif foodinput == "pear":
                Calculator("pear", 1, "fruit", 102, 0.2, 0, 0)
            
    #gen_Vegetables    
        elif foodinput == "broccoli":
                Calculator("broccoli", 1, "NLEA serving", 50, 0.5, 0.1, 0)
                
        else:
            print "Can't recognize."
    
    else:
        print "Empty. Please enter a food."
