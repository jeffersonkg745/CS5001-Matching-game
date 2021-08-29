'''
Kaelyn Jefferson
Fall 2020
CS5001: Final Project

"Memory Matching Game"
'''
import turtle
import random
import time
screen = turtle.Screen()


# global variables holding player info (name and number of cards chosen)
player_name = []
cards_number = []



def welcome_user():
    '''
    name: welcome_user
    parameters: none
    function: asks user info (name, number of cards) on popup window. Accepts even
    numbers, for odd it gives a second chance then rounds to nearest number of cards.
    Returns player name and card_number.
    '''
    # ask user name; if player "cancels" during name input, returns a 0
    player_name = turtle.textinput("Name Input", "Name of player: ")
    if player_name == None:
        return 0

    # ask user card number
    cards_number = turtle.numinput("Number of Cards", "How many cards (8, 10, or 12)?", \
                                   minval = 8, maxval = 12)
    # if odd number of cards entered (9 or 11), then given user second chance
    if cards_number == int(9) or cards_number == type(11):
        cards_number = turtle.numinput("Your answer was an odd number!", \
                                       "Enter an *even* number or your answer will round to closest number",\
                                        minval = 8, maxval = 12)
        # if in second chance, user still inputs odd numbers, then assume next number as answer
        if cards_number == 9:
            cards_number = 10
        elif cards_number == 11:
            cards_number = 12
            
    # if player "cancels" during card number input, returns a 0
    elif cards_number == None:
        return 0

    return (player_name, cards_number)

def create_board():
    '''
    name: create_board
    parameters: None
    function: sets screen size, creates game board outlline (box for cards, leaderboard, and status bar)
    '''
    # sets screen size
    turtle.screensize(canvwidth = 900, canvheight = 800)

    # create box for cards
    turtle.penup()
    turtle.goto(-325, 300)
    turtle.hideturtle()
    turtle.pensize(10)
    turtle.pencolor("purple")
    turtle.pendown()
    turtle.setheading(0) 
    turtle.forward(500)
    turtle.setheading(270) 
    turtle.forward(500)
    turtle.setheading(180) 
    turtle.forward(500)
    turtle.setheading(90) 
    turtle.forward(500)
    turtle.penup()

    # create leaderboard
    turtle.goto(200, 300)
    turtle.pencolor("blue")
    turtle.pendown()
    turtle.setheading(0) 
    turtle.forward(120)
    turtle.setheading(270)
    turtle.forward(500)
    turtle.setheading(180) 
    turtle.forward(120)
    turtle.setheading(90) 
    turtle.forward(500)
    turtle.penup()

    # create status bar at bottom
    turtle.goto(-325, -220)
    turtle.pencolor("purple")
    turtle.pendown()
    turtle.setheading(0) 
    turtle.forward(500)
    turtle.setheading(270) 
    turtle.forward(80)
    turtle.setheading(180) 
    turtle.forward(500)
    turtle.setheading(90) 
    turtle.forward(80)
    turtle.penup()
    turtle.hideturtle()

def add_stop():
    '''
    name: add_stop
    parameters: none
    function: places quit button on board
    '''

    # places "stop" button on board
    turtle.goto(260,-260)
    turtle.showturtle()
    turtle.register_shape("quitbutton.gif")
    turtle.shape("quitbutton.gif")
    

def add_leaderboard():
    '''
    name: add_leaderboard
    parameters: none
    function: Creates leaderboard text, reads from 'winners.txt' to sort and present top 6
    winners on leaderboard. If no 'winners.txt' (new player) then doesn't add score yet.
    '''

    # creates leaderboard header text
    turtle.clone()
    turtle.hideturtle()
    turtle.goto(210,270)
    turtle.pencolor("blue")
    turtle.getpen()
    turtle.write("Leaderboard:", move = False, align = "left", font=('Arial', 16, "bold"))


    # reads from 'winners.txt' and appends to leaderboard_dict
    
    leaderboard_dict = {}
    try:
        with open('winners.txt', mode = 'r') as winners:
                winner_dict = (winners.readlines())
                for each in winner_dict:
                    each = each.strip()
                    each = each.strip(" ")
                    each = each.split(":")
                    leaderboard_dict[each[0]] = each[1]

                    # leaderboard data sent from dictionary to list to order correctly
                    list_1 = []
                    for key in leaderboard_dict:
                        list_1.append(int(key))
                        list_1.sort()

                # prints top 6 winners on leaderboard
                for each in list_1[0:6]:
                    each = str(each)
                    turtle.setheading(270)
                    turtle.forward(40)
                    turtle.write(each, move = False, align = "left", font = ('Arial', 16, "normal"))
                    turtle.setheading(0)
                    turtle.forward(10)
                    turtle.write("  :  ", move = False, align = "left", font = ('Arial', 16, "normal"))
                    turtle.forward(20)
                    turtle.write(leaderboard_dict[each], move = False, align = "left", font = ('Arial', 16, "normal"))
                    turtle.setheading(180)
                    turtle.forward(30)

    # if file winners.txt does not exist (new player), then doesn't add score yet                
    except FileNotFoundError:
        return
   
    
def add_statusboard():
    '''
    name: add_statusboard
    parameters: none
    function: Reads from 'guesses.txt', 'matches.txt', and 'cardcount.txt' files.
    If they don't exist, then they are created here. The text is printed to the game
    to keep track of score with regards to number of guesses and matches.
    '''


    # creates files if don't exist to keep track of number of guesses, matches, and card count
    with open('guesses.txt', mode = 'a') as guesses:
            guesses.write('')
    with open('matches.txt', mode = 'a') as matches:
            matches.write('')
    with open('card_count.txt', mode = 'a') as card_count:
            card_count.write('')

    # reads from the files to print messages below (for statusboard) 
    guess_num = open('guesses.txt', 'r')
    guesses = guess_num.readlines()
    for guess in guesses:
        guess_count = guess
        amt_guesses = len(guess_count)
    matches_num = open('matches.txt', 'r')
    matches = matches_num.readlines()
    for match in matches:
        match_count = match
        amt_matches = len(match_count)
    

    # creates text presented on statusboard (and accounts for UnboundLocalError when no files yet)
    turtle.pencolor("purple")
    turtle.goto(-240, -270)
    turtle.write("Status- ", move = False, align = "left", font = ('Arial', 16, "bold"))
    turtle.setheading(0)
    turtle.forward(90)
    turtle.write("Guesses:", move = False, align = "left", font = ('Arial', 16, "normal"))
    turtle.forward(80)
    try:
        turtle.write(amt_guesses, move = False, align = "left", font = ('Arial', 16, "normal"))
    except UnboundLocalError:
        amt_guesses = 0
        turtle.write(amt_guesses, move = False, align = "left", font = ('Arial', 16, "normal"))
    turtle.forward(40)
    turtle.write("Matches:", move = False, align = "left", font = ('Arial', 16, "normal"))
    turtle.forward(80)
    try:
        turtle.write(amt_matches, move = False, align = "left", font = ('Arial', 16, "normal"))
    except UnboundLocalError:
        amt_matches = 0
        turtle.write(amt_matches, move = False, align = "left", font = ('Arial', 16, "normal"))


                 

def add_cards():
    '''
    name: add_cards
    parameters: none
    function: adds specified number of cards (8,10, or 12) according to user input. 
    '''

    # creates 8 cards if user specifies it
    if cards_number[0] >= 8:
        turtle.setpos(-260,210)
        turtle.register_shape("card_back.gif")
        turtle.shape("card_back.gif")
        for i in range(4):
            turtle.stamp(); turtle.fd(120)   
        turtle.setpos(-260,50)
        for i in range(4):
            turtle.stamp(); turtle.fd(120)
            
    # creates 10 cards if user specifies it
    if cards_number[0] >= 10:
        turtle.setpos(-260, -110)
        for i in range(2):
            turtle.stamp(); turtle.fd(120)

    # creates 12 cards if user specifies it
    if cards_number[0] == 12:
        turtle.setpos(-20, -110)
        for i in range(2):
            turtle.stamp(); turtle.fd(120)
    turtle.hideturtle()
    turtle.setpos(400,400)

def make_dict():
    '''
    name: make_dict
    parameters: none
    function: creates 3 dictionaries for 8, 10, and 12 randomly assorted cards
    which is used by the flip function
    '''

    # for 8 cards
    shape8_dict = {}
     
    list8_num = ['1','2','3','4','5','6','7','8']
    list8_pictures = ["2_of_clubs.gif","2_of_clubs.gif","ace_of_diamonds.gif", "ace_of_diamonds.gif",\
                                     "2_of_diamonds.gif", "2_of_diamonds.gif", "3_of_hearts.gif", "3_of_hearts.gif"]
    random.shuffle(list8_num)
    random.shuffle(list8_pictures)
    
    i = 0
    while i < len(list8_num):
        shape8_dict[list8_num[i]] = list8_pictures[i]
        i+=1


        
    # for 10 cards
    shape10_dict = {}

    list10_num = ['1','2','3','4','5','6','7','8', '9','0']
    list10_pictures = ["2_of_clubs.gif","2_of_clubs.gif","ace_of_diamonds.gif", "ace_of_diamonds.gif",\
                    "2_of_diamonds.gif", "2_of_diamonds.gif", "3_of_hearts.gif", "3_of_hearts.gif", \
                     "jack_of_spades.gif", "jack_of_spades.gif"]

    random.shuffle(list10_num)
    random.shuffle(list10_pictures)

    i = 0
    while i < len(list10_num):
        shape10_dict[list10_num[i]] = list10_pictures[i]
        i+=1



    # for 12 cards
    shape12_dict = {}

    list12_num = ['1','2','3','4','5','6','7','8', '9','0','a','b']
    list12_pictures = ["2_of_clubs.gif","2_of_clubs.gif","ace_of_diamonds.gif", "ace_of_diamonds.gif",\
                    "2_of_diamonds.gif", "2_of_diamonds.gif", "3_of_hearts.gif", "3_of_hearts.gif", \
                     "jack_of_spades.gif", "jack_of_spades.gif", "king_of_diamonds.gif", "king_of_diamonds.gif"]

    random.shuffle(list12_num)
    random.shuffle(list12_pictures)

    i = 0
    while i < len(list12_num):
        shape12_dict[list12_num[i]] = list12_pictures[i]
        i+=1


    return (shape8_dict, shape10_dict, shape12_dict)


    
def flip(x,y, shape_dict = make_dict()):
    '''
    name: flip
    parameters: x, y from Turtle function: turtle.onclick(), shape_dict (type = dictionary)
    function: imports dictionary so when click function gets an x and y coordinate, it will
    flip correct card/or stop to quit. These numbers from each card are stored in a file.
    When the file has 2 numbers (or 2 cards are flipped) then it goes to game().
    '''
    
    
    #dictionary depending on number of cards
    if cards_number[0] == 8:
        shape_dict = shape_dict[0]
    elif cards_number[0] == 10:
        shape_dict = shape_dict[1]
    elif cards_number[0] == 12:
        shape_dict = shape_dict[2]
    
    
    #card1 flipped
    if x > -306 and x < -213 and y < 280 and y > 136:
        turtle.setpos(-260,210)
        turtle.showturtle()
        turtle.register_shape(shape_dict['1'])
        turtle.shape(shape_dict['1'])
        turtle.stamp() 
        turtle.hideturtle()
        # write to file with the card count
        with open('card_count.txt', mode = 'a') as card_count:
            card_count.write('1')
        
    #card2 flipped  
    if x > -180 and x < -100 and y < 280 and y > 136:
        turtle.setpos(-140, 210)
        turtle.showturtle()
        turtle.register_shape(shape_dict['2'])
        turtle.shape(shape_dict['2'])
        turtle.stamp()
        turtle.hideturtle()
        # write to file with the card count
        with open('card_count.txt', mode = 'a') as card_count:
            card_count.write('2')
        
    #card3 flipped
    if x > -64 and x < 31 and y < 280 and y > 136:
        turtle.setpos(-20, 210)
        turtle.showturtle()
        turtle.register_shape(shape_dict['3'])
        turtle.shape(shape_dict['3'])
        turtle.stamp()
        turtle.hideturtle()
        # write to file with the card count
        with open('card_count.txt', mode = 'a') as card_count:
            card_count.write('3')
         
    #card4 flipped
    if x > 55 and x < 277 and y < 280 and y > 136:
        turtle.setpos(100, 210)
        turtle.showturtle()
        turtle.register_shape(shape_dict['4'])
        turtle.shape(shape_dict['4'])
        turtle.stamp()
        turtle.hideturtle()
        with open('card_count.txt', mode = 'a') as card_count:
            card_count.write('4')
        
    #card5 flipped
    if x > -306 and x < -213 and y < 122 and y > -20:
        turtle.setpos(-260, 50)
        turtle.showturtle()
        turtle.register_shape(shape_dict['5'])
        turtle.shape(shape_dict['5'])
        turtle.stamp()
        turtle.hideturtle()
        with open('card_count.txt', mode = 'a') as card_count:
            card_count.write('5')
        
    #card6 flipped  
    if x > -186 and x < -92 and y < 122 and y > -20:
        turtle.setpos(-140, 50)
        turtle.showturtle()
        turtle.register_shape(shape_dict['6'])
        turtle.shape(shape_dict['6'])
        turtle.stamp()
        turtle.hideturtle()
        with open('card_count.txt', mode = 'a') as card_count:
            card_count.write('6')
        
    #card7 flipped
    if x > -65 and x < 30 and y < 122 and y > -20:
        turtle.setpos(-20, 50)
        turtle.showturtle()
        turtle.register_shape(shape_dict['7'])
        turtle.shape(shape_dict['7'])
        turtle.stamp()
        turtle.hideturtle()
        with open('card_count.txt', mode = 'a') as card_count:
            card_count.write('7')
        
    #card8 flipped
    if x > 57 and x < 144 and y < 122 and y > -20:
        turtle.setpos(100, 50)
        turtle.showturtle()
        turtle.register_shape(shape_dict['8'])
        turtle.shape(shape_dict['8'])
        turtle.stamp()
        turtle.hideturtle()
        with open('card_count.txt', mode = 'a') as card_count:
            card_count.write('8')
        
    #card9 flipped
    if x > -306 and x < -213 and y < -38 and y > -180:
        turtle.setpos(-260, -110)
        turtle.showturtle()
        turtle.register_shape(shape_dict['9'])
        turtle.shape(shape_dict['9'])
        turtle.stamp()
        turtle.hideturtle()
        with open('card_count.txt', mode = 'a') as card_count:
            card_count.write('9')
    #card10 flipped
    if x > -185 and x < -90 and y < -38 and y > -180:
        turtle.setpos(-140, -110)
        turtle.showturtle()
        turtle.register_shape(shape_dict['0'])
        turtle.shape(shape_dict['0'])
        turtle.stamp()
        turtle.hideturtle()
        with open('card_count.txt', mode = 'a') as card_count:
            card_count.write('0')
    #card11 flipped
    if x > -65 and x < 28 and y < -38 and y > -180:
        turtle.setpos(-20, -110)
        turtle.showturtle()
        turtle.register_shape(shape_dict['a'])
        turtle.shape(shape_dict['a'])
        turtle.stamp()
        turtle.hideturtle()
        with open('card_count.txt', mode = 'a') as card_count:
            card_count.write('a')
    #card12 
    if x > 56 and x < 150 and y < -38 and y > -180:
        turtle.setpos(100, -110)
        turtle.showturtle()
        turtle.register_shape(shape_dict['b'])
        turtle.shape(shape_dict['b'])
        turtle.stamp()
        turtle.hideturtle()
        with open('card_count.txt', mode = 'a') as card_count:
            card_count.write('b')

    # stop
    if x > 229 and x < 289 and y < -243 and y > -279:
        clear_scores()
        turtle.setpos(0,0)
        turtle.showturtle()
        turtle.register_shape('quitmsg.gif')
        turtle.shape('quitmsg.gif')
        turtle.stamp()
        turtle.hideturtle()
        turtle.delay(3000)
        turtle.fd(1)
        turtle.bye()
        
    
    # each card writes a number to a file, then this reads the file
    pic_num = open('card_count.txt', 'r')
    pictures = pic_num.readlines()
    for picture in pictures:
        card_count = picture

    try:
        # if card count is length 2, then goes to game function
        if len(card_count) == 2:
            game(shape_dict, card_count)
            
            #restart card count after 2 cards
            with open('card_count.txt', mode = 'w') as card_count:
                card_count.write('')
    except UnboundLocalError:
        return
        
       
def game(shape_dict, card_count):
    '''
    name: game
    parameters: shape_dict (type: dictionary), card_count (type: list)
    function: compares cards (if match/don't match) then removes stamps and sends to update_board and
    check_win function
    '''

    #use to delay card flip
    time.sleep(1)
    
    # if cards match, then clears stamps of those cards and sends points to update board function
    if (shape_dict[(card_count[0])]) == (shape_dict[(card_count[1])]):
        point = 1
        update_board(point)

        if card_count[0] == '1' or card_count[1] == '1':
            turtle.clearstamp(36)
        if card_count[0] == '2' or card_count[1] == '2':
            turtle.clearstamp(37)
        if card_count[0] == '3' or card_count[1] == '3':
            turtle.clearstamp(38)
        if card_count[0] == '4' or card_count[1] == '4':
            turtle.clearstamp(39)
        if card_count[0] == '5' or card_count[1] == '5':
            turtle.clearstamp(40)
        if card_count[0] == '6' or card_count[1] == '6':
            turtle.clearstamp(41)
        if card_count[0] == '7' or card_count[1] == '7':
            turtle.clearstamp(42)
        if card_count[0] == '8' or card_count[1] == '8':
            turtle.clearstamp(43)
        if card_count[0] == '9' or card_count[1] == '9':
            turtle.clearstamp(44)
        if card_count[0] == '0' or card_count[1] == '0':
            turtle.clearstamp(45)
        if card_count[0] == 'a' or card_count[1] == 'a':
            turtle.clearstamp(46)
        if card_count[0] == 'b' or card_count[1] == 'b':
            turtle.clearstamp(47)

    # if cards don't match, then update board with 0 points
    else:
        point = 0
        update_board(point)

        
    # "turns back over" the two cards that were flipped
    turtle.clearstamps(-2)

    # updates board's score
    add_status()

    # checks if win game
    check_win()
    

def update_board(point):
    '''
    name: update_board
    parameters: point (type int)
    function: updates the files for number of guesses and matches
    '''

    if point == 1:
        with open('guesses.txt', mode = 'a') as guesses:
            guesses.write('1')
        with open('matches.txt', mode = 'a') as matches:
            matches.write('1')

    if point == 0:
        with open('guesses.txt', mode = 'a') as guesses:
            guesses.write('1')
     

def add_status():
    '''
    name: add_status
    parameters: none
    function: draws a square over previous point board (to hide it), writes new text for
    keeping score count
    '''

    # draws white square over current points to "hide" the old text
    turtle.goto(-120, -260)
    turtle.shape("square")
    turtle.pencolor("white")
    turtle.fillcolor("white")
    turtle.shapesize(2,20)
    turtle.stamp()
    turtle.clone()


    # reads from guesses and matches files
    guess_num = open('guesses.txt', 'r')
    guesses = guess_num.readlines()
    for guess in guesses:
        guess_count = guess
        amt_guesses = len(guess_count)
    matches_num = open('matches.txt', 'r')
    matches = matches_num.readlines()
    for match in matches:
        match_count = match
        amt_matches = len(match_count)
    
    # writes text on point board to update user on current scores
    turtle.pencolor("purple")
    turtle.goto(-240, -270)
    turtle.write("Status- ", move = False, align = "left", font = ('Arial', 16, "bold"))
    turtle.setheading(0)
    turtle.forward(90)
    turtle.write("Guesses:", move = False, align = "left", font = ('Arial', 16, "normal"))
    turtle.forward(80)

    try:
        turtle.write(amt_guesses, move = False, align = "left", font = ('Arial', 16, "normal"))
    except UnboundLocalError:
        amt_guesses = 0
        turtle.write(amt_guesses, move = False, align = "left", font = ('Arial', 16, "normal"))
    
    turtle.forward(40)
    turtle.write("Matches:", move = False, align = "left", font = ('Arial', 16, "normal"))
    turtle.forward(80)
    
    try:
        turtle.write(amt_matches, move = False, align = "left", font = ('Arial', 16, "normal"))
    except UnboundLocalError:
        amt_matches = 0
        turtle.write(amt_matches, move = False, align = "left", font = ('Arial', 16, "normal"))
    

def check_win():
    '''
    name: check_win
    parameters: none
    function: reads from number of matches to determine if the person has "won" the game
    '''

    #reads from matches file that keeps track of # of matches
    matches_num = open('matches.txt', 'r')
    matches = matches_num.readlines()
    for match in matches:
        match_count = match
        amt_matches = len(match_count)
    
    try:
        #if the amount of matches = half the players cards, then save score, and clear this game score
        if amt_matches == int(cards_number[0])/2:
            save_win()
            clear_scores()
            turtle.setpos(0,0)
            turtle.showturtle()
            turtle.register_shape('winner.gif')
            turtle.shape('winner.gif')
            turtle.stamp()
            turtle.hideturtle()
            turtle.delay(3000)
            turtle.fd(1)
            turtle.bye()
        
        else:
            return
    except UnboundLocalError:
        return
        

def save_win():
    '''
    name: save_win
    parameters: none
    function: reads from file 'guesses.txt' and 'winners.txt' to update the file
    with winner data called 'winners.txt'.
    '''

    # open file and get amount of guesses
    guess_number = ""
    guess_num = open('guesses.txt', 'r')
    guesses = guess_num.readlines()
    for guess in guesses:
        guess_count = guess
        amt_guesses = len(guess_count)
        guess_number = guess_number + str(amt_guesses)
         

    # save player name and amount of guesses to a file with winner data
    with open('winners.txt', mode = 'a') as winner_info:

            winner_info.write(str(guess_number))
            winner_info.write(":")
            winner_info.write(str(player_name[0]))
            winner_info.write("\n")

def clear_scores():
    '''
    name: clear_scores
    parameters: none
    function: clears scores in files 'guesses.txt', 'matches.txt', 'card_count.txt'
    when win the game, so next time opened, it has clear files for new game.
    '''
    with open('guesses.txt', mode = 'w') as guesses:
            guesses.write('')
    with open('matches.txt', mode = 'w') as matches:
            matches.write('')
    with open('card_count.txt', mode = 'w') as card_count:
            card_count.write('')

            
    
def main():

    # 1. creates initial title on screen
    turtle.title("CS 5001: Memory Matching Game")

    # 2. asks user info and saves (name and number of cards) in player_info variable
    player_info = welcome_user()
    

    # 3. if player_info is not 0 (player does not click cancel in welcome_user), it makes game board outline

    if player_info != 0:
        create_board()

        # player_name and cards_number saved in global variables for all functions to use
        player_name.append(player_info[0])
        cards_number.append(int(player_info[1]))
       
        
        # 4. stop image is added to game
        add_stop()

        # 5. leaderboard is added and sorted
        add_leaderboard()


        # 6. status board is created
        add_statusboard()


        # 7. cards are created face-down 
        add_cards()


        # 8. use screen clicks and send to function flip
        screen = turtle.Screen()
        screen.onclick(flip)



main()
