# -*- coding: utf-8 -*-
import Tkinter, tkFont
from Tkinter import *

class end_game():
    def __init__(self):
        self.end = False

end = end_game()

class Win_Conditions():
    def __init__(self):
        self.scuba_pass = False
        self.coco_pass = False
        self.dance_pass = False
        self.book_pass = False
        self.castle_pass = False
        self.coffee_pass = False
        self.fish_pass = False
        self.hang_pass = False
        self.ticket_pass = False
        self.Lava_pass = False
        self.sand_pass = False
        self.tiki_pass = False
        self.surf_pass = False
        self.snow_pass = False
        self.fireworks_pass = False
        self.bag_pass = False
        self.Kayak_pass = False

Amazing_Race_GUI = Tkinter.Tk()
Amazing_Race_GUI.title('THE AMAZING RACE')
canvas = Tkinter.Canvas(Amazing_Race_GUI, height = 400, width = 1306, relief = Tkinter.RAISED, bg = 'white')
canvas.grid(row = 0, column = 1)
#fonts
customFont = tkFont.Font(family = 'Arial', size = 40)
intro_font = tkFont.Font(family = 'Arial', size = 40)
intro_font2 = tkFont.Font(family = 'Arial', size = 50)
intro_font3 = tkFont.Font(family = 'Arial', size = 20)
name_font = tkFont.Font(family = 'Arial', size = 50)

customFont = tkFont.Font(family = 'Arial', size = 40)   
        
win = Win_Conditions()

#INTRO
intro_message = "This is only a game. It is an Amazing game, but it is still just a game."
intro_message2 = "Do not go crazy about it or break the laptop." 
intro_message3 = "All people, sitations, and all other things in general that you think is like real life, is not real life."
intro_message4 = "It is coincidental. It is not real."
intro_message5 = "Good luck, you will need it."

canvas.create_text(653, 50, text = 'WELCOME TO', font = intro_font)
canvas.create_text(653, 120, text = 'THE AMAZING RACE!!!', font = intro_font2)
canvas.create_text(653, 200, text = intro_message, font = intro_font3)
canvas.create_text(653, 240, text = intro_message2, font = intro_font3)
canvas.create_text(653, 280, text = intro_message3, font = intro_font3)
canvas.create_text(653, 320, text = intro_message4, font = intro_font3)
canvas.create_text(653, 360, text = intro_message5, font = intro_font3)

def name():
    global name_editor
    canvas.delete("all")
    canvas.create_text(653, 150, text = 'What is your name?', font = name_font)
    name_editor = Tkinter.Text(width = 48, height = 2, font = customFont)
    name_editor.grid(row = 1, column = 1)

next_button = Tkinter.Button(Amazing_Race_GUI, text='NEXT', command = name)
next_button.grid(row = 2, column = 1)

directions1 = "DIRECTIONS"
directions2 = "There is a list of possible directions underneath each description."
directions3 = "Choose a direction by clicking it, such as 'north', 'south', 'east', and 'west'. Use 'next' to do a challenge."
directions4 = "Follow the commands and clues given in the descriptions and in the clues to reach the end."
directions5 = "To see what challenges you have and have not completed, press 'Checklist' to see a list of challenges."
directions6 = "If you choose '?', then you shall see these directions agian."
def directions():
    canvas.delete("all")
    canvas.create_text(653, 50, text = directions1, font = intro_font)
    canvas.create_text(653, 150, text = directions2, font = intro_font3)
    canvas.create_text(653, 190, text = directions3, font = intro_font3)
    canvas.create_text(653, 230, text = directions4, font = intro_font3)
    canvas.create_text(653, 270, text = directions5, font = intro_font3)
    canvas.create_text(653, 310, text = directions6, font = intro_font3)
    
next_button = Tkinter.Button(Amazing_Race_GUI, text = 'NEXT', command = directions)
next_button.grid(row = 2, column = 1)

def quit():
    Amazing_Race_GUI.destroy()
    
#side challenges function
def passes_show():
    side_challenges = Tkinter.Tk()
    side_challenges.title('THE AMAZING RACE - SIDE CHALLENGES')
    canvas = Tkinter.Canvas(side_challenges, height = 500, width = 1303, relief = Tkinter.RAISED, bg = 'white')
    canvas.grid(row = 0, column = 1)
    global ChecksFont
    ChecksFont = tkFont.Font(family = 'Arial', size = 40)
    
    boxes = 0
    checks = 0
    #text
    canvas.create_text(500, 120, text = 'Scuba Challenge', font = tkFont.Font(family = 'Arial', size = 40))
    canvas.create_text(500, 270, text = 'Coconut Challenge', font = tkFont.Font(family = 'Arial', size = 40))
    canvas.create_text(500, 420, text = 'Dance Challenge', font = tkFont.Font(family = 'Arial', size = 40))
    canvas.create_text(500, 570, text = 'Book Challenge', font = tkFont.Font(family = 'Arial', size = 40))     
    canvas.create_text(500, 720, text = 'Sandcastle Challenge', font = tkFont.Font(family = 'Arial', size = 40))                
    canvas.create_text(500, 870, text = 'Coffee Challenge', font = tkFont.Font(family = 'Arial', size = 40))                        
    canvas.create_text(500, 1020, text = 'Fishing Challenge', font = tkFont.Font(family = 'Arial', size = 40))
    canvas.create_text(500, 1170, text = 'Hangman Challenge', font = tkFont.Font(family = 'Arial', size = 40))
    canvas.create_text(500, 1320, text = 'Ticket Challenge', font = ChecksFont)
    canvas.create_text(500, 1470, text = 'Lava Challenge', font = ChecksFont)
    canvas.create_text(500, 1620, text = 'Sand Challenge', font = ChecksFont)
    canvas.create_text(500, 1770, text = 'Tiki Tower Challenge', font = ChecksFont)
    canvas.create_text(500, 1920, text = 'Surf Challenge', font = ChecksFont)
    canvas.create_text(500, 2070, text = 'Snowboard Challenge', font = ChecksFont)
    canvas.create_text(500, 2220, text = 'Fireworks Challenge', font = ChecksFont)
    canvas.create_text(500, 2370, text = 'Bag Challenge', font = ChecksFont)
    canvas.create_text(500, 2520, text = 'Kayak Challenge', font = ChecksFont)
    #start box coordinates
    Fx = 100
    Fy = 70
    Sx = 200
    Sy = 170
    #start check coordinates
    FLx = 100
    FLy = 120
    SLx = 150
    SLy = 170
    TLx = 220
    TLy = 20
    #rectangle created
    while boxes < 17:
        canvas.create_rectangle(Fx, Fy, Sx, Sy, width = 7)
        Fy += 150
        Sy += 150
        boxes += 1
    while checks < 17:
        #grey fill
        fill='#b2b2b2'
        
        #SCUBA
        if win.scuba_pass == True:
            fill = 'green'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        else:
            fill='#b2b2b2'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        #COCO
        if win.coco_pass == True:
            fill = 'green'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        else:
            fill='#b2b2b2'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        #DANCE   
        if win.dance_pass == True:
            fill = 'green'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        else:
            fill='#b2b2b2'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        #BOOK   
        if win.book_pass == True:
            fill = 'green'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        else:
            fill='#b2b2b2'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        #CASTLE
        if win.castle_pass == True:
            fill = 'green'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        else:
            fill='#b2b2b2'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        #COFFEE
        if win.coffee_pass == True:
            fill = 'green'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        else:
            fill='#b2b2b2'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        #FISH
        if win.fish_pass == True:
            fill = 'green'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        else:
            fill='#b2b2b2'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        #HANG
        if win.hang_pass == True:
            fill = 'green'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        else:
            fill='#b2b2b2'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        #TICKET
        if win.ticket_pass == True:
            fill = 'green'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        else:
            fill='#b2b2b2'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        #LAVA
        if win.Lava_pass == True:
            fill = 'green'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        else:
            fill='#b2b2b2'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        #SAND
        if win.sand_pass == True:
            fill = 'green'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        else:
            fill='#b2b2b2'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        #TIKI
        if win.tiki_pass == True:
            fill = 'green'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        else:
            fill='#b2b2b2'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        #SURF
        if win.surf_pass == True:
            fill = 'green'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        else:
            fill='#b2b2b2'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        #SNOW
        if win.snow_pass == True:
            fill = 'green'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        else:
            fill='#b2b2b2'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        #FIREWORKS
        if win.fireworks_pass == True:
            fill = 'green'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        else:
            fill='#b2b2b2'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        #BAG
        if win.bag_pass == True:
            fill = 'green'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        else:
            fill='#b2b2b2'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        #KAYAK
        if win.Kayak_pass == True:
            fill = 'green'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
        else:
            fill='#b2b2b2'
            canvas.create_line(FLx, FLy, SLx, SLy, TLx, TLy, fil = fill, width = 15)
            FLy += 150
            SLy += 150
            TLy += 150 
            checks += 1
            
    def quit_challenges():
        side_challenges.destroy()
       
    scrollbar = Scrollbar(side_challenges, command = canvas.yview)
    scrollbar.grid(row = 0, column = 2, rowspan = 2, sticky = Tkinter.N + Tkinter.S)
    
    Quit = Tkinter.Button(side_challenges, text='QUIT', command = quit_challenges)
    Quit.grid(row = 1, column = 1) 
    
    
SideChallengesShowButton = Tkinter.Button(Amazing_Race_GUI, text='Checklist', command = passes_show)
SideChallengesShowButton.grid(row = 3, column = 1)    

Quit = Tkinter.Button(Amazing_Race_GUI, text='QUIT', command = quit)
Quit.grid(row = 5, column = 1) 

#ROOM CONSTRUCTOR
class Room(object):
    #Constructor
    def __init__(self, name, n_path, s_path, e_path, w_path, next_path, description):
        self.name = name
        self.description = description
        self.north = n_path
        self.south = s_path
        self.east = e_path
        self.west = w_path
        self.next = next_path
    #Movement Method
    def move(self, direction):
        global node
        node = globals()[getattr(self, direction)]   
#ROOMS
             #Room Name                        #N    #S    #E    #W    #Next                                                       #Description
Intro = Room('Introduction',                   None, None, None, None, 'Clue_One',                                                 "")
Clue_One = Room('Clue One',                    None, None, None, None, 'Beginning_Plaza',                                          'Find the South Beach, where a challenge awaits, go diving and finding, good luck mates. Go to the South beach and play the scuba challenge.')
Beginning_Plaza = Room('Plaza',                'Volcano', 'South_Beach', 'East_Beach', 'Pearl_City_Harbor', None,                  'This has all taken place in the plaza in the middle of Honolulu on the island of Oahu. You see a sign not far from where you and your teammate are. You call your teammate over and rush to see the sign. Other teams have the same idea, and soon the sign is crowded. You see that north leads you to a volcano, and west leads to Pearl City and Pearl Harbor. East takes you to East Beach, and south will bring you to South Beach. (Amazing names I know). Which direction will you take?')
South_Beach = Room('South Beach',              'Plaza', 'Coconut_grove', 'Maui_Island', 'Big_Island', 'Scuba',                       'You and your partner rush past opposing racers and head for South Beach. It’s not far, but by the end of the sprint, you are exhausted. You see some people with Amazing Race shirts. You head in their direction, fast walking this time. To your west you see a lot of boats and a sign that says, ‘To Big Island’. To the east there are helicopters with a sign that says, ‘To Maui Island’. Going south will lead you to a coconut grove. There is a scuba challenge here.')
Coconut_grove = Room('Coconut Grove',          'South_Beach', 'Hula_dance', None, None, 'CoCo',                                      'You both rush to coconut grove after you are done changing back into your clothes. You head south, and sure enough there is a coconut grove, with a group of people around it. It seems like some other teams are ahead of you, but you will catch up to them soon enough. The only directions you can go are further south, and back up north. But first you must complete the next challenge.')
Hula_dance = Room('Hula Dance Central',        'Coconut_grove', None, None, None, 'Dance',                                           'You reach the next checkpoint at the Hula Dance Central a bit further ahead than you were, but still not in first place you realize because another team is already there. This is as far south as you can go, you will have to return going north, but first you need to do your mission.')
Maui_Island = Room('Maui Islan	d',              'Coffee_Farm', None, 'Maui_Beach', None, 'Book',                                      'You head by helicopter to Maui Island. The view is amazing. There is the beach, and you can even see some other teams down there. But you have fallen farther behind. Learning to dance took you too long. You and your partner must make up for lost time. You touch down at the University of Hawaii, on Maui Island. There are boats on the north to take you back to Oahu Island when you are done here. Going west will take to you Maui Beach.')
Maui_Beach = Room('Maui Beach',                None, None, None, 'Maui_Island', 'Sandcastle',                                        'You reach the beach exhausted. Your partner doesn’t seem too energetic either. When you are done, you will have to go back to the University, and then go north to reach the boats to get back to Oahu Island. But now you must start your challenge.')
Coffee_Farm = Room('Coffee Farm',              'East_Beach', None, 'Lanai_Island', None, 'Coffee',                                   'You are back on Oahu Island at a coffee farm. There is a sign to your north, saying ‘East Beach’. And also another one pointing east that says, ‘Lanai Island’. First there must be a challenge to complete here.')
Lanai_Island = Room('Lanai Island',            None, None, None, 'Coffee_Farm', 'Fishing',                                           'Your boat gets to Lanai Island. The boat will stay here for you to go back west to Oahu Island when you need to.')
East_Beach = Room('East Beach',                'Miwiwe_Street', 'Coffee_Farm', 'Seal_Show', 'Plaza', 'Hangman',                      'You have finally reached the East Beach of Oahu Island. To your east is a seal show, and to the west is the plaza. North will take you to street called Miwiwe. There is a crowd of people at several tables set up with the Amazing Race banner over them.')
Seal_Show = Room('Seal_Show',                  None, None, None, 'East_Beach', 'Tickets',                                            'You have reached the seal show. To return, you will need to go west back to the East Beach, and then continue. But for now, your challenges must be met.')
Miwiwe_Street = Room('Miwiwe Street',          None, 'East_Beach', None, None, 'RR',                                                 'You and your partner are walking down the street Miwiwe. The only path it seems is going back south to East Beach. You are suddenly surrounded by cops, helicopters and squad cars! An agent comes to you. ‘My name is Lt. Commander Steve McGarrett – Hawaii Five-0. This is a restricted area. Please leave.’ You timidly shake your head yes and start to leave. You are walking along the sidewalk back south to the East Beach. But then…')
Plaza = Room('Plaza',                          'Volcano', 'South_Beach', 'East_Beach', 'Pearl_City_Harbor', None,                  'You walk into the plaza, where you started. By now, most of the decorations and floral arrangements are gone. From here you can go north to the Volcano, south to South Beach, and west to Pearl Harbor, or east to East Beach.')
Volcano = Room('Volcano',                      'North_Beach', 'Plaza', 'Northeast_Beach', 'Northwest_Beach', 'Lava',                 'You reach the volcano summit. From here you can go south to the plaza, east to Northeast beach, and west to Northwest beach, or north to North beach. But it appears there is a challenge here.')
Northeast_Beach = Room('Northeast Beach',      None, None, None, 'Volcano', 'Sand',                                                  'You get down the volcano where some teams are still working. You need to work faster so you can catch up. Going west will take you back up there. But there is another challenge ahead.')
North_Beach = Room('North Beach',              None, 'Volcano', None, None, 'Tiki',                                                  'You walk down the volcano to another beach, called North Beach. ‘There are several large tiki towers over there’, you tell your partner and you both walk that way. You will have to go south back up the mountain to get back, but for now it looks like you have another mission.')
Northwest_Beach = Room('Northwest Beach',      None, 'Mauna_Kea_Volcano', 'Volcano', None, 'Surf',                                   'You reach another beach. East will take you to the Volcano, and south will take you to a mountain called Mauna Kea Volcano. By this time you feel you have seen almost all the world’s beaches. The expression on your partners face shows she feels the same. But it looks like there is a surfing competition here or something.')
Mauna_Kea_Volcano = Room('Mauna Kea Volcano',  'Northwest_Beach', 'Big_Island', 'Pearl_City_Harbor', 'Kauai_Island', 'Snow',         'You climb up the mountain. It is called Mauna Kea Volcano, but it is not active. From the top you can see that to the west is Pearl Harbor.  To the east is another island, Kauai Island. South you see another island, Big Island. North would take you to the Northwest beach. There is snow on this mountain. It looks like this is the place for another challenge.')
Kauai_Island = Room('Kauai Island',            None, None, 'Mauna_Kea_Volcano', None, 'Fireworks',                                   'You ride the snowboards as far down as you can, then you change out of the clothes and boards when the snow runs out. You jog down the rest of the mountain. You did pass up a few teams going down the mountain. Good job! You reach the Kauai Island by boat. By now it is evening. Going east will take you back to the Mountain. There are two teams already on the island. There is one more in a boat coming to the island. You have caught up with the leaders!')
Big_Island = Room('Big Island',                'Mauna_Kea_Volcano', None, 'South_Beach', 'Niihau_Island', 'Bags',                    'You reach this island by boat, and get off in a hurry. You now have a chance to pass the two leading teams up. You can go north to the Mauna Kea Volcano, east to South Beach, or west to Niihau Island. An Amazing Race instructor is comes to assist you. ‘This is the Big Island, filled with big people, big cars, big houses, and big stuff. People love to buy stuff from here, and it is a popular tourist attraction.’')
Niihau_Island = Room('Niihau_Island',          None, None, 'Big_Island', None, 'Kayak',                                              'You have reached the island by speed boat. By now it is night, and the Hawaiian skyline is lit up beautifully with all sorts of colors and lights. In the distance you can see the firework show begin. You can go east to the Big Island or continue. An instructor comes to your team.')
Pearl_City_Harbor = Room('Pearl City Harbour', None, None, 'Plaza', 'Mauna_Kea_Volcano', 'Win',                                      'You are at the Pearl City Harbor. There in the water you can see the USS Arizona Memorial. You can go west to the Mauna Kea Volcano, or east to the Plaza.')  #Normal plaza
Pearl_Harbour = Room('Pearl Harbour',          None, None, None, None, None,                                                       'You run across the streets of Pearl City, Hawaii on Oahu Island. You are not far behind another team. But these streets are so confusing. The other team stops and asks for directions, then rushes off into the night. Them asking for directions got you both a few seconds closer to them. You keep on running, hoping you are leading yourselves in the right direction. You and your partner rush past the other team, who are confusing of where to go at an intersection. You just keep running. Finally you see it. There is the Harbor. You run to the loading dock. You can see the people from The Amazing Race over the sunken ship in the harbor. You run up to the gate, but the old man there says, ‘Sorry, no passage without paying the fee. It’s $2.15 per person, $1.10 per child, and $3.45 per pet.’ You feel greatly pleased with yourself as you remember you kept the spare change from the kayaks. You hurriedly pay the man $4.30 and rush to the boats. There are many rowboats, each with a clue on the seat. You open one. ‘A final test of power, strength, and determination: work together to reach the end.’ You both hop into a rowboat, but so do another other two teams. Your partner is on your left, and has that oar, while you hold the right. You both row to the USS Arizona Memorial in the harbor.')


def Intro_to_game():
    canvas.delete("all")
    description = "Aloha, and welcome to Honolulu, Hawaii, on Oahu Island. You and your partner must complete all 18 challenges, follow the clues given and reach the end to win this race. Here is your first clue. (You are handed an envelope with the Amazing Race Insignia.) Good luck racers. *(Hint: Type 'next' to go on. This will be a miscellanous direction/move.)"
    editor = Tkinter.Text(width = 52, height = 8, font = customFont)
    editor.insert(Tkinter.END, description)
    editor.config(state = Tkinter.DISABLED)
    
IntroGameButton = Tkinter.Button(Amazing_Race_GUI, text='Skip to Start', command = Intro_to_game)
IntroGameButton.grid(row = 4, column = 1)


Amazing_Race_GUI.mainloop()