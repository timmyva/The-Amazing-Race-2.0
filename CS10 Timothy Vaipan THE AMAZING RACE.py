# -*- coding: utf-8 -*-
import random
import sys
import time
import pickle

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
        
win = Win_Conditions()
start_time = time.time()

#INTRO
print "WELCOME TO \x1B[3mTHE AMAZING RACE!!!\x1B[23m"
print
print "This is only a game. It is an Amazing game, but it is still just a game. Do not go crazy about it or break the laptop. All people, sitations, and all other things in general that you think is like real life, is not real life. It is coincidental. It is not real. Good luck, you will need it."
print

#Name for later
global name
name = raw_input("What is your name? >")
if name in ['q', 'quit', 'exit']:
    print "GAME OVER"
    sys.exit(0)
    
print 
directions = "DIRECTIONS: There is a list of possible directions underneath each description. Type a direction in, such as 'north', 'south', 'east', 'west', or 'next'. Follow the commands and clues given in the descriptions and in the clues to reach the end. If you type in '?', then you shall see these directions agian."
print directions
print

#1 SCUBA CHALLENGE
def Scuba(): #Intro
    print "‘We are a marine biology research company. We collect marine samples. You must put on scuba gear and go diving for this mission. You will be collecting samples of marine life, including seaweed that you will need in a later mission.’ You and your partner hurriedly get some gear, and go to the provided rooms to change. Other teams have arrived about midway through the statement, and you can hear the directions being explained again. Other teams will catch up with you if you don’t hurry. You are done changing. You head out, clumsy in your scuba gear and head to the boat and instructor provided for each team, where your partner is already waiting. You head out, along with a few other teams to the small coral reef."
    pionts = 0  #needs to be 8
    
    while pionts < 8:
        print
        print "You need 8 points to win"
        look_for = ["sea star", "plankton", "star fish", "clownfish", "piranha", "sea urchin", "puffer fish"]  #what you're looking for possibles
        finding = random.choice(look_for)#what you're looking for 
        possibles = ['rock', 'coral hill', 'sunken boat', 'dead whale'] #where it is possibles
        hidden = random.choice(possibles)#where it is 
        
        print "You are looking for a", finding
        print "Is it behind the", possibles[0], "or behind the", possibles[1], "or behind the", possibles[2], "or behind the", possibles[3], "?"
        awnser = raw_input("What do you think it is behind? ")  #where do you think it is?
        if awnser == 'q':
            sys.exit(0)  #can leave challenge
        if awnser == hidden:
            print "You got it!"
            pionts += 1  #if you found it
            print "You have %d points" %pionts
        else:
            print "You did not get it right."   #did not get it
            print "The sea star was behind the", hidden
            print "You have %d points" %pionts  
        print
    #Clue/pass
    print "Good job %s! You get a clue: 'Go to the coconut grove and start climbing!" %name
    print
    win.scuba_pass = True  

#2 COCONUT CHALLENGE
def CoCo():    #Intro
    print "You reach the group of people surrounding the coconut trees. There are even some people who look like natives in the trees. A lady approaches you and your partner. ‘You mission is to get coconuts from these trees by climbing them, just like the natives did for hundreds of years, and still do today. Because you are not used to climbing vertically one of you will get a pair of climbing spike shoes and a machete, and the other will get a basket to catch the cut coconuts. Then you will both cut these coconuts and use the water to make coconut milk, and the shells to make coconut bras.’"
    print "You start to climb up. Your partner is below with a basket. You need 5 coconuts."
    coco_pionts = 0  #needs to be 5
    
    while coco_pionts <= 4:
        print
        swings = ["left", "right", "straight"] #possible spots
        correct = random.choice(swings)  #where the coconut is
        catch = [1, 2]
        caught = random.choice(catch) #if you hit it or not = 50/50 chance
        caught2 = random.choice(catch)
        print "Do you swing left, right, or straight with the machete?"
        print "Type in 'left', 'right', or 'straight'"
        swing = raw_input(">")
        if swing == "q":
            sys.exit(0)  #can leave challenge
        if swing == correct:
            print "You hit a coconut!" #if hit it
            if caught == caught2:
                print "Your partner caught it."  #plus a piont! caught it
                coco_pionts += 1
                print "You have %d pionts." %coco_pionts
            else:
                print "But your partner did not catch it - no piont"  #partner must catch it or no piont
        else:  #if you missed the coconut
            print "You missed the coconut."
            print "The coconut was", correct
            print "You have %d pionts." %coco_pionts
        print
    #Clue/pass
    print "Good job %s! You get a clue: 'Keep on going, find the dance party and start crafting and danceing!" %name
    print
    win.coco_pass = True

#3 DANCE CHALLENGE
def Dance(): #Intro
    print "You see a sign with instructions, and you and your partner walk over to check out what your next mission is.  ‘You must now rush to make both of yourselves hula skirts of the seaweed you got earlier, and use the coconut bras you made, then learn to hula correctly from experts. Then you will be ready to try it for yourselves.’"
    print 
    
    print "Hurry %s! You must dry the seaweed first. Type in 'dry'" %name
    dry = raw_input(">")
    if dry == 'dry':
        print "Ok. You now lay your seaweed in the sun."
        print "Good job. Now since this proccess takes a long time, here is some ready made seaweed."
        print "You now have dried seaweed. Now you have to sew it toegther."
        print "Your partner gets a rope, which will go around your waist. You need to sew the seaweed to it."
        print "You need to sew using this method: 'through', and 'over'. And again till you are done."
        Through = raw_input("Type through to start >")
        if Through == 'through':
            print "Good, now type 'over'"
            over = raw_input(">")
            if over == 'over':
                print "Good, now type 'through'" 
                Through1 = raw_input(">")
                if Through1 == 'through':
                    print "Good, now type 'over'"
                    over1 = raw_input(">")
                    if over1 == 'over':
                        print "Good, you are done." 
                        print "Now you must try to make coconut bras. Cut straight forward."
                        cut = raw_input("Type straight >")
                        if cut == 'straight':
                            print "You got it. Now connect the ropes on it to make it a bra."
                            print "You make the coconut bra and are done. Now you have to learn to dance."
                            print "Shake to the left!"
                            left = raw_input(">")
                            if left == 'left':
                                print "Now shake right!"
                                right = raw_input(">")
                                if right == 'right':
                                    print "Now shake left!"
                                    left1 = raw_input(">")
                                    if left1 == 'left':
                                        print "Now shake right!"
                                        right = raw_input(">")
                                        if right == 'right':
                                            print "You did %s You win!" %name
                                            print "You get another clue: 'Go to MAUI ISLAND, and find the book. The one on sandcastles, Good luck - you'll need it.'"
                                            print
                                            win.dance_pass = True
                                        else:
                                            print "You failed. Try agian."
                                    else:
                                        print "You failed. Try agian."
                                else:
                                    print 'You failed. Try agian.'
                            else:
                                print 'You failed. Try agian.'
                        else:
                            print 'You failed. Try agian.'
                    else:
                        print 'You failed. Try agian.'
                else:
                    print 'You failed. Try agian.'
            else:
                print "You failed. Try agian."
        else:
            print "You failed. Try agian."
    else:
        print "Please type in 'dry', to continue your challenge."

#4 BOOK CHALLENGE
def Book():  #Intro
    print "As soon as you leave the helicopter, you get instructions in the form of another clue. Your partner opens it and reads the words, ‘Hawaii University - quite a large place, but one book to find, in this Amazing Race.      -      The book on sandcastles.’ You must need to find a library. You see a campus map, and find out this trip to the library will make to trek uphill to get there. ‘Let’s go’, you both say and get on your way. You finally reach the library, and its cool air conditioned air welcomes you. Now you have to find a book on sandcastles. But suddenly another team rushes part you and into the library. You must find the book before anyone else does."
    correct = 0  #how many you got right
    
    while correct < 6:
        possible_turns = ['left', 'right', 'straight'] #possibilities
        turn = random.choice(possible_turns) #correct
        print
        print "You can go left right or straight. Choose now."  #your chioces
        print "Type in 'left', 'right', or 'straight'"
        print
        chioce = raw_input(">")  #Your chioce
        if chioce == turn:
            print "You turned %s" %chioce
            correct += 1
            if correct >= 5: #If you made it to the book
                print "You made it to the book!"
                print "You open the book up."
                break
            else:
                print "Now where do you want to go %s?" %name   #continuation
            
        else:
            print "You went %s" %chioce  #wrong way result
            print "You went the wrong way %s. Try agian." %name
    #clue/pass
    print "You see another clue in the book: 'You have found the book on sandcastles. Now you have to build one. Many amazing sandscatles have been made and photographed here. Go east to the MAUI BEACH and start building. Good luck.'"
    print
    win.book_pass = True

#5 CASTLE CHALLENGE
def Sandcastle():  #Intro
    print "You rush to the sand, but see that 4 other teams have already started. One is almost done, and another team is right behind you. You have to hurry and start building."
    print "You get a shovel and a pail. If your castle looks good enough you can go on."
    
    print "You must now fill the pail and dump it to make a tower. Type in 'fill'."
    fill = raw_input(">")#what you do
    if fill == "fill":
        print "Now type 'dump'."
        dump = raw_input(">")
        if dump == "dump":
            goodbad = [1, 2]  #might not pass
            GoOn = random.choice(goodbad)
            Goon = random.choice(goodbad)
            if GoOn == Goon: #If does pass...
                print "An instructor comes to you, and looks at your castle. 'It passes! Good job %s, here is your next clue.'" %name
                print "The clue says, 'You must go to the COFFEE FARM. Go back to the main part of this island, then go north to reach the coffee farm. Time to make American's favorite drink.'"
                win.castle_pass = True
                pass
            else:
                print "Now type 'fill' agian." #otherwise...
                fill = raw_input(">")
                if fill == "fill":
                    print "Now type 'dump'."
                    dump = raw_input(">")
                    if dump == "dump":
                        goodbad = [1, 2]
                        GoOn = random.choice(goodbad)  #1 more chance or must try all over again
                        Goon = random.choice(goodbad)
                        if GoOn == Goon:
                            print "An instructor comes to you, and looks at your castle. 'It passes! Good job %s, here is your next clue.'" %name
                            print "The clue says, 'You must go to the COFFEE FARM. Go back to the main part of this island, then go north to reach the coffee farm. Time to make American's favorite drink.'"
                            print
                            win.castle_pass = True
                            pass
                        else:
                            print "You took to long to build your castle and it crumpled. You have to try agian."
                            print "You have to try this challenge again to continue THE AMAZING RACE!!!"
                            pass
                    else:
                        print "Type in 'dump'."
                else:
                    print "Type in 'fill'."
        else:
            print "Type in 'dump'."
    else:
        print "Type in 'fill'."

#6 COFFEE CHALLENGE
def Coffee():  #Intro
    print "You are given a clue. ‘Hawaii has amazing coffee trees that the natives have used for many years to create this wonderful drink. Now it’s your turn. Get to the trees and start picking beans, then make them into coffee."
    print "Because you are not used to climbing vertically one of you will get a pair of climbing spike shoes and a knife, just like earlier, and the other will get a basket to catch the cut coffee bean branches."
    coffee_pionts = 0  #need 5
    
    while coffee_pionts <= 4:
        print
        swings = ["left", "right", "straight"]  #possibles
        correct = random.choice(swings)  #correct
        catch = [1, 2]
        caught = random.choice(catch)  #if caught it
        caught2 = random.choice(catch)
        print "Do you saw the left, right, or straight branch with the knife?"
        print "Type in 'left', 'right', or 'straight'"
        saw = raw_input(">") #input
        if saw == "q":
            sys.exit(0) #Can leave challenge
        if saw == correct: #If you cut it down
            print "You cut the right coffee branch!"
            if caught == caught2:
                print "Your partner caught it." #50/50 chance partner caught it
                coffee_pionts += 1
            else:
                print "But your partner did not catch it."
        else:  #if missed coffee branch
            print "You missed the coffee branch."
            print "The coffee branch was", correct
    print
    print "You got enough coffee beans to make your coffee."
    print "Now you have to peel the beans. Type 'peel'."
    peel = raw_input(">")  #input for next step
    if peel == 'peel':
        print "When coffee is packaged, washing and drying of the beans would be the last step, but that takes days. Then the beans are packaged. So now pachage the beans. Type 'package'."
        package = raw_input(">")
        if package == 'package': #Outro/clue/pass
            print "You are now done. Here is your next clue."
            print "You get a clue: 'Head east to LANAI ISLAND! Time to go have fun doing a popular Hawaiian sport! Good luck.'"
            print
            win.coffee_pass = True
        else:
            print "Type in 'package'."
    else:
        print "Please print 'peel'."

#7 FISHING CHALLENGE
def Fishing():  #Intro
    print "You are given a clue and a box of fishing gear! You wonder what you will have to do now. The clue says, ‘There are many types of fish in these waters, and fishing is a great sport here. Go to the pier and catch ten fish, but you have to hurry!’"
    print "You both walk to the end of the pier where there are poles and fishing gear all set up for you both."
    caught_fish = 0  #need 10
    
    while caught_fish < 10:
        print
        chioce_swings = ["left", "right", "straight"]  #Possibles
        fish_present = random.choice(chioce_swings)  #where fish are
        bite = [1, 2]
        bite1 = random.choice(bite)  #if bite bait 
        bite2 = random.choice(bite)
        caught = [1, 2]
        caught1 = random.choice(caught)  #if caught fish
        caught2 = random.choice(caught)
        print "%s, do you swing your line left, right, or straight with the fishing pole?" %name
        print "Type in 'left', 'right', or 'straight'"
        swing = raw_input(">")  #your input 
        if swing == "q":
            sys.exit(0)
        if swing == fish_present:  #if where the fish is
            print "You got your line next to a fish!"
            if bite1 == bite2:  #if bit bait
                print "The fish bit your bait. He's hooked! Now you reel him in!"
                if caught1 == caught2:  #if caught it
                    print "You got the fish!"
                    caught_fish += 1
                    print "You have %d pionts." %caught_fish
                else: #otherwise...
                    print "But last second the fish got free of your hook and swam away."
            else:  #otherwise...
                print "The fish did not bite your bait. Try agian."
        else:  #otherwise...
            print "There are no fish there."
            print "The fish were", fish_present
            print "You have %d pionts." %caught_fish
        print
    #Outro/pass/clue
    print "You did it %s! You got all 10 fish!" %name
    print "You get a clue: 'It was once known as the death penalty. Now it is a fun game used to pass the time. Go back to Oahu Island, and head north to the East Beach to continue the Amazing Race!'"
    print
    win.fish_pass = True
    
#8 HANGMAN CHALLENGE
def Hangman():                      #Intro
    print "You walk over to a table. An old lady on the other side says you must play a game of hangman (a popular pastime in Hawaii) with her before you continue."
    print "You must play a game of hangman and win, and then continue, to win the Amazing Race."
    print
    
    allwords = "mouse", "laptop", "espanol", "fire", "mr", "ms", "mrs", "test", "taking", "take", "tips", "congruent", "protractor", "step", "steps", "signs", "sign", "exit", "enter", "not", "who", "you", "are", "that", "gaming", "question", "questions", "holds", "you", "back", "think", "thought", "games", "game", "fabric", "cloth", "screw", "nail", "hammer", "squirt", "picture", "frame", "pictureframe", "for", "it", "is", "tape", "box", "phone", "cellphone", "user", "username", "password", "pass", "ruler", "measure", "comfortable", "the", "a", "alright", "day", "days", "bench", "brick", "bricks", "earaser", "pad", "panel", "tempeture", "blackborad", "chalk", "cube", "statue", "january", "febuary", "march", "april", "may", "june", "july", "august", "october", "november", "december", "month", "months", "ice", "door", "drawing", "liberty", "well", "good", "qiuz", "objective", "geometry", "math", "english", "spanish", "video", "food", "case", "water", "soda", "pyramid", "overhead", "projector", "umbrella", "textbook", "text", "bookcase", "tacos", "burritos", "wiebe", "kyle", "volume", "control", "error", "whipe", "pen", "trash", "gear", "clock", "stool", "chair", "desk", "grease", "bread", "motor", "marker", "monitor", "wire", "input", "fit", "cane", "stack", "weed", "drugs", "printer", "back", "whiteboard", "wood", "metal", "code", "Bible", "binder", "paper", "hilighter", "pencil", "bucket", "round", "circular", "hangman", "bottle", "nag", "expo", "green", "all", "word", "cabinet", "banner", "turtle", "mouse", "jellyfish", "peanuts", "whale", "tiger", "panther", "couger", "words", "flag", "chair", "triangle", "circle", "square", "trapaziod", "hexagon", "blue", "orange", "purple", "brown", "black", "white", "red", "moroon", "gold", "silver", "bronze", "medallion", "medal", "book", "movie", "trip", "car", "bike", "trike", "tricycle", "moped", "I", "ice", "idea", "ideal", "identical", "identification", "identify",  "bye", "hi", "if", "ignore", "ill", "illegal", "illness", "illustrate", "image", "imaginary", "imagination", "imaginative", "imagine", "imitate", "immediate", "immigrant", "immoral", "impact", "impatience", "impatient", "import", "stuff", "all", "cool", "nice", "zero", "zone", "zoo", "dog", "cat", "chat", "illuminati", "computer", "hello", "yard", "yawn", "year", "yearly", "yell", "yellow", "yes", "yesterday", "yet", "you", "young", "your", "yours", "yourself", "loooooser", "winner", "alligator", "llama", "comotellamas", "supercalifragilisticexpialidocious", "table", "tactful", "tactless", "tail", "take", "takeoff", "talent", "talk", "tall", "tank", "tap", "tape", "target", "task", "taste", "tax", "taxi", "tea", "teach", "teacher", "team", "teammate", "tear", "technical", "technique" #this is the list of possible words
    bank = random.choice(allwords)  #this chooses a random word from the "allwords"
    guesses = ""                    #this is an empyty list that adds every guess you guessed to it
    turns = 5                       #this is varaible that is how many turns to get to play hangman. 

    while turns > 0:                #while you still have turns left...
        wrong = 0                   #you have 0 wrong guesses. (No letters left to guess)
        for char in bank:          #for every character in the bank
            if char in guesses:    #if the character is part of the guesses...
                print char,        #then it prints the character you guesses in place of the underscore...
            else:                  #otherwise....
                print "_",         #it prints an underscore
                wrong += 1          #and your wrong goes up one. 
        if wrong == 0:             #if you have no wrongs(no letters left to guess)...
            print
            print "You Won!"       #it'll print that you won
            print
            print "Now go east to the seal show. Although they were all once wild and brutal, they have been tamed and trained for our enjoyment into gentle beasts." #clue           
            print
            win.hang_pass = True       #Pass
            print
            break
    
        guess = raw_input("Guess a letter: ").strip().lower()  #this is actually where you guess a letter
        guesses += guess             #and it adds it to the guess list
    
        if guess not in bank:       #if your guess is not in the bank then it ...
            turns -= 1               #takes one turn away
            print ""
            print "Wrong Letter"    #and tells you it was wrong
            print ""                #this is a blank line
            print "You have", turns, "turns left!"   #and it tells you how many turns you have left. 
            print ""                #this is a blank line
        
    if turns == 0:                   #if you used all your turns 
        print "Ha Ha, You lost!"     #it prints that you lost
        print "The word was", bank  #and tells you what the word was
        print                       #this is a blank line

#9 TICKET CHALLENGE
def Tickets():  #Intro
    print "You find a stack of clues on a table. You take one and open it. ‘You have gotten this far, but will you make it through? Sell tickets to the show, until you have 100 dollars, you will need it later on."
    print "You each grab a stack of tickets."
    money = 0 #Needs to be 100
    
    while money < 100:  #Until you get 100
        print
        people = ["left", "right", "straight"]  #possible buyers
        buyers = random.choice(people)   #will buy
        print "Do you go the the people on the left, on the right, or straight. "
        print "Type in 'left', 'right', or 'straight'"
        print
        direction = raw_input(">")  #asks where you will go to sell
        if direction == "q":
            sys.exit(0)  #can leave challenge
        if direction == buyers:
            selling_piont = ["'Please buy a ticket and go see the wonderful show!'", "'Buy a ticket now!'", "'Do you want to buy a ticket to see the seal show?'", "'Buy a ticket to see the wonderful seals perform!'"] #possible selling pionts
            sell_piont = random.choice(selling_piont) #the one you use
            print "You say to them,", sell_piont  #what happens if they do buy one
            print "They say to you, 'We'll buy some!'"
            sold = random.randint(1, 25)  #how many they bought
            print "They buy %d tickets from you!" %sold
            money += sold
            print "You have %d dollars!" %money  #how much money you have
        else:  #if they don't buy any
            print "They say to you, 'No thanks. We don't want to go to the seal show.'"
            print "You should have gone %s. Another group went there and sold tickets to them." %buyers
            print "You have %d dollars." %money
        print
    #outro and next clue/pass
    print "You did it %s! You sold enough tickets. Now you have 100 dollars. Keep going." %name
    print "You get a clue: 'Head to the volcano! But trust me, do not go to Miwiwe street. You do not want to go there. I told you don't go there. You just got to trust me, don't go there. Head to the plaza, and then north to get to the volcano, but DO NOT go to Miwiwe street.'"
    print
    win.ticket_pass = True

#10 RR CHALLENGE
def RR():
    message = "But just then you are grabbed from behind by someone! They push you into an alley!"  #Intro
    global dead                                              
    fullgun = "barrel 1", "barrel 2", "barrel 3", "barrel 4", "barrel 5", "barrel 6"
    chosen = random.choice(fullgun)    #randon barrel  -  what you got
    bulletIn = random.choice(fullgun)  #random barrel  -  where bullet is
    
    print message  #prints above message which introduces the situation
    print
    print "Prepare yourself."
    print
    print "You raise the gun to your head. Dum Dum DUM!!!!!! YOU CLICK IT...!!!"  #suspence
    if bulletIn == chosen:
        print "Sorry. You got shot. You dead.  :("    #if they are the same you die, and the game ends.
        end.end = True
    else:
        print "You got lucky this time. You can go free. You did not get shot.   :)"  #if not, you survive and continue on your way. 

#11 LAVA CHALLENGE
def Lava():
    print "You walk over to a table set up for this challenge. You see some other teams have already started this challenge. The man at the table says, ‘You have to get into these suits to protect yourselves. This lava here is hundreds of years old, but some farther up is fresher. You will use the tools and retrieve some lava that the Lava Institute of Hawaii uses for data analysis. Get suited up.’ You and your partner get into your suits at the changing rooms and head out, up the volcano to get some lava."
    print "You have to get to the freshest lava at the lava flow, however you can slip through and burn yourself on some unstable lava on your way up. Careful!"
    print
    print "You have to go up the mountain and then back down, but beacuse the lava flows contstatly move, the trip down and up will be diffrent."
    correct_direction = 0  #how many you got right
    
    while correct_direction < 6:
        possible_turns = ['left', 'right', 'straight'] #possibilities
        direction = random.choice(possible_turns) #correct direction
        print
        print "You can go left, right, or straight. Choose now."  #your chioces
        print "Type in 'left', 'right', or 'straight'"
        print
        chioce = raw_input(">")  #Your chioce
        if chioce == 'q':  #can exit challenge
            sys.exit(0)
        if chioce == direction:
            print "You turned %s" %direction
            correct_direction += 1
            if correct_direction >= 5: #If you made it to the right lava place
                print "You made it to the lava flow!"  #Intro to 2nd part
                print "You get lava and put it in your container. But now you have to get back down, without slipping, which will be harder since you are going down and fast beacuse you want to win this race."
                print
                break   
            else:
                print "Now where do you want to go?"  #continuation
        else:
            print "You went %s" %chioce  #wrong way result
            print "You went the wrong way, and almost slipped through the lava. Try agian."

    correct_direction_down = 0  #how many you got right going down
    #2nd part = going down
    while correct_direction_down < 11:  #until 10 right
        possible_turns_down = ['left', 'right', 'straight'] #possibilities
        direction_down = random.choice(possible_turns_down) #correct
        print
        print "You can go left right or straight down. Choose now."  #your chioces
        print "Type in 'left', 'right', or 'straight'"
        print
        chioce_down = raw_input(">")  #Your chioce
        if chioce == 'q':  #can exit challenge
            sys.exit(0)
        if chioce_down == direction_down:
            print "You turned %s" %direction_down
            correct_direction_down += 1
            if correct_direction_down >= 10: #If you made it to the bottom
                if chioce == 'q':  #can exit challenge
                    sys.exit(0)
                print
                print "You made it back to the table!"
                print "You deliver the sample and recive a clue in return."
                #clue/pass
                print "'You must now head down to the Northeast Beach (at your east) for a special wondeful suprise (another challenge)! Good luck.'"
                print
                win.Lava_pass = True
                break
            else:
                print "Now where do you want to go? %s" %name  #continuation 
        else:
            print "You went %s" %chioce_down  #wrong way result
            print "You went the wrong way agian %s! And you almost tripped into a fresh flow of lava, nearly killing yourself. Try agian." %name

#12 SAND CHALLENGE
def Sand():   #Intro and list of sands
    print "You reach a beach filled with colorful sand. The perfect blue water is amazing, but can’t compare to the beauty filled multi colored sand across this beach. At a table a man tells you both, ‘The volcano has created all these types of sand over the years, and the water has helped as well. You must now collect each type of sand listed on this sheet. (He hands your partner a sheet with a diagram on it.) We will use it in the Sand Institute of Hawaii Foundation.’"
    print 
    print "           LIST OF SANDS"
    print "GREEN -        from Olivine crystals(natural glass)"
    print "RED -          from iron"
    print "PINK -         from red corals"
    print "BLACK -        from lava"
    print "WHITE -        from absence of nearbye minerals"
    print "ORANGE -       from a little iron"
    print "PURPLE -       from nearbye minerals"
    print "BROWN -        from nearbye minerals"
    print "GREY -         from pieces of worn rocks"
    print 
    AllSands = ["GREEN", "RED", "PINK", "BLACK", "WHITE", "ORANGE", "PURPLE", "BROWN", "GREY"]
    sands = 0  #how many sands you have 
    left_to_find = 9
    while sands < 10:
        possible_turns = ('left', 'right', 'straight') #possibilities
        sand_place = random.choice(possible_turns) #where sand is
        print
        print "You can go left right or straight."  #gives options
        print "Type in 'left', 'right', or 'straight'"
        print
        sand_direction = raw_input(">")  #Your chioce
        if sand_direction == 'q':  #can leave challenge
            sys.exit(0)
        if sand_direction == sand_place:
            print "You turned %s" %sand_direction
            print "You found a different kind of sand!"
            print
            found_sand = random.choice(AllSands)
            print "You found the %s sand!" %found_sand
            left_to_find -= 1
            print "You have %d sands left to find!" %left_to_find
            AllSands.remove(found_sand)
            sands += 1
            if sands >= 9: #If you found all the sands
                print "You found all the sands!"
                print "You go to the table and return all the sands to the man."
                break
            else:
                print "Now where do you want to go?"  #continuation
        else:
            print "You went %s" %sand_direction  #wrong way result
            print "There is no new sand here. Keep going and try agian."
    #clue/pass
    print
    print "You recieve a clue: Head back to the volcano, then go north for a tumbling tiwi tower experience. (another challenge)"
    print
    win.sand_pass = True

#13 TIKI CHALLENGE
def Tiki():   #Intro
    print "You are given a knife each, a hunk of wood, and instructions. ‘The natives here built many large tiki towers, for many years. They have turned into a large tourist attraction, and smaller models are sold across the world. Now it’s your turn to create a tower out of wood.’"
    print "But your tower will be a much smaller version of the big idols that were made, so don't build to big. It will be sold as a tourist attraction sovenier if it is good enough."
    correct_cuts = 0  #how many cuts you got right
        
    while correct_cuts <= 5:  #needs 8 correct cuts
        possible_turns = ['left', 'right', 'front'] #possibilities
        correct_cut = random.choice(possible_turns) #correct
        print
        print "You can cut with the knife on the left right or front side. Better choose the right cut or you will mess up the statue."  #your chioces
        print "Type in 'left', 'right', or 'front'"
        print
        cut_chioce = raw_input(">")  #Your chioce
        if cut_chioce == 'q':   #can leave challenge.
            sys.exit(0)
        if cut_chioce == correct_cut:
            print "You cut the %s side." %cut_chioce
            print "Then your partner makes a cut. Nice job."
            correct_cuts += 1
            if correct_cuts >= 5: #If you made the right cuts, and finished the statue
                print "You made the staue. It is done!"
                print "You bring it back to the instructor, finished. She gives you a clue."
                break
            else:
                print "Now where do you want to cut?"  #continuation
        else:
            print "You cut %s" %cut_chioce  #wrong way result
            print "Your cut almost messed up the satute, but you can fix it. Just keep on trying %s." %name
    #clue/pass
    print
    print "You open up the clue. 'Head back up the volcano, then head west to the Northwest beach. Time to do THE MOST POPULAR HAWIIAN SPORT OF ALL TIMES!!! Good luck dudes and dudets.'"
    print
    win.tiki_pass = True 

#14 SURF CHALLENGE
def Surf():
    print "You walk to the water, where there is a large group of surfers and Amazing Race officials. One comes to your team. ‘You will learn to surf today, so get a board appropriate to your height, and start learning with one of our teachers.’"
    print "You get on your board, while your partner does the same."
    print "'Surfing is accomplished by geting on a wave, then using your body to turn the board the direction you want it to go.'"
    correct_surf_turns = 0  #how many turns you got right
    
    while correct_surf_turns < 3:  #You have to make 3 correct turns
        print "You made it on the wave! Good job %s!" %name
        possible_turns = ['left', 'right'] #possibilities
        correct_turn = random.choice(possible_turns) #correct turn
        print
        print "You can turn the surfboard with your body. Do you turn left or right?"  #your chioces
        print "Type in 'left', or 'right'."
        print
        chioce_turn = raw_input(">")  #Your chioce
        if chioce_turn == 'q':
            sys.exit(0)
        if chioce_turn == correct_turn:
            print "You turned %s" %chioce_turn
            print "That was a good turn. You did a good job! Keep on going %s!" %name
            print 
            correct_surf_turns += 1
            if correct_surf_turns >= 3: #If you surfed the wave
                print "You did it!"
                print "You surfed your first wave %s!" %name
                break
            else:
                print "You try agian!"  #continuation
        else:
            print "You turned %s" %chioce_turn  #wrong way result
            print "You messed up and whiped out. You try agian."
            print
    #clue/pass
    print
    print "You get a clue. 'Now you have surfboared. Time to try out a diffrent board, at the MAUNA KEA VOLCANO. (Hint: Head south.) Good luck.'"
    print
    win.surf_pass = True

#15 SNOW CHALLENGE
def Snow():
    print "An amazing race instructor comes to you both. ‘This mountain is actually a Volcano called Mauna Kea Volcano. There is only snow very high up, so it’s a bit hard to breathe. This is a good challenge for you two. You are a bit behind the leaders, so the faster you learn to snowboard, the sooner you can get down from here and on to your 	 challenge.’ He gives you both snowboards and clothes to match this suddenly cold weather. You go to change into them, and are out soon to continue your mission. Then you both head out with the provided snowboards to learn!"
    print "You get on your board, and your partner does the same."
    print "'Snowboarding is done by using your body to turn the board the direction you want it to go. It is a lot like surfing, so if you did good on your last challenge, it will help here.'"
    correct_snow_turns = 0  #turns you got right
    
    while correct_snow_turns < 5:  #You have to make 5 correct turns
        possible_turns = ['left', 'right'] #possibilities
        correct_snow_turn = random.choice(possible_turns) #correct turn
        print
        print "You can turn your snowboard with your body. Do you turn left or right?"  #your chioces
        print "Type in 'left', or 'right'."
        print
        snow_chioce_turn = raw_input(">")  #Your chioce
        if snow_chioce_turn == 'q':
            sys.exit(0)
        if snow_chioce_turn == correct_snow_turn:
            print "You turned %s" %snow_chioce_turn
            print "That was a good turn. You did a good job and have great potential!"
            print 
            correct_snow_turns += 1
            if correct_snow_turns >= 5: #If you learned to snowboard
                print "You did it!"
                print "You boarded your 1st mountain %s!" %name
                break
            else:
                print "Keep going! You can do it %s!" %name #continuation
                print "JUST DO IT!!!"
        else:
            print "You turned %s" %snow_chioce_turn  #wrong way result
            print "You messed up and whiped out in the snow on the side of the mountain. You try agian."
            print
    #clue/pass
    print
    print "You get a clue. 'Now that you have learned to snowboard, get down the mountain as fast as you can and head west to KAUAI ISLAND! Learn the amazing art of working fire! It is a very popular pastime for tourists in the evening. Good luck.'"
    print
    win.snow_pass = True

#16 FIREWORKS CHALLENGE
def Fireworks():
    print "You both walk over to an instructor giving instructions to another team. A second team has already started their mission. ‘You must now learn the art of fireworks. We do a weekly show here, and we need some more fireworks. Do this right and we will use your fireworks for the show.’"
    print "You are equipped with two pre-drilled 3 inch paper hemispheres, a batch of 75 grams of 10 mm pumped 'Tiger tail' stars, a 'spolette' (a tube) to act as a fuse, a powder to act as a busrt charge, cardboard, paper, tape, string, and glue."
    print "IMPORTANT NOTE!!! DO NOT TRY THIS AT HOME OR ANYWHERE ELSE!!!"
    print
    print "You must now fill both hemispheres with the 'Tiger tail' stars, so type in 'fill'."
    fill_hems = raw_input(">")# the following gives instructions about what to type in and the player must do so.
    if fill_hems == "fill":
        print "Now you have to put in a piece of paper in each hemisphere, an then add the powder. Type in 'add' to add in the paper and powder."
        add = raw_input(">")
        if add == "add":
            print "Now you have to use the paper, tape, and glue to attach the two hemispheres and cover them completely. This should seal them together, and cover the two hemispherres. Type in 'seal', to seal the two hemispheres together."
            seal = raw_input(">")
            if seal == 'seal':
                print "Now type in 'cover', to cover the sphere."
                cover = raw_input(">")
                if cover == 'cover':
                    print "Beacuse the hemishere is pre-drilled you do not need to drill. Just add the 'spolette' as the fuse and attach some string at the end. Type in 'attach'."
                    attach = raw_input(">")
                    if attach == 'attach':
                        print "Now attach the carboard in a circle shape as a base of the firework. Type in 'attach' agian."
                        attach1 = raw_input(">")
                        if attach1 == 'attach':
                            print
                            print "You are done! You did it! An instructor comes to you, and looks at your now finished firework. 'It passes! Good job, here is your next clue.'"
                            print "The clue says, 'Head back to the Snowboarding mountain. From there go south to BIG ISLAND for a big experience!'"
                            print
                            win.fireworks_pass = True                            
                        else:
                            print "You were supposed to type in 'attach'."
                    else:
                        print "You were supposed to type in 'attach'."
                else:
                    print "You were supposed to type in 'cover'."
            else:
                print "You were supposed to type in 'seal'."
        else:
            print "You were supposed to type in 'add'."
    else:
        print "You were supposed to type in 'fill'."

#17 BAGS CHALLENGE
def Bags():
    print "‘You will get a hand woven bag. These bags are popular merchandise in Hawaii. With it you will find a piece of paper with the maker's name on it. You must find a bag that looks the same as yours, with the same name as it in the whole city. It is dark now so the task is harder than ever. Find the bag soon and get ahead. Find it late, and it might cost you the race.’"
    names = ['Sasha', 'Elizabeth', 'Kassidy', 'Kristin', 'Emily', 'Olivia', 'Ava', 'Sophia', 'Isabella', 'Avery', 'Madison', 'Chloe', 'Lily', 'Evelyn', 'Ellie', 'Natalie', 'Grace', 'Audrey', 'Victoria', 'Violet', 'Penelope', 'Stella']
    name = random.choice(names)
    print
    print "Your bag's maker is", name
    bag_found = False
    while bag_found == False:
        possible_bag_turns = ('left', 'right') #possible turns 
        bag_correct_turn = random.choice(possible_bag_turns)
        print "You can go left or right."
        print "Type in 'left', or 'right'"
        print
        bag_turn = raw_input(">")  #your chioce of turns
        if bag_turn == 'q':  #can leave challenge
            sys.exit(0)
        if bag_correct_turn == bag_turn:  #50/50 chance there are bags there
            print "There is a bag here! You check the name on the inside."
            bag_name = random.choice(names)  #the bag has a random maker from the list
            if name == bag_name: #if that bag is the one you were looking for
                print "You found the bag that was made by %s! You did it. Now you go back to the beggining of this challenge, and turn in the two bags to recive your next clue." %name
                bag_found = True
            else:  #if that bag was not the same
                print "The name in the bag is %s. Sorry, that is not the maker of your bag. Keep looking." %bag_name
                names.remove(bag_name)  #it removes that name from the list, so you won't find it agian.
        else:
            print "There are no bags here. Keep trying %s." %name #if there are no bags there
    #clue/pass
    print
    print "Your clue says, 'Go west to NIIHAU ISLAND, and lead one of the famous Hawiian tours!' (another challenge)"
    print
    win.bag_pass = True

#18 KAYAK CHALLENGE
def Kayak(): #Intro
    print "‘Kayaking is a popular pastime for both resident and tourist here. It is nice in the day, but the night has its own majesty that it reveals to the kayaker. You both will be tour guides along this path. (She hands you a map with a red path drawn on it going through the water.) This is where you will need your 100 dollars. You will need to rent kayaks for yourselves in order to lead the tour group.’"
    if win.ticket_pass:  #You have to have the 100 dollars from the earlier ticket challenege
        print "You both go to a booth and rent kayaks and helmets. You have 5 dollars extra from the original 100 dollars."
        print "You will lead the group, while your partner points out cool facts and places."
        print "    MAP"   #The map
        print "         |"
        print "         |"
        print "        /"
        print "       /"
        print "      |"
        print "      |"
        print "     /"
        print "    /"
        print "   |"
        print "   |"
        print "   /"
        print "  /"
        print " |"
        print " |"
        correct_kayak_turns = 0
        while correct_kayak_turns < 7:  #You need a total of 7 correct turns
            print
            print "Now you have to go straight up. Type 'up'."  #you have to go up
            up = raw_input(">")
            if up =='q':
                sys.exit(0)
            if up == 'up':
                correct_kayak_turns += 1
                print "Now type 'right', for this next right turn." #you have to go right
                print
                right = raw_input(">")
                if right =='q':
                    sys.exit(0)
                if right == 'right':
                    correct_kayak_turns += 1  #one more correct turn
                    print "Good job."
                else:
                    print "You almost crashed. You should have typed 'right'."
            else:
                print "You almost crashed. You should have typed 'up'."
        #Outro/clue/pass
        print "You did it. You made it to the end of the kayak path!"
        print "You get a clue: 'You did it! You have completed all of the challenges! Now rush to the USS Arizona Memorial in the Pearl City harbor if you want to win! When you get there, type in 'next'.'"
        print
        win.Kayak_pass = True
    else:  #if you did not do the ticket challenge
        print
        print "You did not do the ticket selling challenge earlier, and so now you don't have 100 dollars to rent kayaks. You have failed %s. Good bye.  :|" %name
        end.end = True    

def Win():
    global start_time
    print
    print "You run across the streets of Pearl City, Hawaii on Oahu Island. You are not far behind another team. But these streets are so confusing. The other team stops and asks for directions, then rushes off into the night. Them asking for directions got you both a few seconds closer to them. You keep on running, hoping you are leading yourselves in the right direction. You and your partner rush past the other team, who are confusing of where to go at an intersection. You just keep running. Finally you see it. There is the Harbor. You run to the loading dock. You can see the people from The Amazing Race over the sunken ship in the harbor. You run up to the gate, but the old man there says, ‘Sorry, no passage without paying the fee. It’s $2.15 per person, $1.10 per child, and $3.45 per pet.’ You feel greatly pleased with yourself as you remember you kept the spare change from the kayaks. You hurriedly pay the man $4.30 and rush to the boats. There are many rowboats, each with a clue on the seat. You open one. ‘A final test of power, strength, and determination: work together to reach the end.’ You both hop into a rowboat, but so do another other two teams. Your partner is on your left, and has that oar, while you hold the right. You both row to the USS Arizona Memorial in the harbor."
    print
    end_time = time.time()
    global end_time
    elapsed_time = end_time - start_time
    print "Good job %s! You made it to the end." %name
    print "You took %d seconds to get to the end." %elapsed_time
    print
    if elapsed_time <= 1500: #25 minutes
        if win.scuba_pass and win.coco_pass and win.dance_pass and win.book_pass and win.castle_pass and win.coffee_pass  and win.fish_pass  and win.hang_pass and win.ticket_pass and win.Lava_pass and win.sand_pass and win.tiki_pass and win.surf_pass and win.snow_pass and win.fireworks_pass and  win.bag_pass and win.Kayak_pass:
            print "You both finally reach the end. Another team is even with you, and there is another getting close. Some teams are just getting into rowboats. Your team and the other team rush to the end. But you get there first. ‘Good job %s! You barely made it. You got first in this round of THE AMAZING RACE! For your great work and effort you have won a trip to the Netherlands! Where there is endless green hills, and windmills! Have fun! AND YOU WILL HAVE A CHANCE TO COMPETE FOR THE GRAND PRIZE OF ONE MILLION DOLLARS! Good luck and we will see you again next week, on The Amazing Race’." %name
            end.end = True
        else:
            print "You both finally reach the end. Another team is even with you, and there is another getting close. Some teams are just getting into rowboats. Your team and the other team rush to the end. But they get there first. The announcer says to the other team, ‘Good job. You barely made it. But you got first in this round of THE AMAZING RACE! For your great work and effort you have won a trip to the Netherlands. Where there is endless green hills, and windmills! Have fun! AND YOU WILL HAVE A CHANCE TO COMPETE FOR THE GRAND PRIZE OF ONE MILLION DOLLARS!’ Sadly you have not made it in time to be first, but you will be in the next round, and will compete for one million dollars. But you don’t get a trip to the Netherlands, where there is endless green hills, and windmills! ‘Good luck and we will see you again next week, on The Amazing Race.’"
            end.end = True  
    if elapsed_time > 1500 and elapsed_time <= 2700: #45 minutes
        print "You both finally reach the end. Another team is even with you, and there is another getting close. Some teams are just getting into rowboats. Your team and the other team rush to the end. But they get there first. The announcer says to the other team, ‘Good job. You barely made it. But you got first in this round of THE AMAZING RACE! For your great work and effort you have won a trip to the Netherlands. Where there is endless green hills, and windmills! Have fun! AND YOU WILL HAVE A CHANCE TO COMPETE FOR THE GRAND PRIZE OF ONE MILLION DOLLARS!’ Sadly you have not made it in time to be first, but you will be in the next round, and will compete for one million dollars. But you don’t get a trip to the Netherlands, where there is endless green hills, and windmills! ‘Good luck and we will see you again next week, on The Amazing Race.’" 
        end.end = True
    if elapsed_time > 2700: #45 minutes
        print "You did not make it in time. You took too long to finish. You came in last. You lost. You have failed. You do not ever get to compete again. Try again later %s." %name
        end.end = True

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
Intro = Room('Introduction',                   None, None, None, None, 'Clue_One',                                                 '‘Aloha, and welcome %s, to Honolulu, Hawaii, on Oahu Island. You and your partner must complete all 18 challenges, follow the clues given and reach the end to win this race. Here is your first clue. (You are handed an envelope with the Amazing Race Insignia.) Good luck racers.’ \x1B[3m*(Hint: Type "next" to go on. This will be a miscellanous direction/move.)*\x1B[23m' %name)
Clue_One = Room('Clue One',                    None, None, None, None, 'Beginning_Plaza',                                          'Find the South Beach, where a challenge awaits, go diving and finding, good luck mates. Go to the South beach and play the scuba challenge.')
Beginning_Plaza = Room('Plaza',                'Volcano', 'South_Beach', 'East_Beach', 'Pearl_City_Harbor', None,                  'This has all taken place in the plaza in the middle of Honolulu on the island of Oahu. You see a sign not far from where you and your teammate are. You call your teammate over and rush to see the sign. Other teams have the same idea, and soon the sign is crowded. You see that north leads you to a volcano, and west leads to Pearl City and Pearl Harbor. East takes you to East Beach, and south will bring you to South Beach. (Amazing names I know). Which direction will you take?')
South_Beach = Room('South Beach',              'Plaza', 'Coconut_grove', 'Maui_Island', 'Big_Island', Scuba,                       'You and your partner rush past opposing racers and head for South Beach. It’s not far, but by the end of the sprint, you are exhausted. You see some people with Amazing Race shirts. You head in their direction, fast walking this time. To your west you see a lot of boats and a sign that says, ‘To Big Island’. To the east there are helicopters with a sign that says, ‘To Maui Island’. Going south will lead you to a coconut grove. There is a scuba challenge here.')
Coconut_grove = Room('Coconut Grove',          'South_Beach', 'Hula_dance', None, None, CoCo,                                      'You both rush to coconut grove after you are done changing back into your clothes. You head south, and sure enough there is a coconut grove, with a group of people around it. It seems like some other teams are ahead of you, but you will catch up to them soon enough. The only directions you can go are further south, and back up north. But first you must complete the next challenge.')
Hula_dance = Room('Hula Dance Central',        'Coconut_grove', None, None, None, Dance,                                           'You reach the next checkpoint at the Hula Dance Central a bit further ahead than you were, but still not in first place you realize because another team is already there. This is as far south as you can go, you will have to return going north, but first you need to do your mission.')
Maui_Island = Room('Maui Island',              'Coffee_Farm', None, 'Maui_Beach', None, Book,                                      'You head by helicopter to Maui Island. The view is amazing. There is the beach, and you can even see some other teams down there. But you have fallen farther behind. Learning to dance took you too long. You and your partner must make up for lost time. You touch down at the University of Hawaii, on Maui Island. There are boats on the north to take you back to Oahu Island when you are done here. Going west will take to you Maui Beach.')
Maui_Beach = Room('Maui Beach',                None, None, None, 'Maui_Island', Sandcastle,                                        'You reach the beach exhausted. Your partner doesn’t seem too energetic either. When you are done, you will have to go back to the University, and then go north to reach the boats to get back to Oahu Island. But now you must start your challenge.')
Coffee_Farm = Room('Coffee Farm',              'East_Beach', None, 'Lanai_Island', None, Coffee,                                   'You are back on Oahu Island at a coffee farm. There is a sign to your north, saying ‘East Beach’. And also another one pointing east that says, ‘Lanai Island’. First there must be a challenge to complete here.')
Lanai_Island = Room('Lanai Island',            None, None, None, 'Coffee_Farm', Fishing,                                           'Your boat gets to Lanai Island. The boat will stay here for you to go back west to Oahu Island when you need to.')
East_Beach = Room('East Beach',                'Miwiwe_Street', 'Coffee_Farm', 'Seal_Show', 'Plaza', Hangman,                      'You have finally reached the East Beach of Oahu Island. To your east is a seal show, and to the west is the plaza. North will take you to street called Miwiwe. There is a crowd of people at several tables set up with the Amazing Race banner over them.')
Seal_Show = Room('Seal_Show',                  None, None, None, 'East_Beach', Tickets,                                            'You have reached the seal show. To return, you will need to go west back to the East Beach, and then continue. But for now, your challenges must be met.')
Miwiwe_Street = Room('Miwiwe Street',          None, 'East_Beach', None, None, RR,                                                 'You and your partner are walking down the street Miwiwe. The only path it seems is going back south to East Beach. You are suddenly surrounded by cops, helicopters and squad cars! An agent comes to you. ‘My name is Lt. Commander Steve McGarrett – Hawaii Five-0. This is a restricted area. Please leave.’ You timidly shake your head yes and start to leave. You are walking along the sidewalk back south to the East Beach. But then…')
Plaza = Room('Plaza',                          'Volcano', 'South_Beach', 'East_Beach', 'Pearl_City_Harbor', None,                  'You walk into the plaza, where you started. By now, most of the decorations and floral arrangements are gone. From here you can go north to the Volcano, south to South Beach, and west to Pearl Harbor, or east to East Beach.')
Volcano = Room('Volcano',                      'North_Beach', 'Plaza', 'Northeast_Beach', 'Northwest_Beach', Lava,                 'You reach the volcano summit. From here you can go south to the plaza, east to Northeast beach, and west to Northwest beach, or north to North beach. But it appears there is a challenge here.')
Northeast_Beach = Room('Northeast Beach',      None, None, None, 'Volcano', Sand,                                                  'You get down the volcano where some teams are still working. You need to work faster so you can catch up. Going west will take you back up there. But there is another challenge ahead.')
North_Beach = Room('North Beach',              None, 'Volcano', None, None, Tiki,                                                  'You walk down the volcano to another beach, called North Beach. ‘There are several large tiki towers over there’, you tell your partner and you both walk that way. You will have to go south back up the mountain to get back, but for now it looks like you have another mission.')
Northwest_Beach = Room('Northwest Beach',      None, 'Mauna_Kea_Volcano', 'Volcano', None, Surf,                                   'You reach another beach. East will take you to the Volcano, and south will take you to a mountain called Mauna Kea Volcano. By this time you feel you have seen almost all the world’s beaches. The expression on your partners face shows she feels the same. But it looks like there is a surfing competition here or something.')
Mauna_Kea_Volcano = Room('Mauna Kea Volcano',  'Northwest_Beach', 'Big_Island', 'Pearl_City_Harbor', 'Kauai_Island', Snow,         'You climb up the mountain. It is called Mauna Kea Volcano, but it is not active. From the top you can see that to the west is Pearl Harbor.  To the east is another island, Kauai Island. South you see another island, Big Island. North would take you to the Northwest beach. There is snow on this mountain. It looks like this is the place for another challenge.')
Kauai_Island = Room('Kauai Island',            None, None, 'Mauna_Kea_Volcano', None, Fireworks,                                   'You ride the snowboards as far down as you can, then you change out of the clothes and boards when the snow runs out. You jog down the rest of the mountain. You did pass up a few teams going down the mountain. Good job! You reach the Kauai Island by boat. By now it is evening. Going east will take you back to the Mountain. There are two teams already on the island. There is one more in a boat coming to the island. You have caught up with the leaders!')
Big_Island = Room('Big Island',                'Mauna_Kea_Volcano', None, 'South_Beach', 'Niihau_Island', Bags,                    'You reach this island by boat, and get off in a hurry. You now have a chance to pass the two leading teams up. You can go north to the Mauna Kea Volcano, east to South Beach, or west to Niihau Island. An Amazing Race instructor is comes to assist you. ‘This is the Big Island, filled with big people, big cars, big houses, and big stuff. People love to buy stuff from here, and it is a popular tourist attraction.’')
Niihau_Island = Room('Niihau_Island',          None, None, 'Big_Island', None, Kayak,                                              'You have reached the island by speed boat. By now it is night, and the Hawaiian skyline is lit up beautifully with all sorts of colors and lights. In the distance you can see the firework show begin. You can go east to the Big Island or continue. An instructor comes to your team.')
Pearl_City_Harbor = Room('Pearl City Harbour', None, None, 'Plaza', 'Mauna_Kea_Volcano', Win,                                      'You are at the Pearl City Harbor. There in the water you can see the USS Arizona Memorial. You can go west to the Mauna Kea Volcano, or east to the Plaza.')  #Normal plaza
Pearl_Harbour = Room('Pearl Harbour',          None, None, None, None, None,                                                       'You run across the streets of Pearl City, Hawaii on Oahu Island. You are not far behind another team. But these streets are so confusing. The other team stops and asks for directions, then rushes off into the night. Them asking for directions got you both a few seconds closer to them. You keep on running, hoping you are leading yourselves in the right direction. You and your partner rush past the other team, who are confusing of where to go at an intersection. You just keep running. Finally you see it. There is the Harbor. You run to the loading dock. You can see the people from The Amazing Race over the sunken ship in the harbor. You run up to the gate, but the old man there says, ‘Sorry, no passage without paying the fee. It’s $2.15 per person, $1.10 per child, and $3.45 per pet.’ You feel greatly pleased with yourself as you remember you kept the spare change from the kayaks. You hurriedly pay the man $4.30 and rush to the boats. There are many rowboats, each with a clue on the seat. You open one. ‘A final test of power, strength, and determination: work together to reach the end.’ You both hop into a rowboat, but so do another other two teams. Your partner is on your left, and has that oar, while you hold the right. You both row to the USS Arizona Memorial in the harbor.')

node = Intro  #Beggining Room       

def save():
    global name, start_time, win, node
    with open('savegame.dat', 'wb') as f:
        pickle.dump([name, start_time, win, node], f, protocol = 2)
    print "Game succsessfully saved"
    
def load():
    global name, start_time, win, node
    with open('savegame.dat', 'rb') as f:
        name, start_time, win, node = pickle.load(f)
    print "Game succsessfully loaded"

while True:
    print
    if end.end == True:
        sys.exit(0)
        break
    print "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    print "ROOM: " + node.name  #prints name of room
    print "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    print
    print "DESCRIPTION: " + node.description   #prints description of room
    print
    if node.north!=None :
        print "---North"
    if node.south!=None :
        print "---South"
    if node.east!=None :
        print "---East"
    if node.west!=None :
        print "---West"
    if node.next!=None :
        print "---Next"
    command = raw_input(">").strip().lower() #gets your command
    if command in ['q', 'quit', 'exit']:     #you can exit mid-game
        print "GAME OVER"
        sys.exit(0)
    elif command in ["save"]:
        save()
    elif command in ["load"]:
        load()
    elif command in 'next':  #if command starts a function
        try:
            function = node.next
            function()    #then it will run that function
        except:          #except if it's not a function
            try:
                node.move(command)   #then move
            except:
                pass
    elif command in ['north', 'south', 'east', 'west', 'next', '?']:  #if possible movement path
        try:
            node.move(command)   #then move
        except:
            try:
                if command == "?":
                    print directions
                    pass
            except:
                print "That command is invalid. You can not go that way. Sorry, maybe you should try going another way."   #if not then say so
            
    else:
        print
        print "That command is invalid. You can not go that way. Sorry, maybe you should try going another way."   #if not then say so