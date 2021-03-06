# Battleship IV. (four tiles big :)
# This while statement let's the game run forever.
# At the end of each game You have the option to change the variable "play", which results in breaking the while loop and finishing the game.
play ="y"
while play =='y':
    import random
    import time
    print "Welcome to.."
    time.sleep(1)
    print '''
        
        ,-----.            ,--.    ,--.  ,--.              ,--.     ,--.           ,--.,--.   ,--.  
        |  |) /_  ,--,--.,-'  '-.,-'  '-.|  | ,---.  ,---. |  ,---. `--' ,---.     |  | \  `.'  /   
        |  .-.  \' ,-.  |'-.  .-''-.  .-'|  || .-. :(  .-' |  .-.  |,--.| .-. |    |  |  \     /    
        |  '--' /\ '-'  |  |  |    |  |  |  |\   --..-'  `)|  | |  ||  || '-' '    |  |   \   /.--. 
        `------'  `--`--'  `--'    `--'  `--' `----'`----' `--' `--'`--'|  |-'     `--'    `-' '--' 
                                                                        `--'
        '''                                                        
    print
    # this is the multiplayer part option of the game
    # first i created a variable multi (it's value can be whatever except 1 or 2)
    # then i ask for users input to change this variable to 1 or two
    # while loop will only break if you enter the number in the list multi
    multi ="a"
    mp=['1','2','3']
    while multi not in mp:
        multi = raw_input("SINGLE (1) - 2 PLAYERS (2) - AI (3) ")
    multi = int(multi)
    print   
    if multi == 2:
        player1 = raw_input('Player 1, please enter your name: ')
        print
        player2 = raw_input('Player 2, please enter your name: ')
        print

    # similar situation as with the multiplayer option, we change the variable "difficulty" to 1,2 or 3
    difficulty ='a'
    dif=['1','2','3']

    while  difficulty not in dif: 
        difficulty = raw_input('Choose your difficulty level 1-3 :')

    # converting difficulty into a integer value, so we can perform comparison
    difficulty =int(difficulty)
    print

    # here we define a function diff, that takes in as input the difficulty we have chosen
    # and returns the number of rows that should be used for that difficulty level.
    def diff(difficulty):
        if difficulty == 1:
            return 5
        elif difficulty == 2:
            return 8
        elif difficulty == 3:
            return 30

    # here we assign the variable skill the result of our diff function
    skill = diff(difficulty)

    # Building the board
    board = []

    # here we create the list that we will use as the upper list that numbers each column (1  2  3  4 ...)
    upper_list =[]
    for a in range(1,skill+1):
        upper_list.append(a)

    # the board will be modeled accoring to the difficulty/skill we have chosen
    for x in range(0,skill):
      board.append(["~ "] * skill)

    # if the number in the upper list gets 10 or higher, they use more space, so we only add one space between the numbers if they are 10+, otherwise we add 2 spaces. 
    def print_board(board):
        nl=''
        for i in upper_list:
            if i<10:
                nl = nl+str(i)+'  '
            else:nl = nl+str(i)+' '
        print '  ',nl
        #here we print the rows
        #basically after each list printed, we also print the row number
        p=0
        for row in board:
            p=p+1
            if p<10:
                print p,''," ".join(row),p
            else:
                print p," ".join(row),p
            
        print '  ',nl
    
    print_board(board)
    # Hiding the first part of the ship
    def random_row(board):
      return random.randint(1,len(board))

    def random_col(board):
      return random.randint(1,len(board[0]))

    ship_row = random_row(board)
    ship_col_1 = random_col(board)

    # Creating the other parts of the ship, checking if they are next to each other and making sure that they stay on the board.

    def second_part(board):
        if ship_col_1 == len(board):
            return ship_col_1 - 1
        if ship_col_1 == 1:
            return ship_col_1 + 1
        else:
            return ship_col_1 + 1

    ship_col_2 = second_part(board)

    def third_part(board):
        if (ship_col_2 == len(board) or ship_col_1 == len(board)) and \
           (ship_col_2 == len(board)-1 or ship_col_1 == len(board)-1):
            return len(board)-2
        elif ship_col_1 == 1:
                return ship_col_1 +2
        elif (ship_col_2 == 0 or ship_col_1 == 0) and \
             (ship_col_2 == len(board)-1 or ship_col_1 == len(board)-1):
            return ship_col_2 -2
        else: return  ship_col_2 +1   

    ship_col_3 = third_part(board)

    def fourth_r(board):
        if ship_row == 1:
            return 2
        else:
            return ship_row-1

    def fourth_c(board):
        return max(ship_col_1,ship_col_2,ship_col_3) # picking the highest value 

    ship_row_2 = fourth_r(board)+1
    fourth_col = fourth_c(board)+1


    def titanic(board):
        return random.randint(1,len(board))

    titanic_r1 = titanic(board)

    ship_row_2 = fourth_r(board)
    fourth_col = fourth_c(board)

    def titanic_col_1(board):
        d=50
        while d==50 or (d==ship_col_1 and ship_row==titanic_r1 or \
                       d==ship_col_2 and ship_row==titanic_r1 or \
                       d==ship_col_3 and ship_row==titanic_r1 or \
                       d==fourth_col and ship_row_2==titanic_r1) or \
                       d==len(board) and (ship_col_1 == len(board)-1 or \
                       ship_col_2 == len(board)-1 or ship_col_3 == len(board)-1 or \
                       fourth_col == len(board)-1) or \
                       d == 1 and (ship_col_1 == 2 or ship_col_2 == 2 or ship_col_3 == 2):
            d = random.randint(1,len(board))
        return d

    titanic_c1 = titanic_col_1(board)

    def titanic_col_2(board):
        if titanic_c1 ==len(board):
            return titanic_c1-1
        elif titanic_c1 == 1:
            return  titanic_c1+1
        elif titanic_c1+1 == ship_col_1 or\
             titanic_c1+1 == ship_col_2 or\
             titanic_c1+1 == ship_col_3 or\
             titanic_c1+1 == fourth_col:
            return titanic_c1-1
        else:
            return titanic_c1+1

    titanic_c2 = titanic_col_2(board)
    tries = 6  # "tries" will track how many turns you have left
    if multi ==1 and difficulty==1:
        tries = 6
    if multi ==1 and difficulty==2:
        tries = 8
    if multi ==1 and difficulty==3:
        tries = 10        
    if multi ==2 and difficulty==1:
        tries = 6
    if multi ==2 and difficulty==2:
        tries = 10
    if multi ==2 and difficulty==3:
        tries = 12        
    if multi ==3 and difficulty==1:
        tries = 6
    if multi ==3 and difficulty==2:
        tries = 10
    if multi ==3 and difficulty==3:
        tries = 12        

    print len(board)
    print 
    print 'ship_row',ship_row
    print 'ship_col_1',ship_col_1
    print 'ship_col_2',ship_col_2
    print 'ship_row_2',ship_row_2
    print 'titanic_r1',titanic_r1
    print 'titanic_c1',titanic_c1
    print 'titanic_c2',titanic_c2
    print 'ship_col_3',ship_col_3

    while tries > 0:

      # these two ifs only execute if we have chosen the multiplayer option
      # player1 plays when the "tries" are a even number, otherwise it's player2 turn
      if tries%2 == 0 and multi ==2:
          print "It's Your turn",player1
          print
      if tries%2 != 0 and multi==2:
          print "It's Your turn",player2
          print
      if tries%2 == 0 and multi ==3:
          print "It's Your turn human.."
          print
      if tries%2 != 0 and multi ==3:
          print "AI's move.."
          print             
      if tries%2 == 0 and multi ==2:
          guess_row = raw_input("Guess Row:")
          guess_col = raw_input("Guess Col:")

      if tries%2 != 0 and multi ==2:
          guess_row = raw_input("Guess Row:")
          guess_col = raw_input("Guess Col:")

      if  multi == 1:
          guess_row = raw_input("Guess Row:")
          guess_col = raw_input("Guess Col:")

      if tries%2 == 0 and multi ==3:
          guess_row = raw_input("Guess Row:")
          guess_col = raw_input("Guess Col:")

      if tries%2 != 0 and multi ==3:
          guess_row = random.randint(0,len(board)-1)
          guess_col = random.randint(0,len(board)-1)
          while board[guess_row][guess_col] == "X " or board[guess_row][guess_col] == "@ ":
              guess_row = random.randint(0,len(board)-1)
              guess_col = random.randint(0,len(board)-1)
          guess_row = str(guess_row)
          guess_col = str(guess_col)

      if guess_row.isdigit() == False or guess_col.isdigit() == False:     # accepting only numeral entries. .isdigit() returns a True if a string contains a integer
          print 'Misfire ey?'

      elif (int(guess_row)-1 == ship_row-1 and int(guess_col)-1 == ship_col_1-1)or \
           (int(guess_row)-1 == ship_row-1 and int(guess_col)-1 == ship_col_2-1)or \
           (int(guess_row)-1 == ship_row-1 and int(guess_col)-1 == ship_col_3-1)or \
           (int(guess_row)-1 == ship_row_2-1 and int(guess_col)-1 == fourth_col-1)or \
           (int(guess_row)-1 == titanic_r1-1 and int(guess_col)-1 == titanic_c1-1) or\
           (int(guess_row)-1 == titanic_r1-1 and int(guess_col)-1 == titanic_c2-1):     #  if either of the parts of the ship is hit, you won
        if (tries%2==0 or tries%2!=0) and multi ==1:
            print "Congratulations, You sunk my battleship!!"
            print
        elif tries%2==0 and multi ==2:
            print "Congratulations "+player1+"! You sunk my battleship!!"
            print
        elif tries%2!=0 and multi ==2:
            print "Congratulations "+player2+"! You sunk my battleship!!"
            print
        elif tries%2==0 and multi==3:
            print "Congratulations human, You sunk my battleship!!"
            print
        elif tries%2!=0  and multi==3:
            print "AI owns this game!!"
            print

        guess_row = int(guess_row)-1
        guess_col = int(guess_col)-1
        # printing the ship in case of victory
        board[ship_row-1][ship_col_1-1] = "O "
        board[ship_row-1][ship_col_2-1] = "O "
        board[ship_row-1][ship_col_3-1] = "O "
        board[ship_row_2-1][fourth_col-1] = "O "
        board[titanic_r1-1][titanic_c1-1] = "o "
        board[titanic_r1-1][titanic_c2-1] = "o "
        board[guess_row][guess_col]='* '   # the part of the ship you hit, will be displayed with a *
        print_board(board)
        break
      else:
        guess_row = int(guess_row)-1
        guess_col = int(guess_col)-1
        if guess_row < 0 or guess_row > len(board)-1 or guess_col < 0 or guess_col > len(board)-1:
          print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X ") or(board[guess_row][guess_col] == "@ "):
          print "You guessed that one already."          
        else:
          print "You missed my battleship!"
          if tries%2!=0  and multi==3: 
              board[guess_row][guess_col] = "@ "
          if tries%2==0  and multi==3:
              board[guess_row][guess_col] = "X "
          if tries%2!=0  and multi==2:
              board[guess_row][guess_col] = "X "
          if tries%2==0  and multi==3:
              board[guess_row][guess_col] = "X "
          if tries%2!=0  and multi==2:
              board[guess_row][guess_col] = "X "
          if tries%2==0  and multi==2:
              board[guess_row][guess_col] = "X "              
          if tries%2==0  and multi==1:
              board[guess_row][guess_col] = "X "
          if tries%2!=0  and multi==1:
              board[guess_row][guess_col] = "X "
          
          tries = tries - 1
          if tries>0:
              print 'You have',tries/2,'more left!'
          if  tries < 1:
              # printing the position of the ship, in case you loose
              board[ship_row-1][ship_col_1-1] = "O "
              board[ship_row-1][ship_col_2-1] = "O "
              board[ship_row-1][ship_col_3-1] = "O "
              board[ship_row_2-1][fourth_col-1] = "O "
              board[titanic_r1-1][titanic_c1-1] = "o "
              board[titanic_r1-1][titanic_c2-1] = "o "
              print_board(board)
              print
              print '-----------------'
              print "-= Game Over!! =-"
              print '-----------------'
              print
              break
          print_board(board)
    # here we can choose to continue, or finishing the game by breaking the loop, with anything else then a 'y'  
    play = raw_input('Do you want to play again? press "y" for yes: ')

print "Thank You for playing Battleships IV !!"
