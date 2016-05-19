#!/usr/bin/env python
import time
import pygame

#!/usr/bin/python
from sys import argv, exit
import zbar
global varia
global foodinput
foodinput = ""
global x
x = 50
global y
y = 50
osi = []
ppo = 0
entererq = False

def search():
    def Calculator(name, sving_size, sving_size_unit, calories, total_fat, sat_fat, trans_fat):
        koop("it is a(n) " + name + " with " + str(sving_size) + " " + str(sving_size_unit) + " as the serving size, " + str(calories) + " calories, and " + str(total_fat) + "g of total fat.", True)
        koop("this includes " + str(sat_fat) + "g of saturated fat and " + str(trans_fat) + "g of trans fat.", True)
        
    if len(foodinput) > 0:
            
#FritoLay        
    #Cheetos
        if foodinput == "cheetos crunchy":
            Calculator("cheetos crunchy", 1, "oz (28g or about 21 pieces)", 150, 10, 1.5, 0)
        elif foodinput == "cheetos puffs":
            Calculator("cheetos puffs", 1, "oz (28g or about 21 pieces)", 150, 10, 1.5, 0)
    #Doritos
        elif foodinput == "doritos cool ranch":
            Calculator("doritos cool ranch", 1, "oz (28g or about 11 pieces)", 150, 8, 1, 0)
        elif foodinput == "doritos nacho cheese":
            Calculator("doritos nacho cheese", 1, "oz (28g or about 11 pieces)", 140, 8, 1, 0)
    #Lay's
        elif foodinput == "lays barbecue":
                Calculator("lay's barbecue", 1, "oz (28g or about 15 pieces)", 160, 10, 1.5, 0)
        elif foodinput == "lays classic":
            Calculator("lay's classic", 1, "oz (28g or about 15 pieces)", 160, 10, 1.5, 0)
        
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
            Calculator("hhhooooonnneyyyy", 1, "tbsp", 60, 0, 0, 0)

        else:
            koop("can not recognize", True)
        
    else:
        koop("empty please enter a food", True)
def admin():
        print "asdf"
def enter():

    koop("what is the food  ", False)
def process():
    global foodinput, thingin
    foodinput = thingin
    
    foodinput = foodinput.lower()
    search()
def scanner():
    # create a Processor
    proc = zbar.Processor()
    
    # configure the Processor
    proc.parse_config('enable')
    
    # initialize the Processor
    device = '/dev/video0'
    try:  
        if len(argv) > 1:
            device = argv[1]
        proc.init(device)
    except:
        koop("error device not found", True)
        doStuff(False)
        
    
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
def showStuff():
    global x
    if adown:
        screen.blit(pica, [x, y])
    elif bdown:
        screen.blit(picb, [x, y])
    elif cdown:
        screen.blit(picc, [x, y])
    elif ddown:
        screen.blit(picd, [x, y])
    elif edown:
        screen.blit(pice, [x, y])
    elif fdown:
        screen.blit(picf, [x, y])
    elif gdown:
        screen.blit(picg, [x, y])
    elif hdown:
        screen.blit(pich, [x, y])
    elif idown:
        screen.blit(pici, [x, y])
    elif jdown:
        screen.blit(picj, [x, y])
    elif kdown:
        screen.blit(pick, [x, y])
    elif ldown:
        screen.blit(picl, [x, y])
    elif mdown:
        screen.blit(picm, [x, y])
    elif ndown:
        screen.blit(picn, [x, y])
    elif odown:
        screen.blit(pico, [x, y])
    elif pdown:
        screen.blit(picp, [x, y])
    elif qdown:
        screen.blit(picq, [x, y])
    elif rdown:
        screen.blit(picr, [x, y])
    elif sdown:
        screen.blit(pics, [x, y])
    elif tdown:
        screen.blit(pict, [x, y])
    elif udown:
        screen.blit(picu, [x, y])
    elif vdown:
        screen.blit(picv, [x, y])
    elif wdown:
        screen.blit(picw, [x, y])
    elif xdown:
        screen.blit(picx, [x, y])
    elif ydown:
        screen.blit(picy, [x, y])
    elif zdown:
        screen.blit(picz, [x, y])
    elif spacedown:
        print "space"
    elif onedown:
        screen.blit(pic1, [x, y])
    elif twodown:
        screen.blit(pic2, [x, y])
    elif threedown:
        screen.blit(pic3, [x, y])
    elif fourdown:
        screen.blit(pic4, [x, y])
    elif fivedown:
        screen.blit(pic5, [x, y])
    elif sixdown:
        screen.blit(pic6, [x, y])
    elif sevendown:
        screen.blit(pic7, [x, y])
    elif eightdown:
        screen.blit(pic8, [x, y])
    elif ninedown:
        screen.blit(pic9, [x, y])
    elif zerodown:
        screen.blit(pic0, [x, y])
    pygame.display.flip()
def noop(letter):
    global adown, bdown, adown, cdown, ddown, edown, fdown, gdown, hdown, idown, jdown, kdown, ldown, mdown, ndown, odown, pdown, qdown, rdown, sdown, tdown, udown, vdown, wdown, xdown, ydown, zdown, spacedown, onedown, twodown, threedown, fourdown, fivedown, sixdown, sevendown, eightdown, ninedown, zerodown
    if letter == 'a':
        adown = True
        showStuff()
        adown = False
    elif letter == 'b':
        bdown = True
        showStuff()
        bdown = False
    elif letter == 'c':
        cdown = True
        showStuff()
        cdown = False
    elif letter == 'd':
        ddown = True
        showStuff()
        ddown = False
    elif letter == 'e':
        edown = True
        showStuff()
        edown = False
    elif letter == 'f':
        fdown = True
        showStuff()
        fdown = False
    elif letter == 'g':
        gdown = True
        showStuff()
        gdown = False
    elif letter == 'h':
        hdown = True
        showStuff()
        hdown = False
    elif letter == 'i':
        idown = True
        showStuff()
        idown = False
    elif letter == 'j':
        jdown = True
        showStuff()
        jdown = False
    elif letter == 'k':
        kdown = True
        showStuff()
        kdown = False
    elif letter == 'l':
        ldown = True
        showStuff()
        ldown = False
    elif letter == 'm':
        mdown = True
        showStuff()
        mdown = False
    elif letter == 'n':
        ndown = True
        showStuff()
        ndown = False
    elif letter == 'o':
        odown = True
        showStuff()
        odown = False
    elif letter == 'p':
        pdown = True
        showStuff()
        pdown = False
    elif letter == 'q':
        qdown = True
        showStuff()
        qdown = False
    elif letter == 'r':
        rdown = True
        showStuff()
        rdown = False
    elif letter == 's':
        sdown = True
        showStuff()
        sdown = False
    elif letter == 't':
        tdown = True
        showStuff()
        tdown = False
    elif letter == 'u':
        udown = True
        showStuff()
        udown = False
    elif letter == 'v':
        vdown = True
        showStuff()
        vdown = False
    elif letter == 'w':
        wdown = True
        showStuff()
        wdown = False
    elif letter == 'x':
        xdown = True
        showStuff()
        xdown = False
    elif letter == 'y':
        ydown = True
        showStuff()
        ydown = False
    elif letter == 'z':
        zdown = True
        showStuff()
        zdown = False
    elif letter == ' ':
        spacedown = True
        showStuff()
        spacedown = False
    elif letter == '1':
        onedown = True
        showStuff()
        onedown = False
    elif letter == '2':
        twodown = True
        showStuff()
        twodown = False
    elif letter == '3':
        threedown = True
        showStuff()
        threedown = False
    elif letter == '4':
        fourdown = True
        showStuff()
        fourdown = False
    elif letter == '5':
        fivedown = True
        showStuff()
        fivedown = False
    elif letter == '6':
        sixdown = True
        showStuff()
        sixdown = False
    elif letter == '7':
        sevendown = True
        showStuff()
        sevendown = False
    elif letter == '8':
        eightdown = True
        showStuff()
        eightdown = False
    elif letter == '9':
        ninedown = True
        showStuff()
        ninedown = False
    elif letter == '0':
        zerodown = True
        showStuff()
        zerodown = False
        
def koop(string, yesorno):
    global x, y
    liststr = list(string)
    for i in range(len(string)):
        for j in ['a', 'b', 'c' ,'d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            if liststr[i] == j:
                noop(j)
                x += 40
                if x > 1650:
                    x = 0
                    y += 60
    if yesorno:
        x = 0
        y += 60
                
#code that does stuff.
pygame.init()
screen = pygame.display.set_mode([1800, 1000])
screen.fill([255, 255, 255])
pica = pygame.image.load("letters/a.jpg")
picb = pygame.image.load("letters/b.jpg")
picc = pygame.image.load("letters/c.png")
picd = pygame.image.load("letters/d.png")
pice = pygame.image.load("letters/e.jpg")
picf = pygame.image.load("letters/f.png")
picg = pygame.image.load("letters/g.png")
pich = pygame.image.load("letters/h.png")
pici = pygame.image.load("letters/i.jpg")
picj = pygame.image.load("letters/j.jpg")
pick = pygame.image.load("letters/k.ico")
picl = pygame.image.load("letters/l.jpg")
picm = pygame.image.load("letters/m.jpg")
picn = pygame.image.load("letters/n.png")
pico = pygame.image.load("letters/o.png")
picp = pygame.image.load("letters/p.png")
picq = pygame.image.load("letters/q.jpg")
picr = pygame.image.load("letters/r.jpg")
pics = pygame.image.load("letters/s.jpg")
pict = pygame.image.load("letters/t.png")
picu = pygame.image.load("letters/u.png")
picv = pygame.image.load("letters/v.jpg")
picw = pygame.image.load("letters/w.png")
picx = pygame.image.load("letters/x.png")
picy = pygame.image.load("letters/y.png")
picz = pygame.image.load("letters/z.png")
pic1 = pygame.image.load("numbers/1.png")
pic2 = pygame.image.load("numbers/2.png")
pic3 = pygame.image.load("numbers/3.png")
pic4 = pygame.image.load("numbers/4.jpg")
pic5 = pygame.image.load("numbers/5.png")
pic6 = pygame.image.load("numbers/6.jpg")
pic7 = pygame.image.load("numbers/7.jpg")
pic8 = pygame.image.load("numbers/8.png")
pic9 = pygame.image.load("numbers/9.jpg")
pic0 = pygame.image.load("numbers/0.jpg")
adown = True
bdown = True
cdown = True
ddown = True
edown = True
fdown = True
gdown = True
jdown = True
hdown = True
idown = True
kdown = True
ldown = True
mdown = True
adown = False
bdown = False
cdown = False
ddown = False
edown = False
fdown = False
gdown = False
hdown = False
idown = False
jdown = False
kdown = False
ldown = False
ldown = False
mdown = False
ndown = True
odown = True
pdown = True
qdown = True
rdown = True
sdown = True
tdown = True
udown = True
vdown = True
wdown = True
xdown = True
ydown = True
zdown = True
ndown = False
odown = False
pdown = False
qdown = False
rdown = False
sdown = False
tdown = False
udown = False
vdown = False
wdown = False
xdown = False
ydown = False
zdown = False
onedown = True
twodown = True
threedown = True
fourdown = True
fivedown = True
sixdown = True
sevendown = True
eightdown = True
ninedown = True
zerodown = True
spacedown = True
onedown = False
twodown = False
threedown = False
fourdown = False
fivedown = False
sixdown = False
sevendown = False
eightdown = False
ninedown = False
zerodown = False
spacedown = False

screen.fill([255, 255, 255])
def doStuff(bypassyesorno):
    global thinginputo, x, y, osi, enterer, thingin, entererq
    if bypassyesorno == False:
        thinginputo = True
    while 1:
        entererq = False
        if thinginputo:
            
            koop('enter s for scanner', False)
            enterer = True 
            y += 60
            x = 50
            koop('enter e for enter', False)
            y += 60
            x = 50
            koop('enter q to quit', True)
            thinginputo = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    adown = True
                    showStuff()
                    osi.append("a")
                    adown = False
                    koop('a', False)
                if event.key == pygame.K_b:
                    bdown = True
                    showStuff()
                    osi.append("b")
                    bdown = False
                    koop('b', False)
                if event.key == pygame.K_c:
                    cdown = True
                    showStuff()
                    osi.append("c")
                    cdown = False
                    koop('c', False)
                if event.key == pygame.K_d:
                    ddown = True
                    showStuff()
                    osi.append("d")
                    ddown = False
                    koop('d', False)
                if event.key == pygame.K_e:
                    if enterer:
                        print "First E entered."
                        enter()
                        #enterer = False
                        osi = []
                    if not enterer:
                        edown = True
                        showStuff()
                        osi.append("e")
                        edown = False
                        koop('e', False)
                print "after K-e: enterer=", enterer
                if event.key == pygame.K_f:
                    fdown = True
                    showStuff()
                    osi.append("f")
                    fdown = False
                    koop('f', False)
                if event.key == pygame.K_g:
                    gdown = True
                    showStuff()
                    osi.append("g")
                    gdown = False
                    koop('g', False)
                if event.key == pygame.K_h:
                    hdown = True
                    showStuff()
                    osi.append("h")
                    hdown = False
                    koop('h', False)
                if event.key == pygame.K_i:
                    idown = True
                    showStuff()
                    osi.append("i")
                    idown = False
                    koop('i', False)
                if event.key == pygame.K_j:
                    jdown = True
                    showStuff()
                    osi.append("j")
                    jdown = False
                    koop('j', False)
                if event.key == pygame.K_k:
                    kdown = True
                    showStuff()
                    osi.append("k")
                    kdown = False
                    koop('k', False)
                if event.key == pygame.K_l:
                    ldown = True
                    showStuff()
                    osi.append("l")
                    ldown = False
                    koop('l', False)
                if event.key == pygame.K_m:
                    mdown = True
                    showStuff()
                    osi.append("m")
                    mdown = False
                    koop('m', False)
                if event.key == pygame.K_n:
                    ndown = True
                    showStuff()
                    osi.append("n")
                    ndown = False
                    koop('n', False)
                if event.key == pygame.K_o:
                    odown = True
                    showStuff()
                    osi.append("o")
                    odown = False
                    koop('o', False)
                if event.key == pygame.K_p:
                    pdown = True
                    showStuff()
                    osi.append("p")
                    pdown = False
                    koop('p', False)
                if event.key == pygame.K_q:
                    if enterer:
                        exit()
                    qdown = True
                    showStuff()
                    osi.append("q")
                    qdown = False
                    koop('q', False)
                if event.key == pygame.K_r:
                    rdown = True
                    showStuff()
                    osi.append("r")
                    rdown = False
                    koop('r', False)
                if event.key == pygame.K_s:
                    print "after enter S: enterer=", enterer
                    if enterer:
                        scanner()
                        osi = []
                    if not enterer:
                        sdown = True
                        showStuff()
                        osi.append("s")
                        sdown = False
                        koop('s', False)
                if event.key == pygame.K_t:
                    tdown = True
                    showStuff()
                    osi.append("t")
                    tdown = False
                    koop('t', False)
                if event.key == pygame.K_u:
                    udown = True
                    showStuff()
                    osi.append("u")
                    udown = False
                    koop('u', False)
                if event.key == pygame.K_v:
                    vdown = True
                    showStuff()
                    osi.append("v")
                    vdown = False
                    koop('v', False)
                if event.key == pygame.K_w:
                    wdown = True
                    showStuff()
                    osi.append("w")
                    wdown = False
                    koop('w', False)
                if event.key == pygame.K_x:
                    xdown = True
                    showStuff()
                    osi.append("x")
                    xdown = False
                    koop('x', False)
                if event.key == pygame.K_y:
                    ydown = True
                    showStuff()
                    osi.append("y")
                    ydown = False
                    koop('y', False)
                if event.key == pygame.K_z:
                    zdown = True
                    showStuff()
                    osi.append("z")
                    zdown = False
                    koop('z', False)
                if event.key == pygame.K_SPACE:
                    koop(' ', False)
                    osi.append(' ')
                if event.key == pygame.K_BACKSPACE:
                    print "hi"
                if event.key == pygame.K_RETURN:
                    y += 60
                    x = 0
                    thingin = ''.join(osi)
                    if thingin == "refresh":
                        screen.fill([255, 255, 255])
                        x = 0
                        y = 0
                    print thingin
                    process()
                    osi = []
                    entererq = True
                    enterer = True
                    koop('enter s for scanner', False)
                    y += 60
                    x = 50
                    koop('enter e for enter', False)
                    y += 60
                    x = 50
                    koop('enter q to quit', True)
                if entererq == False:
                    enterer = False
                if x > 1650:
                    x = 0
                    y += 60
                print "after one key input, enterer=", enterer
        if y > 800:
            screen.fill([255, 255, 255])
            y = 5
doStuff(False)

            
                
            

