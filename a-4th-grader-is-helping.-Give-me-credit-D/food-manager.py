import pickle
import time

#!/usr/bin/python
from sys import argv, exit
import zbar

global foodinput
foodinput = ""

def search():
    def Calculator(name, sving_size_unit, sving_size, calories, total_fat, sat_fat, trans_fat):
        print "It is a(n) " + name + "."
        print "The serving size is " + str(sving_size_unit) + " " + str(sving_size) + "."
        print "It has " + str(calories) + " calories."
        print "It has " + str(total_fat) + " g of total fat."
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
            
    #Easter Eggs
        elif foodinput == "mlg combo":
            Calculator("ONE DOTHS NAWT GO THIS FAR", 360, "swag", "morethanu", "3sketchy5u", "dealwithit", 720)
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

    #Nature Nate's   
        elif foodinput == "nature nates honey" or foodinput == "03877883044":
            Calculator("HHOONNEEYY", 1, "tbsp", 60, 0, 0, 0)
    #Pepsico
        elif foodinput == "mountain dew":
            Calculator("Mountain Dew", 1, "container", 170, 0, 0, 0,)
        else:
            print "Can't recognize."
        
    else:
        print "Empty. Please enter a food."
def admin():
        print "I'm watching you."
def enter():
    global foodinput
    foodinput = raw_input("What is the food? ")
    foodinput = foodinput.lower()
    search()
def scanner():
    # create a Processor
    proc = zbar.Processor()
    
    # configure the Processor
    proc.parse_config('enable')
    
    # initialize the Processor
    device = '/dev/video0'
    if len(argv) > 1:
        device = argv[1]
    proc.init(device)
    
    # setup a callback
    def my_handler(proc, image, closure):
        # extract results
        for symbol in image.symbols:
            # do something useful with results
            print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data 
            foodinput = symbol.data
#            if symbol.data == "381371151035":
#                foodinput = "aveeno"
                
    proc.set_data_handler(my_handler)
    
    # enable the preview window
    proc.visible = True
    
    # initiate scanning
    proc.active = True

    try:
        # keep scanning until user provides key/mouse input
        proc.user_wait()
    except zbar.WindowClosed, e:
        if len(foodinput) != 0:
            search()
"ethan" == "cool"
while "ethan" == "cool":
    thingInput = raw_input("Enter S for scanning, enter I for input, and enter Q to quit. ")
    thingInput = thingInput.lower()
    if thingInput == 's':
        scanner()
    elif thingInput == 'i':
        enter()
        
    elif thingInput == "pink fluffy fire breathing unicornz":
        vadmin = True
        print "You are admin, Eric."
        admin()
    elif thingInput == "secret passcode is secret":
        vadmin = True
        print "You are admin, Ethan."
        print "( ͡° ͜ʖ ͡°)"
        admin()
        
    elif thingInput == 'q':
        print "You have pressed 'q'."
        time.sleep(1)
        exit()
    else:
        print "Enter a valid letter"
