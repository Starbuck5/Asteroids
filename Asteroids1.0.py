import pygame
import math
import random

def printer(ship_pointlist, object_list, color, scalar3, scalar2, scalar1, scalarscalar): #prints the object
    screen.fill(color)
    for i in range(int(len(object_list)/8)): 
        xpos = object_list[(i * 8)]
        
        ypos = object_list[1 + (i * 8)]
        object_number = object_list[4 + (i * 8)] 
        if object_number == 1: #draws main ship
            pygame.draw.aalines(screen, (255, 255, 255), True, ship_pointlist, False)
        if object_number == 2 or object_number == 8: #draws missiles (id 8 are alien missiles)
            pygame.draw.circle(screen, (255, 255, 255), (int(xpos), int(ypos)), 2, 0)
        if object_number == 3: #draws reserve ships
            res_ship_pointlist = [[xpos, ypos-30*scalar3], [xpos+15*scalar3, ypos+10*scalar3], [xpos, ypos], [xpos-15*scalar3, ypos+10*scalar3]]
            pygame.draw.aalines(screen, (255, 255, 255), True, res_ship_pointlist, True)
        if object_number == 4: #draws explosion effects
            pygame.draw.circle(screen, (255, 255, 255), (int(xpos), int(ypos)), 1, 0)
        if object_number == 5: #draws shielded ship
            pygame.draw.polygon(screen, (255,255,255), ship_pointlist, round(3*scalarscalar))
        if object_number == 6: #draws alien
            alien_pointlist = [[xpos-25*scalar1, ypos], [xpos-18*scalar1, ypos], [xpos-10*scalar1, ypos+8*scalar1], [xpos+10*scalar1, ypos+8*scalar1], [xpos+18*scalar1, ypos], [xpos+25*scalar1, ypos], [xpos-18*scalar1, ypos],
                            [xpos-10*scalar1, ypos], [xpos-7*scalar1, ypos-7*scalar1], [xpos, ypos-10*scalar1], [xpos+7*scalar1, ypos-7*scalar1], [xpos+10*scalar1, ypos]]
            pygame.draw.aalines(screen, (255,255,255), True, alien_pointlist, False)
            
        # asteroids
        if object_number == 11:
            asteroid1 = [[xpos+17*scalar2, ypos+1*scalar2], [xpos+12*scalar2, ypos+8*scalar2], [xpos-2*scalar2, ypos+17*scalar2], [xpos-8*scalar2, ypos+11*scalar2], [xpos-16*scalar2, ypos+3*scalar2], [xpos-14*scalar2, ypos-7*scalar2],
                         [xpos-4*scalar2, ypos-17*scalar2], [xpos+10*scalar2, ypos-10*scalar2]]           
        if object_number == 12:
            asteroid1 = [[xpos+16*scalar2, ypos-3*scalar2], [xpos+12*scalar2, ypos+10*scalar2], [xpos-2*scalar2, ypos+17*scalar2], [xpos-10*scalar2, ypos+14*scalar2], [xpos-19*scalar2, ypos-2*scalar2], [xpos-8*scalar2, ypos-13*scalar2],
                         [xpos+2*scalar2, ypos-16*scalar2], [xpos+8*scalar2, ypos-12*scalar2]]          
        if object_number == 13:     
            asteroid1 = [[xpos+16*scalar2, ypos+3*scalar2], [xpos+7*scalar2, ypos+13*scalar2], [xpos-8*scalar2, ypos+14*scalar2], [xpos-18*scalar2, ypos+4*scalar2], [xpos-11*scalar2, ypos-11*scalar2], [xpos-3*scalar2, ypos-16*scalar2],
                         [xpos+11*scalar2, ypos-9*scalar2]]
        if object_number == 14:
            asteroid1 = [[xpos+18*scalar2, ypos+0*scalar2], [xpos+10*scalar2, ypos+-10*scalar2], [xpos+0*scalar2, ypos+-17*scalar2], [xpos+-13*scalar2, ypos+-12*scalar2],
                         [xpos+-20*scalar2, ypos+0*scalar2], [xpos+-11*scalar2, ypos+11*scalar2], [xpos+0*scalar2, ypos+13*scalar2], [xpos+14*scalar2, ypos+12*scalar2]]
        if object_number == 16:
            asteroid1 = [[xpos+26*scalar2, ypos-3*scalar2], [xpos+20*scalar2, ypos+10*scalar2], [xpos+4*scalar2, ypos+21*scalar2], [xpos-8*scalar2, ypos+9*scalar2], [xpos-8*scalar2, ypos+10*scalar2], [xpos-18*scalar2, ypos+14*scalar2],
                         [xpos-26*scalar2, ypos+10*scalar2], [xpos-25*scalar2, ypos-1*scalar2], [xpos-9*scalar2, ypos-18*scalar2], [xpos+10*scalar2, ypos-12*scalar2], [xpos+19*scalar2, ypos-16*scalar2]]           
        if object_number == 17:
            asteroid1 = [[xpos+24*scalar2, ypos+2*scalar2], [xpos+11*scalar2, ypos+9*scalar2], [xpos+4*scalar2, ypos+24*scalar2], [xpos-9*scalar2, ypos+19*scalar2], [xpos-22*scalar2, ypos+5*scalar2], [xpos-13*scalar2, ypos-20*scalar2],
                         [xpos+3*scalar2, ypos-24*scalar2], [xpos+18*scalar2, ypos-13*scalar2]]          
        if object_number == 18:
            asteroid1 = [[xpos+23*scalar2, ypos-1*scalar2], [xpos+16*scalar2, ypos+19*scalar2], [xpos-4*scalar2, ypos+26*scalar2], [xpos-13*scalar2, ypos+13*scalar2], [xpos-26*scalar2, ypos+3*scalar2], [xpos-17*scalar2, ypos-20*scalar2],
                         [xpos-4*scalar2, ypos-23*scalar2], [xpos+16*scalar2, ypos-14*scalar2]]
        if object_number == 19:
            asteroid1 = [[xpos+27*scalar2, ypos+0*scalar2], [xpos+15*scalar2, ypos+-15*scalar2], [xpos+0*scalar2, ypos+-25*scalar2], [xpos+-21*scalar2, ypos+-15*scalar2], [xpos+-22*scalar2, ypos+0*scalar2],
                         [xpos+-19*scalar2, ypos+15*scalar2], [xpos+0*scalar2, ypos+24*scalar2], [xpos+21*scalar2, ypos+17*scalar2]]
        if object_number == 21:
            asteroid1 = [[xpos+33*scalar2, ypos-4*scalar2], [xpos+27*scalar2, ypos+23*scalar2], [xpos-6*scalar2, ypos+30*scalar2], [xpos-18*scalar2, ypos+24*scalar2], [xpos-32*scalar2, ypos+5*scalar2], [xpos-25*scalar2, ypos-18*scalar2],
                         [xpos+6*scalar2, ypos-30*scalar2], [xpos+20*scalar2, ypos-22*scalar2]]            
        if object_number == 22:
            asteroid1= [[xpos+20*scalar2, ypos], [xpos+24*scalar2, ypos+24*scalar2], [xpos-8*scalar2, ypos+32*scalar2], [xpos-23*scalar2, ypos+18*scalar2], [xpos-33*scalar2, ypos+5*scalar2], [xpos-26*scalar2, ypos-28*scalar2],
                        [xpos+3*scalar2, ypos-33*scalar2], [xpos+27*scalar2, ypos-22*scalar2]]
        if object_number == 23:
            asteroid1 = [[xpos+30*scalar2, ypos+0*scalar2], [xpos+26*scalar2, ypos+-22*scalar2], [xpos+3*scalar2, ypos+-33*scalar2], [xpos+-22*scalar2, ypos+-22*scalar2], [xpos+-38*scalar2, ypos+0*scalar2], [xpos+-27*scalar2, ypos+22*scalar2],
                         [xpos+3*scalar2, ypos+34*scalar2], [xpos+30*scalar2, ypos+23*scalar2]]
        if object_number == 24:
            asteroid1 = [[xpos+39*scalar2, ypos], [xpos+29*scalar2, ypos+-22*scalar2], [xpos, ypos-35*scalar2], [xpos-28*scalar2, ypos-20*scalar2],
                         [xpos-37*scalar2, ypos], [xpos-24*scalar2, ypos+23*scalar2], [xpos, ypos+35*scalar2], [xpos+19*scalar2, ypos+22*scalar2]]
        if object_number > 10:
            pygame.draw.aalines(screen, (255,255,255), True, asteroid1, 4)


#brings up functions for use without cluttering main file
from pgx import *


def objecthandler(object_list, width, height):
    # objects [xpos, ypos, xmom, ymom, type, serial number, time left (negative = dead), perishable (True or false)]
    if object_list:
        for i in range(int(len(object_list)/8)):
            if object_list[7 + (i * 8)]:
                object_list[6 + (i * 8)] -= 1            
            # edges section
            if object_list[0 + (i * 8)] > width:
                object_list[0 + (i * 8)] -= width
            if  object_list[0 + (i * 8)] < 0:
                object_list[0 + (i * 8)] += width
            if object_list[1 + (i * 8)] > height:
                object_list[1 + (i * 8)] -= height
            if object_list[1 + (i * 8)] < 0:
                object_list[1 + (i * 8)] += height
            # positioner
            object_list[0 + (i * 8)] += object_list[2 + (i * 8)]
            object_list[1 + (i * 8)] -= object_list[3 + (i * 8)]
    return object_list


def particlemaker(xpos, ypos, xmom, ymom):
    # particle settings
    particle_lifespan = 45
    random_factor = 30 # higher number = less random
    max_particles = 6
    max_deviation = 2
    # particle settings
    printerlist_add = []
    for i in range(random.randint(max_particles - max_deviation, max_particles)):
        printerlist_add += [xpos, ypos, xmom + ((random.randint(-20, 20))/random_factor), ymom + ((random.randint(-20, 20))/random_factor), 4, "N/A", particle_lifespan, True]      
    return printerlist_add

def asteroidspeedmaker(max_asteroid_spd):
    asteroid_speedset = []
    if random.randint(0,1) == 1:# if else statements institute a minimum horizontal and vertical speed (separately) of half the asteroid high speed
        asteroid_speedset.append(random.randint(int(max_asteroid_spd/2), max_asteroid_spd)/100)
    else:
        asteroid_speedset.append(random.randint(-1*max_asteroid_spd, int(-1*max_asteroid_spd/2))/100)
    if random.randint(0,1) == 1:
        asteroid_speedset.append(random.randint(int(max_asteroid_spd/2), max_asteroid_spd)/100)
    else:
        asteroid_speedset.append(random.randint(-1*max_asteroid_spd, int(-1*max_asteroid_spd/2))/100)
    return asteroid_speedset

def asteroidsplitter(scalarscalar, object_list, i, listed_asteroids):
    listed_count = len(listed_asteroids) - 1
    printerlist_add = [object_list[(i * 8)], object_list[1+(i * 8)], object_list[2+(i * 8)]+((random.randint(round(-10*scalarscalar), round(10*scalarscalar)))/15),
                        object_list[3+(i * 8)]+((random.randint(round(-10*scalarscalar), round(10*scalarscalar)))/15), listed_asteroids[random.randint(0, listed_count)], "N/A", 1, False] 
    printerlist_add += [object_list[(i * 8)], object_list[1+(i * 8)], object_list[2+(i * 8)]+((random.randint(round(-10*scalarscalar), round(10*scalarscalar)))/15),
                        object_list[3+(i * 8)]+((random.randint(round(-10*scalarscalar), round(10*scalarscalar)))/15), listed_asteroids[random.randint(0, listed_count)], "N/A", 1, False]
    return printerlist_add

def explosion_sounds():
    explosion1 = pygame.mixer.Sound(handlePath("Assets\\Bomb1.wav"))
    explosion2 = pygame.mixer.Sound(handlePath("Assets\\Bomb2.wav"))
    explosion1.set_volume(0.05)
    explosion2.set_volume(0.05)
    explosion_picker = random.randint(0,1)
    if explosion_picker == 0:
        explosion1.play()
    if explosion_picker == 1:
        explosion2.play()


def score_printer(high_scores, high_initials):
    for i in range(len(high_initials)):
        text_input = [(740, 200+i*70), str(high_scores[i]), 4]
        Texthelper.write(screen, text_input)
        text_input = [(1020, 200+i*70), str(high_initials[i]), 4]
        Texthelper.write(screen, text_input) 

def main():
    global screen
    file_settings = filehelper.get(0) #grabs settings from file

    #sets adjustable settings
    width = int(file_settings[0])
    height = int(file_settings[1])
    max_asteroids = int(file_settings[2])
    ship_drag = file_settings[3]
    if ship_drag == "true":
        drag = [1, 5]
    if ship_drag != "true":
        drag = []

    #scaling
    scalarscalar = height / 1080
    scalar2 = 1.5 * scalarscalar # controls asteroid size
    scalar3 = 1.2 * scalarscalar # controls ship size
    alien_size = [1.2 * scalarscalar, 1.8 * scalarscalar]

    #texthelper setup for scaling
    Texthelper.scalar = scalarscalar
    Texthelper.width = width
    Texthelper.height = height

    # settings
    '''
    max_speed = 4 * scalarscalar
    missile_lifespan = 130 * scalarscalar
    missile_accel = 7 * scalarscalar
    step_x = 0.08 * scalarscalar
    step_y = 0.08 * scalarscalar
    step_r = 2.3 
    step_drag = 0.004 * scalarscalar
    max_asteroid_spd = 270 * scalarscalar
    ship_safetymargin = 250 * scalarscalar
    color = (0, 0, 0) # for background
    shield_lifespan = 300
    extratime_setter = 25
    '''

    #expc = 1/0.6 #expected clock 1/decimal percent of expected
    expc = 1

    max_speed = 4 * scalarscalar * expc
    missile_lifespan = 130 * scalarscalar * expc
    missile_accel = 7 * scalarscalar * expc
    step_x = 0.08 * scalarscalar * expc
    step_y = 0.08 * scalarscalar * expc
    step_r = 2.3  * expc
    step_drag = 0.004 * scalarscalar * expc
    max_asteroid_spd = 270 * scalarscalar * expc
    ship_safetymargin = 250 * scalarscalar *expc
    color = (0, 0, 0) # for background
    shield_lifespan = 300
    extratime_setter = 25    

    # pygame setup
    pygame.init()
    pygame.display.set_caption("Asteroids")
    logo = loadImage("Assets\\asteroid1-small.png")
    pygame.display.set_icon(logo)
    if width == 0 or height == 0:
        screen_sizes = pygame.display.list_modes()
        screen_sizes = screen_sizes[0]
        width = screen_sizes[0]
        height = screen_sizes[1]
    if file_settings[4] == "true":
        screen = pygame.display.set_mode([width, height], pygame.NOFRAME | pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode([width, height])
        
    # variable setup
    s_asteroids = [11, 12, 13, 14]
    m_asteroids = [16, 17, 18, 19]
    l_asteroids = [21, 22, 23, 24]
    all_asteroids = s_asteroids + m_asteroids + l_asteroids
    status = "menuinit"
    lower_rotation_constant = math.degrees(math.asin(10 / 325 ** 0.5))
    flame_rotation_constant = math.degrees(math.atan(6 / 5))
    flame = False
    menu_music_fadeout_OG = 1200
    menu_music_fadeout = menu_music_fadeout_OG
    clock = pygame.time.Clock()

    #collision detection helper
    def collinfo(i):
        if object_list[4 + (i * 8)] in s_asteroids:
            watch_radius = [18*scalar2, -700, 3]
        elif object_list[4 + (i * 8)] in m_asteroids:
            watch_radius = [25*scalar2, -710, 3]
        elif object_list[4 + (i * 8)] in l_asteroids:
            watch_radius = [35*scalar2, -720, 3]
        elif object_list[4 + (i * 8)] == 1:
            watch_radius = [20*scalar3, -670, 1]
        elif object_list[4 + (i * 8)] == 6:
            watch_radius = [18*scalar1, -730, 2]
        elif object_list[4 + (i * 8)] == 8:
            watch_radius = [1, -610, 2]
        elif object_list[4 + (i * 8)] == 2:
            watch_radius = [1, -620, 1]
        else:
            watch_radius = []
        return watch_radius
    
    running = True
    while running:
        clock.tick(100)
        collect_inputs()
     
        if status == "menuinit":
            # sound
            pygame.mixer.init()
            menu_music = pygame.mixer.Sound(handlePath("Assets\\AsteroidsTitle.wav"))
            menu_music.play(-1)
            menu_music.set_volume(0.4)
            menu_music_fadeout = menu_music_fadeout_OG
            pygame.mouse.set_visible(True)
            countervar = 0
            object_list2 = []
            while countervar < random.randint((max_asteroids*2)-2, max_asteroids * 2): #while there are less asteroids than a set random number of aseroids, continue this loop
                selector_man = random.randint(1,2) #selector_man either = 1 or 2
                if selector_man == 1: #if selector_man = 1, then create random sized asteroids in random location
                    object_list_add = [random.randint(0, width), random.randint(0, height), random.randint(-1 * max_asteroid_spd, max_asteroid_spd)/600, random.randint(-1 * max_asteroid_spd, max_asteroid_spd)/600]
                    object_list_add += [l_asteroids[random.randint(0, len(l_asteroids)-1)], 0, 1, False]
                if selector_man == 2: #if selector_man = 2, then create random sized asteroids in random location
                    object_list_add = [random.randint(0, width), random.randint(0, height), random.randint(-1 * max_asteroid_spd, max_asteroid_spd)/600, random.randint(-1 * max_asteroid_spd, max_asteroid_spd)/600]
                    object_list_add += [m_asteroids[random.randint(0, len(m_asteroids)-1)], 0, 1, False]                    
                countervar += 1 #the asteroid created is counted
                object_list2 += object_list_add #add the asteroid to existing object list of asteroids
            status = "menu" 

        if status == "menu": #if game is in menu
            # moving asteroids background
            objecthandler(object_list2, width, height)
            ship_pointlist = [[50, 50 - 30], [50 + 15, 50 + 10], [50, 50], [50 - 15, 50 + 10]]
            temp_scalar2 = 1 #not necessary, just defaults
            temp_scalar1 = 1 #so the printer doesn't have a fit
            printer(ship_pointlist, object_list2, color, scalar3, temp_scalar2, temp_scalar1, scalarscalar)

            # actual text
            text_input = [(360, 540-200), "Asteroids", 10]
            Texthelper.write(screen, text_input)
            
            # buttons
            #Texthelper.last_click = click
            #click = new_mouse2()
            
            text_input = [(410, 540-50), "Play", 3]
            if Texthelper.writeButton(screen, text_input):
                status = "gameinit"
                menu_music.fadeout(menu_music_fadeout)
            text_input = [(410, 550), "Quit to desktop", 3]
            if Texthelper.writeButton(screen, text_input): #if "quit to desktop" is clicked           
                pygame.quit() #stop the program
                raise SystemExit #close the program
            text_input = [(960-550, 540+70), "Options", 3] #display "options" on menu
            if Texthelper.writeButton(screen, text_input): #if "options" is clicked
                status = "optionsinit" #initialize options page
                back_selector = "menuinit" #used in options page 
                menu_music.fadeout(menu_music_fadeout) #stop music
            text_input = [(960-550, 540+130), "Tutorial", 3] #display "tutorial" on menu
            if Texthelper.writeButton(screen, text_input): #if "tutorial" clicked
                status = "tutorial"
                menu_music.fadeout(menu_music_fadeout)
            text_input = [(960-550, 540+190), "High Scores", 3]
            if Texthelper.writeButton(screen, text_input):
                status = "menuscorescreen"
                menu_music.fadeout(menu_music_fadeout)
                high_scores = filehelper.get(1)
                high_initials = filehelper.get(2)
            pygame.display.flip()

        if status == "menuscorescreen":
            screen.fill(color)
            score_printer(high_scores, high_initials)
            # back button
            text_input = [(20, 20), "Back", 3]
            if Texthelper.writeButton(screen, text_input) == True:
                status = "menuinit"
            pygame.display.flip()

        if status == "optionsinit":
            edit_selector = ""
            previous_ticks = pygame.time.get_ticks()
            file_settings2 = file_settings[0:]
            
            optionwidth = InputGetter([(960-200, 240), str(file_settings2[0]), 3], "int")
            optionheight = InputGetter([(960, 240), str(file_settings2[1]), 3], "int")
            optionmaxasteroids = InputGetter([(960-150, 310), str(file_settings2[2]), 3], "int")
            optiondrag = InputGetter([(960-200, 380), str(file_settings2[3]), 3], "str")
            optionfullscreen = InputGetter([(960-200, 450), str(file_settings2[4]), 3], "str")
            optionlist = [optionwidth, optionheight, optionmaxasteroids, optiondrag, optionfullscreen]
            
            status = "optionspage"

        if status == "optionspage":
            screen.fill(color)
            
            text_input = [(960-600, 140), "Options", 6]
            Texthelper.write(screen, text_input)
            text_input = [(960, 190), "All changes require restart", 2]
            Texthelper.write(screen, text_input)
            Texthelper.write(screen, [(300, 800), "To edit a value click on the value and then type", 2])

            text_input = [(960-600, 240), "Resolution", 3]
            Texthelper.write(screen, text_input)            
            optionwidth.update(screen)
            optionheight.update(screen)

            text_input = [(960-600, 310), "Max Asteroids", 3]
            Texthelper.write(screen, text_input)
            optionmaxasteroids.update(screen)

            text_input = [(960-600, 380), "Ship Drag", 3]
            Texthelper.write(screen, text_input)
            text_input = [(960-450, 420), "True or false", 1.5]
            Texthelper.write(screen, text_input)           
            optiondrag.update(screen)

            text_input = [(960-600, 450), "Fullscreen", 3]
            Texthelper.write(screen, text_input)
            text_input = [(960-450, 490), "True or false", 1.5]
            Texthelper.write(screen, text_input)            
            optionfullscreen.update(screen)

            for i in range(len(optionlist)):
                savinghelper = optionlist[i].getText()
                if savinghelper.isdigit() == True:
                    file_settings2[i] = int(savinghelper)
                else:
                    file_settings2[i]  = savinghelper            

            if file_settings != file_settings2:
                text_input = [(960, 140), "save changes", 3]
                if Texthelper.writeButton(screen, text_input):
                    filehelper.set(file_settings2, 0)
                    file_settings = file_settings2[0:]
                    status = "optionsinit"

            text_input = [(960-600, 900), "Reset to Defaults", 3]
            if Texthelper.writeButton(screen, text_input):
                file_settings = filehelper.get(3)
                filehelper.set(file_settings, 0)
                status = "optionsinit"                    
                        
            # back button
            text_input = [(20, 20), "Back", 3]
            if Texthelper.writeButton(screen, text_input) == True:
                status = back_selector

            pygame.display.flip()
            
        if status == "pauseinit":
            pygame.mouse.set_visible(True)
            alien_alarm.stop()
            alientimer = 0            
            text_input = [("center", 540-136), "Paused", 6]
            Texthelper.write(screen, text_input)
            pygame.display.flip()
            pygame.time.wait(200)
            text_input = [("center", 540-55), "Resume", 2]
            Texthelper.write(screen, text_input)
            pygame.display.flip()
            pygame.time.wait(200)
            text_input = [("center", 540-20), "Restart", 2]
            Texthelper.write(screen, text_input)
            pygame.display.flip()
            pygame.time.wait(200)            
            text_input = [("center", 540+15), "Quit to desktop", 2]
            Texthelper.write(screen, text_input)
            pygame.display.flip()
            pygame.time.wait(200)
            text_input = [("center", 540+50), "Quit to menu", 2]
            Texthelper.write(screen, text_input)
            pygame.display.flip()
            status = "paused"

        if status == "paused":
            text_input = [("center", 540-55), "Resume", 2]
            if Texthelper.writeButton(screen, text_input):
                pygame.mouse.set_visible(False)
                status = "game"
            text_input = [("center", 540-20), "Restart", 2]
            if Texthelper.writeButton(screen, text_input):
                status = "gameinit"   
            text_input = [("center", 540+15), "Quit to desktop", 2]
            if Texthelper.writeButton(screen, text_input):
                pygame.quit()
                raise SystemExit
            text_input = [("center", 540+50), "Quit to menu", 2]
            if Texthelper.writeButton(screen, text_input):
                status = "menuinit"
            pygame.display.flip()

        if status == "highscorecheck":
            alien_alarm.stop()
            pygame.mouse.set_visible(True)
            high_scores = filehelper.get(1)
            high_initials = filehelper.get(2)
            if score > high_scores[4]:
                high_scores.append(score)
                high_scores.sort(reverse=True)
                high_scores.pop()
                score_index =high_scores.index(score)
                high_initials = high_initials[:score_index] + [""] + high_initials[score_index:]
                high_initials.pop()
                status = "highscorescreen"
            else:
                status = "gameoverinit"

        if status == "highscorescreen":
            inputvar = keyboard()
            screen.fill(color)
            alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            printer(ship_pointlist, object_list, color, scalar3, scalar2, scalar1, scalarscalar)

            text_input = [(574, 70), "High Score Achieved", 4]
            Texthelper.write(screen, text_input)
            text_input = [(567, 130), "Please enter your initials", 3]
            Texthelper.write(screen, text_input)
            
            # calls a function to print out the scores
            score_printer(high_scores, high_initials)
          
            if len(inputvar) == 1 and len(inputvar[0]) == 1 and inputvar != previous_inputvar and inputvar[0] in alphabet_list:
                high_initials[score_index] += inputvar[0]
            if len(inputvar) == 1 and inputvar != previous_inputvar:
                if inputvar[0] ==  "back" or inputvar[0] == "delete":                    
                    high_initials[score_index] = high_initials[score_index][:-1]
            if len(high_initials[score_index]) == 3:
                text_input = [(620, 700), "Press Enter to Continue", 3]
                Texthelper.write(screen, text_input)
            if len(inputvar) == 1 and len(high_initials[score_index]) == 3:
                if inputvar[0] == "enter":
                    filehelper.set(high_scores, 1)
                    filehelper.set(high_initials, 2)
                    printer(ship_pointlist, object_list, color, scalar3, scalar2, scalar1, scalarscalar)
                    status = "gameoverinit"
                 
            pygame.display.flip()
            previous_inputvar = inputvar #helps with distinct keyclicks

        if status == "gameoverinit":            
            text_input = [("center", 540-136), "Game over", 6]
            Texthelper.write(screen, text_input)            
            pygame.display.flip()
            pygame.time.wait(200)
            text_input = [("center", 540-55), "Play again", 2]
            Texthelper.write(screen, text_input)
            pygame.display.flip()
            pygame.time.wait(200)
            text_input = [("center", 540-20), "Quit to desktop", 2]
            Texthelper.write(screen, text_input)
            pygame.display.flip()
            pygame.time.wait(200)
            text_input = [("center", 540+15), "Quit to menu", 2]
            Texthelper.write(screen, text_input)
            pygame.display.flip()
            status = "gameover"

        if status == "gameover":
            text_input = [("center", 540-55), "Play again", 2]
            if Texthelper.writeButton(screen, text_input):
                status = "gameinit"
                
            text_input = [("center", 540-20), "Quit to desktop", 2]
            if Texthelper.writeButton(screen, text_input):
                pygame.quit()
                raise SystemExit
            
            text_input = [("center", 540+15), "Quit to menu", 2]
            if Texthelper.writeButton(screen, text_input):
                status = "menuinit"
            pygame.display.flip()

        if status == "tutorial":
            screen.fill(color)
            blockdim1 = 100 * scalarscalar
            thickness = round(5*scalarscalar)
            if thickness == 0:
                thickness = 1
            # QWE movement block
            temp_1 = (50, 160) #positions whole block
            temp_12 = (temp_1[0]*scalarscalar, temp_1[1]*scalarscalar)  #for scaling
            pygame.draw.rect(screen, (255,255,255), [temp_12[0], temp_12[1], blockdim1, blockdim1], thickness) 
            Texthelper.write(screen, [(temp_1[0]+30, temp_1[1]+20), "Q", 5])
            Texthelper.write(screen, [(temp_1[0]+30, temp_1[1]+110), "Left", 1])
            Texthelper.write(screen, [(temp_1[0]+7, temp_1[1]+130), "Rotation", 1])
            pygame.draw.rect(screen, (255,255,255), [temp_12[0]+130*scalarscalar, temp_12[1], blockdim1, blockdim1], thickness) 
            Texthelper.write(screen, [(temp_1[0]+160, temp_1[1]+20), "W", 5])
            Texthelper.write(screen, [(temp_1[0]+143, temp_1[1]+110), "Forward", 1])            
            pygame.draw.rect(screen, (255,255,255), [temp_12[0]+260*scalarscalar, temp_12[1], blockdim1, blockdim1], thickness) 
            Texthelper.write(screen, [(temp_1[0]+290, temp_1[1]+20), "E", 5])
            Texthelper.write(screen, [(temp_1[0]+284, temp_1[1]+110), "Right", 1])
            Texthelper.write(screen, [(temp_1[0]+267, temp_1[1]+130), "Rotation", 1])            

            Texthelper.write(screen, [(500,185), "or", 3])

            # arrow key block (no positioner)
            pygame.draw.rect(screen, (255,255,255), [640*scalarscalar, 230*scalarscalar, blockdim1, blockdim1], thickness) 
            pygame.draw.polygon(screen, (255,255,255), [(660*scalarscalar,280*scalarscalar),(720*scalarscalar,250*scalarscalar),(720*scalarscalar,310*scalarscalar)], 0) 
            Texthelper.write(screen, [(670,340), "Left", 1])
            Texthelper.write(screen, [(647,360), "Rotation", 1])   
            pygame.draw.rect(screen, (255,255,255), [770*scalarscalar, 100*scalarscalar, 100*scalarscalar, 100*scalarscalar], thickness) 
            pygame.draw.polygon(screen, (255,255,255), [(820*scalarscalar,120*scalarscalar),(850*scalarscalar,180*scalarscalar),(790*scalarscalar,180*scalarscalar)], 0) 
            Texthelper.write(screen, [(783,78), "Forward", 1]) 
            pygame.draw.rect(screen, (255,255,255), [770*scalarscalar, 230*scalarscalar, blockdim1, blockdim1], thickness)
            pygame.draw.polygon(screen, (255,255,255), [(820*scalarscalar,310*scalarscalar),(850*scalarscalar,250*scalarscalar),(790*scalarscalar,250*scalarscalar)], 0)
            pygame.draw.rect(screen, (255,255,255), [900*scalarscalar, 230*scalarscalar, blockdim1, blockdim1], thickness)
            pygame.draw.polygon(screen, (255,255,255), [(980*scalarscalar,280*scalarscalar),(920*scalarscalar,250*scalarscalar),(920*scalarscalar,310*scalarscalar)], 0)
            Texthelper.write(screen, [(924,340), "Right", 1])
            Texthelper.write(screen, [(907,360), "Rotation", 1])

            Texthelper.write(screen, [(1080,185), "to move", 3])

            # row 2 - firing block
            temp_3 = (140, 450) # positions block
            temp_32 = (temp_3[0]*scalarscalar, temp_3[1]*scalarscalar)
            pygame.draw.rect(screen, (255,255,255), [temp_32[0], temp_32[1], 7*blockdim1, blockdim1], thickness)
            Texthelper.write(screen, [(temp_3[0]+298, temp_3[1]+38), "space", 2])
            Texthelper.write(screen, [(temp_3[0]+800, temp_3[1]+30), "to fire", 3])

            # row 3 - pausing block
            temp_4 = (290, 630) #positions block
            temp_42 = (temp_4[0]*scalarscalar, temp_4[1]*scalarscalar)
            pygame.draw.rect(screen, (255,255,255), [temp_42[0], temp_42[1], blockdim1, blockdim1], thickness)
            Texthelper.write(screen, [(temp_4[0]+8, temp_4[1]+33.2), "esc", 2.8])
            Texthelper.write(screen, [(temp_4[0]+180, temp_4[1]+32), "or", 3])
            pygame.draw.rect(screen, (255,255,255), [temp_42[0]+312*scalarscalar, temp_42[1], blockdim1, blockdim1], thickness) 
            Texthelper.write(screen, [(temp_4[0]+342, temp_4[1]+20), "P", 5])
            Texthelper.write(screen, [(temp_4[0]+484, temp_4[1]+32), "to pause", 3])

            # back button
            text_input = [(20, 20), "Back", 3]
            if Texthelper.writeButton(screen, text_input) == True:
                status = "menuinit"

            pygame.display.flip()
            

        if status == "gameinit":       
            # changing variable setup
            object_list = [width / 2, height / 2, 0, 0, 1, 1, 1, False] # ship starter
            for i in range(3):
                object_list += [50*scalarscalar+(i*50*scalar3), height-50*scalarscalar, 0, 0, 3, 1, 1, False]            
            level = 0
            score = 0
            rotation = 90
            serialnumber = 2
            extratime = extratime_setter
            extratime_trigger = False
            previous_tick = 0
            previous_tick2 = 0
            pygame.mouse.set_visible(False)

            # sound
            beat_timer = 250
            max_beat_timer = beat_timer
            beat1 = pygame.mixer.Sound(handlePath("Assets\\Beat1loud.wav"))
            beat1.set_volume(0.9)
            beat2 = pygame.mixer.Sound(handlePath("Assets\\Beat2loud.wav"))
            beat2.set_volume(0.9)
            missilesound = pygame.mixer.Sound(handlePath("Assets\\missilesound.wav"))
            missilesound.set_volume(0.35)
            enginesound = pygame.mixer.Sound(handlePath("Assets\\enginesoundloud.wav"))
            enginesound.set_volume(0.2)
            timer1 = 0
            alien_alarm = pygame.mixer.Sound(handlePath("Assets\\alien_alarm.wav"))
            alien_alarm.set_volume(0.10)
            alientimer = 0

            # aliens
            scalar1 = 0 #just default value so no errors on startup            
            previous_inputvar = []
            alien_clock = ""
            alien_event = ""
            alien_index = ""

            status = "game"

        if status == "game":
            # leveler
            asteroids_count = 0
            for i in range(int(len(object_list)/8)):
                if 26 > object_list[4 + (i * 8)] > 10:
                    asteroids_count += 1          
            if asteroids_count == 0:
                level += 1
                countervar = 0
                while countervar < random.randint(max_asteroids - 2, max_asteroids):
                    asteroid_speedset = asteroidspeedmaker(max_asteroid_spd)                    
                    object_list_add = [random.randint(0, width), random.randint(0, height), asteroid_speedset[0], asteroid_speedset[1]]
                    object_list_add += [l_asteroids[random.randint(0, len(l_asteroids)-1)], 3, 1, False] 
                    xdiff = object_list[0] - object_list_add[0]
                    ydiff = object_list[1] - object_list_add[1]
                    distance = ((xdiff ** 2) + (ydiff ** 2)) ** 0.5
                    if distance > ship_safetymargin:
                        countervar += 1
                        object_list += object_list_add
                if object_list[4] == 1 or object_list[4] == 3:
                    object_list[4] = 5
                    object_list[5] = 3
                    object_list[6] = shield_lifespan
                    object_list[7] = True
            # leveler

            # sound
            if menu_music_fadeout >= 0:
                menu_music_fadeout -= 10
            if menu_music_fadeout < 0:
                if beat_timer == max_beat_timer:
                    beat2.stop()
                    beat1.play()
                beat_timer -= 1
                if beat_timer == int(max_beat_timer/2):
                    beat1.stop()
                    beat2.play()
                if beat_timer <= 0:
                    beat_timer = max_beat_timer    
            # sound
            
            # input handling
            inputvar = keyboard()
            thrust_vector = (math.cos(math.radians(rotation)), math.sin(math.radians(rotation)))
            ticks = pygame.time.get_ticks()
            if inputvar:
                if "w" in inputvar or "uparrow" in inputvar:
                    object_list[2] += step_x * thrust_vector[0]
                    object_list[3] += step_y * thrust_vector[1]
                    flame = True
                if "e" in inputvar or "rightarrow" in inputvar:
                    rotation -= step_r
                if "q" in inputvar or "leftarrow" in inputvar:
                    rotation += step_r
                if "escape" in inputvar or "p" in inputvar or "windows" in inputvar and len(inputvar) == 1:
                    status = "pauseinit"
                if "space" in inputvar and (ticks - previous_tick) > 360:
                    xmom_miss = object_list[2] + (thrust_vector[0] * missile_accel)
                    ymom_miss = object_list[3] + (thrust_vector[1] * missile_accel)
                    object_list_addition = [object_list[0]+top_xrot*scalar3, object_list[1]-top_yrot*scalar3, xmom_miss, ymom_miss, 2, serialnumber, missile_lifespan, True]
                    object_list += object_list_addition
                    serialnumber += 1
                    previous_tick = ticks
                    missilesound.stop()
                    missilesound.play()
                if "shift" in inputvar and "c" in inputvar and (ticks - previous_tick2) > 360:
                    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                    while color[0] + color[1] + color[2] > 150:
                        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                    previous_tick2 = ticks                    
            # input handling

            # alien section
            #searches through list for where the alien is
            alien_index = "" #scrubbes results, so start fresh
            for i in range(int(len(object_list)/8)):
                if object_list[(i*8)+4] == 6:
                    alien_index = i

            #Alien sound
            if alien_index != "" and alientimer == 0:
                alien_alarm.play()
                alientimer += 1
            if alien_index != "" and alientimer > 0:
                alientimer += 1
            if alien_index == "" and alientimer > 0:
                alien_alarm.stop()
                alientimer = 0
            if alien_index != "" and alientimer == 1000:
                alien_alarm.stop()
                alientimer = 0
                
            #alien creation section
            if alien_index == "" and random.randint(0,1500) == 14:
                scalar1 = random.randint(round(alien_size[0]*100), round(alien_size[1]*100)) # controls alien size
                scalar1 = scalar1/100
                #positions x and y somewhere along perimeter of screen
                if random.randint(0,1) == 0:
                    alien_x = random.randint(0,width)
                    if random.randint(0,1) == 0:
                        alien_y = 0
                    else:
                        alien_y = height
                else:
                    alien_y = random.randint(0,height)
                    if random.randint(0,1) == 0:
                        alien_x = 0
                    else:
                        alien_x = width
                asteroid_speedset = asteroidspeedmaker(max_asteroid_spd)   
                object_list += [alien_x, alien_y, asteroid_speedset[0], asteroid_speedset[1], 6, "NA", 10, False]
                alien_momentum = [asteroid_speedset[0], asteroid_speedset[1]]
                                 
            if alien_clock == "" and random.randint(0,400) == 1 and alien_index != "":
                alien_event = "zig-zag"
                zig_zagginess = [random.randint(25, 175), random.randint(25, 175)]
                zig_zagginess[0] = zig_zagginess[0]/100
                zig_zagginess[1] = zig_zagginess[1]/100
                alien_clock = 0
                
            if alien_event == "zig-zag":
                #in case alien is killed while zig zagging
                if alien_index == "":
                    alien_clock = ""
                    alien_event = ""
                    
                if alien_clock == 0:
                    object_list[alien_index*8+2] = object_list[alien_index*8+2] * zig_zagginess[0] 
                    object_list[alien_index*8+3] = alien_momentum[1] * zig_zagginess[1] 
                
                if alien_clock == 150:
                    object_list[alien_index*8+2] = alien_momentum[0] * zig_zagginess[1]
                    object_list[alien_index*8+3] = alien_momentum[1] * zig_zagginess[0] 
                
                if alien_clock == 300:
                    object_list[alien_index*8+2] = alien_momentum[0]
                    object_list[alien_index*8+3] = alien_momentum[1]
                    alien_clock = ""
                    alien_event = ""

            #targeting section
            m = 0
            n = 0
            random10 = random.randint(0,100)
            alien_target = ""
            j = 0
            targets = []
            while j + 1 <= int(len(object_list)/8) and alien_index != "":
                if (object_list[j*8+4] >= 10 and random10 == 3) or j == 0:
                    asteroid_distance = int(math.pow(math.pow(object_list[j * 8] - object_list[alien_index*8], 2) + math.pow(object_list[alien_index*8+1] - object_list[(j * 8) + 1] , 2), 0.5))
                    asteroid_help = (asteroid_distance, j)
                    targets.append(asteroid_help)
                    targets.sort()
                    #object_list
                    if len(targets) >= 3:
                        m, n = targets[random.randint(0,2)]
                    else:
                        m, n = targets[0]
                j = j + 1
            alien_target = [object_list[(n*8)], object_list[(n*8)+1], object_list[(n*8)+2], object_list[(n*8)+3]] #xpos, ypos, xmom, ymom

            #shooting section
            if random10 == 3 and alien_index != "" and alien_target != "":
                asteroid_deltaPosition = [alien_target[0] - object_list[alien_index*8], object_list[alien_index*8+1] - alien_target[1]]
                asteroid_distance = math.pow(math.pow(asteroid_deltaPosition[0],2) + math.pow(asteroid_deltaPosition[1],2), 0.5)
                colliding = False
                coolTicker = 0
                while colliding == False:
                    asteroid_deltaPosition = [(alien_target[0] + alien_target[2]*coolTicker) - (object_list[alien_index*8]),
                                              (alien_target[1] - alien_target[3]*coolTicker) - (object_list[alien_index*8+1])]                    
                    #if distance between ship and future asteroid pos is less than distance a missile could travel in that time
                    if math.pow(math.pow(asteroid_deltaPosition[0],2) + math.pow(asteroid_deltaPosition[1],2), 0.5) < (missile_accel * coolTicker):
                        colliding = True

                        #commented out section below gives a graphical representation of the shot firing process
                        #pygame.draw.circle(screen, (255,255,255),(int(object_list[alien_index*8]), int(object_list[alien_index*8+1])), int(missile_accel*coolTicker), 4)
                        #pygame.draw.circle(screen, (120, 49, 88), (int(alien_target[0]), int(alien_target[1])), 20, 0)
                        #pygame.draw.circle(screen, (50, 200, 30), (int(object_list[alien_index*8]+asteroid_deltaPosition[0]), int(object_list[alien_index*8+1]+asteroid_deltaPosition[1])), 20, 0)
                        #pygame.display.flip()
                        
                        xmom_miss = (asteroid_deltaPosition[0] / coolTicker)
                        ymom_miss = -(asteroid_deltaPosition[1] / coolTicker)
                        object_list_addition = [object_list[alien_index*8], object_list[alien_index*8+1], xmom_miss, ymom_miss, 8, serialnumber, missile_lifespan, True]
                        object_list += object_list_addition
                        missilesound.stop()
                        missilesound.play()  
                    
                    elif coolTicker > 5000:
                        break
                    
                    else:
                        coolTicker += 1                           
            # alien section
                    
            # speed limit section
            if object_list[2] > max_speed:
                object_list[2] = max_speed
            if object_list[2] < -1 * max_speed:
                object_list[2] =  -1 * max_speed
            if object_list[3] > max_speed:
                object_list[3] = max_speed
            if object_list[3] < -1 * max_speed:
                object_list[3] = -1 * max_speed
            # speed limit section
        
            # rotation section
            top_xrot = 30 * math.cos(math.radians(rotation))
            top_yrot = 30 * math.sin(math.radians(rotation))
            right_yrot = 325 ** (1/2.0) * math.cos(math.radians(rotation - lower_rotation_constant))
            right_xrot = 325 ** (1/2.0) * math.sin(math.radians(rotation - lower_rotation_constant))
            left_yrot = 325 ** (1/2.0) * math.cos(math.radians(rotation + 180 + lower_rotation_constant))
            left_xrot = 325 ** (1/2.0) * math.sin(math.radians(rotation + 180 + lower_rotation_constant))
            if flame:
                bottomflame_xrot = 20 * math.cos(math.radians(rotation))
                bottomflame_yrot = 20 * math.sin(math.radians(rotation))
                rightflame_xrot = 61 ** (1/2.0) * math.sin(math.radians(rotation - flame_rotation_constant))
                rightflame_yrot = 61 ** (1/2.0) * math.cos(math.radians(rotation - flame_rotation_constant))
                leftflame_xrot = 61 ** (1/2.0) * math.sin(math.radians(rotation + 180 + flame_rotation_constant))
                leftflame_yrot = 61 ** (1/2.0) * math.cos(math.radians(rotation + 180 + flame_rotation_constant))
            # rotation section

            # collision detection           
            for i in range(int(len(object_list)/8)):
                watch_radius = collinfo(i) 
                if watch_radius:
                    for i2 in range(int(len(object_list)/8)):
                        watch_radius2 = collinfo(i2)
                        if watch_radius2:
                            #exempting collisions section
                            if object_list[4 + (i * 8)] in all_asteroids and object_list[4 + (i2 * 8)] in all_asteroids: #exempts asteroid on asteroid collisions
                                pass
                            elif object_list[4 + (i * 8)] == 2 and object_list[4 + (i2 * 8)] == 1: #exempts ship missile and ship collisions
                                pass
                            elif object_list[4 + (i * 8)] == 1 and object_list[4 + (i2 * 8)] == 2: #exempts ship missile and ship collisions
                                pass
                            elif i == i2: #exempts colliding with yourself
                                pass
                            elif object_list[4 + (i * 8)] == 6 and object_list[4 + (i2 * 8)] == 8: #exempts alien missile and alien collisions
                                pass
                            elif object_list[4 + (i * 8)] == 8 and object_list[4 + (i2 * 8)] == 6: #exempts alien missile and alien collisions
                                pass
                            #elif object_list[4 + (i * 8)] == 1 or object_list[4 + (i2 * 8)] == 1: <----Grants immortality
                                #pass                            
                            else:
                                hitrange = watch_radius[0] + watch_radius2[0]
                                if hitrange >= object_list[(i*8)] - object_list[(i2*8)] >= -hitrange or hitrange >= object_list[(i*8)+1] - object_list[(i2*8)+1] >= -hitrange:
                                    xdiff = object_list[(i * 8)] - object_list[(i2 * 8)]
                                    ydiff = object_list[1 + (i * 8)] - object_list[1 + (i2 * 8)]
                                    distance = ((xdiff ** 2) + (ydiff ** 2)) ** 0.5
                                    if distance < hitrange:
                                        object_list[(i*8)+6] = watch_radius[1]-watch_radius2[2]
                                        object_list[(i2*8)+6] = watch_radius2[1]-watch_radius[2]
            # collision detection
            
            # collision detection consequences
            printerlist_add = []
            for i in range(int(len(object_list)/8)):
                if round(object_list[(i*8)+6], -1) == -700: # small asteroid destruction
                    printerlist_add += particlemaker(object_list[(i * 8)], object_list[1+(i * 8)], object_list[2+(i * 8)], object_list[3+(i * 8)])
                    if abs(object_list[(i*8)+6])%10 == 1:
                        score += 100
                    explosion_sounds()                    
                if round(object_list[(i*8)+6], -1) == -710: # medium asteroid destruction
                    printerlist_add += asteroidsplitter(scalarscalar, object_list, i, s_asteroids)
                    printerlist_add += particlemaker(object_list[(i * 8)], object_list[1+(i * 8)], object_list[2+(i * 8)], object_list[3+(i * 8)])                      
                    if abs(object_list[(i*8)+6])%10 == 1:
                        score += 50
                    explosion_sounds()                    
                if round(object_list[(i*8)+6], -1) == -720: # large asteroid destruction                 
                    printerlist_add += asteroidsplitter(scalarscalar, object_list, i, m_asteroids)
                    printerlist_add += particlemaker(object_list[(i * 8)], object_list[1+(i * 8)], object_list[2+(i * 8)], object_list[3+(i * 8)])
                    if abs(object_list[(i*8)+6])%10 == 1:
                        score += 20
                    explosion_sounds()                    
                if round(object_list[(i*8)+6], -1) == -730: # alien ship destruction
                    printerlist_add += particlemaker(object_list[(i * 8)], object_list[1+(i * 8)], object_list[2+(i * 8)], object_list[3+(i * 8)])
                    if abs(object_list[(i*8)+6])%10 == 1:
                        score += 200
                    explosion_sounds()
                if round(object_list[(i*8)+6], -1) == -610: # alien shot destruction
                    pass
                if round(object_list[(i*8)+6], -1) == -620: # ship shot destruction
                    pass
                if round(object_list[(i*8)+6], -1) == -670: # ship destruction
                    if object_list[12] == 3:
                        object_list[12] = 5
                        object_list[14] = shield_lifespan
                        object_list[15] = True
                        rotation = 90
                        object_list[8] = width/2
                        object_list[9] = height/2
                    else:
                        extratime_trigger = True
                    explosion_sounds()                    
            object_list += printerlist_add                             
            # collision detection consequences
            
            # deaderizer
            indexadj = 0
            while indexadj < len(object_list): 
                if object_list[6 + indexadj] <= 0:
                    if object_list[4+indexadj] == 5:
                        object_list[7+indexadj] = False
                        object_list[6+indexadj] = 1
                        object_list[4+indexadj] = 1
                    else:
                        object_list = object_list[:indexadj] + object_list[8 + indexadj:]
                indexadj += 8        
            # deaderizer
            
            # printer and flame and score
            object_list = objecthandler(object_list, width, height)
            if object_list[4] == 1 or object_list[4] == 5:
                ship_pointlist = [[object_list[0]+top_xrot*scalar3, object_list[1]-top_yrot*scalar3], [object_list[0]+right_xrot*scalar3, object_list[1]+right_yrot*scalar3], [object_list[0], object_list[1]],
                                  [object_list[0]+left_xrot*scalar3, object_list[1]+left_yrot*scalar3]]
            else:
                ship_pointlist = [[0,0],[0,0]]
            printer(ship_pointlist, object_list, color, scalar3, scalar2, scalar1, scalarscalar) 
            if flame == True and (object_list[4] == 1 or object_list[4] == 5):
                flame_pointlist = [[object_list[0]+rightflame_xrot*scalar3, object_list[1]+rightflame_yrot*scalar3], [object_list[0]-bottomflame_xrot*scalar3, object_list[1]+bottomflame_yrot*scalar3],
                                   [object_list[0]+leftflame_xrot*scalar3, object_list[1]+leftflame_yrot*scalar3]]
                pygame.draw.aalines(screen, (255, 255, 255), False, flame_pointlist, True)
            if flame == True and timer1 == 0:
                enginesound.stop()
                enginesound.play()
            if flame == True and timer1 < 21:
                timer1 += 1
            if flame == True and timer1 == 21:
                timer1 = 0
            if flame == False:
                enginesound.fadeout(10)
            flame = False
            # scoring - big asteroid split = 20, medium asteroid split = 50, small asteroid destroy = 100, alien destroy = 200
            score_string = "score:" + str(score)
            if len(score_string) < 11:
                for i in range(12-len(score_string)):
                    score_string += " "
            else:
                score_string += " "
            text_input = [("right", 10), score_string, 3]
            Texthelper.write(screen, text_input)
            pygame.display.flip()
            # printer and flame and score
            
            # drag
            for i in range(int(len(object_list)/8)):
                if object_list[4 +(i*8)] in drag:
                    stepper = abs(object_list[2 +(i*8)]) + abs(object_list[3 +(i*8)])
                    if stepper == 0:
                        stepper = 1
                    step_drag_x = abs(object_list[2 +(i*8)]) / stepper * step_drag
                    step_drag_y = abs(object_list[3 +(i*8)]) / stepper * step_drag   
                    if object_list[2 +(i*8)] > 0 and object_list[2 +(i*8)] > step_drag_x:
                        object_list[2 +(i*8)] -= step_drag_x
                    elif step_drag_x > object_list[2 +(i*8)] > 0:
                        object_list[2 +(i*8)] = 0
                    if object_list[2 +(i*8)] < 0 and object_list[2 +(i*8)] < step_drag_x:
                        object_list[2 +(i*8)] += step_drag_x
                    elif step_drag_x < object_list[2 +(i*8)] < 0:
                        object_list[2 +(i*8)] = 0     
                    if object_list[3 +(i*8)] > 0 and object_list[3 +(i*8)] > step_drag_y:
                        object_list[3 +(i*8)] -= step_drag_y
                    elif step_drag_y > object_list[3 +(i*8)] > 0:
                        object_list[3 +(i*8)] = 0   
                    if object_list[3 +(i*8)] < 0 and object_list[3 +(i*8)] < step_drag_y:
                        object_list[3 +(i*8)] += step_drag_y
                    elif step_drag_y < object_list[3 +(i*8)] < 0:
                        object_list[3 +(i*8)] = 0
            # drag

            # helpers
            if extratime_trigger == True: #lets particle effects dissipate after gameover
                extratime -= 1
                if extratime < 0:
                    status = "highscorecheck"
            previous_inputvar = inputvar #helps with distinct keyclicks
            if alien_clock != "": #helps with alien zigzags and general timing
                alien_clock += 1
            # helpers

         
        for event in AllEvents.TICKINPUT:
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                raise SystemExit


#checks if it needs to run setupper
if filehelper.get(0)[0] == "?":
    from setupper import *
    
main()
