import itertools
import random
import secrets
import os
import time 

#initialising variables 
playerList = [] # each player i.e. [1,2,3,4]
total = [0,0,0,0] # create a list to record every players' score
deck = list(itertools.product(range(10),['C','S','T','H']))
lst = ([i for i in deck])


#List1 = [] # define each player's list to store his most recent cards
#List2 = []
#List3 = []
#List4 = []


#playerList: [1, 2, 3, 4]
#total: a list of every player's score (print after every player or every round)

# putDownList = [] #the list of cards the player decides to put in the pool
score = 0 # individual score of current player
player = 0 # current player

def rules(): # print rules
    print()
    str1 = "Please play at full screen and read the instructions carefully."
    print(str1.center(130, "*"))
    print()
    print("1. This is a 4-player game. In the first round, you each will be given 4 cards to start with. \n   Starting from the second round, you have to keep finding sequences of 3, 4 or 5 numbers in your deck of cards.\n")
    print("2. There are 4 shapes: Circle, Square, Triangle and Heart. Our card deck is made up of cards numbered from 0 to 9 in each of the mentioned shapes. \n   In this game, only the numerical value of your card matters. The entire deck of cards will be printed when you start a new game.\n")
    print("3. Once the cards are distributed to you, if you cannot find any numerical sequence, pick up a card from home. \n   An example would be something like 1 2 3 or 8 7 9. \n")
    print("4. In order to put down your cards, only type the numerical value of the intended cards i.e. 1 2 3, separated by a space.\n")
    print("5. If you find a sequence of 3 in your cards, put them down in the pool and earn 3 coins. \n   A sequence of 4 gets you 6 coins and a holy sequence of 5 will get you 15 coins.\n")
    print("6. You can choose to withhold your sequence for a longer one, or you can put them in the pool immediately. \n   Note that having a total of 10 cards will cost you your place in the game.\n")
    print("7. If any one player ends up having 10 cards and still no sequence, you will be discardified and the game must start again.\n")
    print("8. The player with the most coins wins the game.\n")
    print("9. In case of the same number of coins, the player with the least number of cards wins.\n")
    print("Let's start in 3 ... 2 ... 1 ...\n")
    time.sleep(3)

def startGame():
    global List1, List2, List3, List4
    List1 = [] # define each player's list to store his most recent cards
    List2 = []
    List3 = []
    List4 = []
    global n
    global playerList
    str2 = " >_< ---Welcome to Discardified--- >_< "
    print(str2.center(130, "-")) # welcome
    while True: #this function keeps the game running
        starter = input("For rules: please press R. To start the game please press P.\n\n" + "Your answer: ")
        if starter == "R":
            rules()
        elif starter == "P":
            n = 4
            localEnd = False 
            while localEnd == False:
                if (type(n) == int) and n == 4:
                    for i in range(1, n+1):
                        playerList.append(i) # create a player list
                    localEnd = True
                    break
                else:
                    print("\nInvalid input! Please enter again.")
                    time.sleep(1)
                    n = 4
            if localEnd == True:
                break
        else:
            print("Invalid input! Please enter again.")
            time.sleep(1)

def playerList1(cardlist):
    global List1
    List1 = cardlist
    return List1

def playerList2(cardlist):
    global List2
    List2 = cardlist
    return List2

def playerList3(cardlist):
    global List3
    List3 = cardlist
    return List3

def playerList4(cardlist):
    global List4
    List4 = cardlist
    return List4

def firstRound(player): #distribute 4 cards for the first round
    global playerList
    secrets.choice(lst)
    print(*lst, "\n")
    i = 0 #counter for playerList
    while i < n: 
        a,b,c,d = random.sample(lst,4) 
        lstForFour = [a, b, c, d] # four cards
        if playerList[i] == 1:
            List1.extend(lstForFour)
            print("Player 1: Your cards:\n")
            print(List1)
            print("\nPress Enter to hide your cards.")
            cleanScreen()
            print("Please pass your device to Player 2. \nPlayer 2 please press Enter.")
            cleanScreen()
        elif playerList[i] == 2:
            List2.extend(lstForFour)
            print("Player 2: Your cards:\n")
            print(List2)
            print("\nPress Enter to hide your cards.")
            cleanScreen()
            print("Please pass your device to Player 3. \nPlayer 3 please press Enter.")
            cleanScreen()
        elif playerList[i] == 3:
            List3.extend(lstForFour)
            print("Player 3: Your cards:\n")
            print(List3)
            print("\nPress Enter to hide your cards.")
            cleanScreen()
            print("Please pass your device to Player 4. \nPlayer 4 please press Enter.")
            cleanScreen()
        elif playerList[i] == 4:
            List4.extend(lstForFour)
            print("Player 4: Your cards:\n")
            print(List4)
            print("\nPress Enter to hide your cards.")
            cleanScreen()
            print("Please pass your device to Player 1. \nPlayer 1 please press Enter.")
            cleanScreen()

        lst.remove(a) #remove the picked cards from big deck of cards so they they cannot be reused
        lst.remove(b)
        lst.remove(c)
        lst.remove(d)
        i += 1

def cleanScreen():
    wait = input("")
    print("Please wait. \n2... 1...")
    #time.sleep(2)
    os.system('clear')
    
def switchPlayer():
    player = playerList[0]
    del(playerList[0])
    playerList.append(player)
    for player in playerList: #playerList stores all the players in the game i.e. P1, P2, P3, P4
        if player == 1:
            break
        elif player == 2:
            break
        elif player == 3:
            break
        elif player == 4:
            break

def sequence(lst, player):
    global List1
    global List2
    global List3
    global List4
    # print(List1, List2, List3, List4) #devug
    score = 0

    if playerList[0] == 1: #if the number of cards 
        cardlist = List1 #cardlist is every player's cards, will change by every player
        # score = total[0]
    if playerList[0] == 2:   ##changed from elif to if to check result
        cardlist = List2
        # score = total[1]
    if playerList[0] == 3:
        cardlist = List3
        # score = total[2]
    if playerList[0] == 4:
        cardlist = List4
        # score = total[3]
    player = playerList[0]
    print("Player",player,"\nIt's Your Turn!")
    newCard = random.choice(lst)
    cardlist.append(newCard)
    cardlist.sort()
    print("The card you picked up is:", newCard)
    print("Your cards:",cardlist)
    print("\nNumber of cards:",len(cardlist))
    if len(cardlist) == 10:
        print("10 cards!")
        wannaplay()

    have = False # have sequence 
    slist = [] # this checks whether there is sequences and removes duplicate numbers when candidate of pool
    if (len(cardlist) > 2) and (len(cardlist) < 10):
        for i in range(len(cardlist)):
            slist.append(cardlist[i][0])

        for j in range(len(slist)-1,-1, -1):
            if slist[j] == slist[j-1]:
                del(slist[j]) #remove duplicate
                    
        for i in range(len(slist)-2):
            if slist[i]+2 == slist[i+1]+1 == slist[i+2]:
                have = True
                break

    if have == False:
        print("You don't have a sequence!")
        # print("\nYour score is:", score)
    elif have == True:
        print("You have a sequence.")

    while have == True:
        move = input("Score or Hold (S/H): ")
        if move == "S":
            localEnd = False
            # 1. need to check for integer before using int()
            # 2. only input one num is still correct
            while True: # keep running until inpu become valid
                q = input("Put down: ") # q is the input of cards from player
                qlist = [num for num in q.split()] # changing the input to a list so that we can read each element separately
                for num in qlist: # check if num is decimal or not first
                    if num.isdecimal() == False:
                        print("Invalid input. Please put down again.")
                        localEnd = True
                if localEnd: # run within the input q parameter
                    continue # if localEnd == True, continue to the top part of while loop (input q)

                # localEnd *= (num in slist)
                qlist = [int(num) for num in q.split()]
                if len(qlist) == 3: # check if qlist is a sequence of 3
                    if qlist[0]+2 == qlist[1]+1 == qlist[2]: 
                        score = 3
                        # addScore(n, score)
                        # score += 3 
                        # print("\nYour score is:",score)
                        break
                    else:
                        print("You put down the wrong card! Please put down again.")
                        continue # continue to the top part of while loop (input q)

                elif len(qlist) == 4: # check if qlist is a sequence of 4
                    if qlist[0]+3 == qlist[1]+2 == qlist[2]+1 == qlist[3]:
                        score = 5
                        # addScore(n, score)
                        # score += 5
                        # print("\nYour score is",score)
                        break
                    else:
                        print("You put down the wrong card! Please put down again.")
                        continue # continue to the top part of while loop (input q)
        
                elif len(qlist) == 5: # check if qlist is a sequence of 5
                    if qlist[0]+5 == qlist[1]+4 == qlist[2]+3 == qlist[3]+2 == qlist[4]+1 == qlist[5]:
                        score = 8
                        # addScore(n, score)
                        # score += 8
                        # print("\nYour score is",score)
                        break
                    else:
                        print("You put down the wrong card! Please put down again.")
                        continue # continue to the top part of while loop (input q)
                else: # all decimal inputs but don't meet all conditions
                    print("You put down the wrong card! Please put down again")
                    continue # continue to the top part of while loop (input q)

            for i in qlist:
                for j in range(len(cardlist)-1,-1,-1):
                    if i == cardlist[j][0]:
                        cardlist.remove(cardlist[j])
                        break # break for loop (j) since only remove one card if duplicate cardlist exist
            print("Your remaining cards:",cardlist)
            print("Number of cards:",len(cardlist))
            break # break "while have == True"

        elif move == "H":
            break

    if playerList[0] == 1:
        List1 = cardlist
    if playerList[0] == 2:
        List2 = cardlist
    if playerList[0] == 3:
        List3 = cardlist
    if playerList[0] == 4:
        List4 = cardlist
    addScore(n,score)
    print("Please press Enter to finish your round.")
    cleanScreen()
    if player == 4:
        print("Please pass your device to Player 1. \nPlayer 1 please press Enter.")
    else:
        print("Please pass your device to Player", playerList[1], ".\nPlayer", playerList[1], "please press Enter.")
    cleanScreen()
    switchPlayer()

    # return score, cardlist

def addScore(n, score):
    global playerList # calling the global playerList so that it can be changed through this function
    #global score
    if playerList[0] == 1:
        total[0] += score
        print("Your score is:", total[0])
    elif playerList[0] == 2:
        total[1] += score
        print("Your score is:", total[1])
    elif playerList[0] == 3:
        total[2] += score
        print("Your score is:", total[2])
    elif playerList[0] == 4: 
        total[3] += score
        print("Your score is:", total[3])
    print("\nThis is the end of your turn! Next player please.")
    tot = "The score right now is:"
    print(tot, *total)


def playerRun():
    global n
    global score
    # global end
    # global put_down_list
    global playerList
    localEnd = False
    while localEnd == False:
        for i in range(1): #len(playerList)): ##added 1 as counting starts from 0
            sequence(lst, player)
            for i in range(len(playerList)): # adjust cardlist and add score
                if playerList[i] == 1:
                    playerList1(List1)
                elif playerList[i] == 2:
                    playerList2(List2)
                elif playerList[i] == 3:
                    playerList3(List3)
                elif playerList[i] == 4:
                    playerList4(List4)

        if max(total) >= n*4:
            localEnd = True
            break
        elif (len(List1) >= 10) or (len(List2) >= 10) or (len(List3) >= 10) or (len(List4) >= 10):
            localEnd = True
            break
        
                    
def winner(total, List1, List2, List3, List4): # put total score of all players into one list called total
    global n #call number of players 
    draw = False
    # end = False
    while n == 4:
        if total[0] >= n*4 and total[0] > total[1] and total[0] > total[2] and total[0] > total[3]:
            # end = True
            print(f"Congratulations to {p1}!")
            print("Thank you for playing!!")
            break
        if total[1] >= n*4 and total[1] > total[0] and total[1] > total[2] and total[1] > total[3]:
            # end = True
            print(f"Congratulations to {p2}!")
            print("Thank you for playing!!")
            break
        if total[2] >= n*4 and total[2] > total[0] and total[2] > total[1] and total[2] > total[3]:
            # end = True
            print(f"Congratulations to {p3}!")
            print("Thank you for playing!!")
            break
        if total[3] >= n*4 and total[3] > total[0] and total[3] > total[1] and total[3] > total[2]:
            # end = True
            print(f"Congratulaions to {p4}!")
            print("Thank you for playing!!")
            break
        if total[0] == total[1] == total[2] == total[3] >= n*4:
            # end = True
            if len(List1) < len(List2) and len(List1) < len(List3) and len(List1) < len(List4):
                print(f"Congratulations to {p1}!")
                print("Thank you for playing!!")
                break
            if len(List2) < len(List1) and len(List2) < len(List3) and len(List2) < len(List4):
                print(f"Congratulations to {p2}!")
                print("Thank you for playing!!")
                break
            if len(List3) < len(List1) and len(List3) < len(List2) and len(List3) < len(List4):
                print(f"Congratulations to {p3}!")
                print("Thank you for playing!!")
                break
            if len(List4) < len(List1) and len(List4) < len(List2) and len(List4) < len(List3):
                print(f"Congratulations to {p4}")
                print("Thank you for playing!!")
                break
            else:
                draw() # 
        if total[0] == total[1] >= n*4 and total[0] > total[2] and total[0] > total[3]:
            if len(List1) < len(List2):
                # end = True
                print(f"Congratulations to {p1}!")
                print("Thank you for playing!!")
                break
            if len(List2) < len(List1):
                # end = True
                print(f"Congratulations to {p2}!")
                print("Thank you for playing!!")
                break
            else:
                draw()
        if total[0] == total[2] >= n*4 and total[0] > total[1] and total[0] > total[3]:
            if len(List1) < len(List3):
                # end = True
                print(f"Congratulations to {p1}!")
                print("Thank you for playing!!")
                break
            if len(List3) < len(List1):
                # end = True
                print(f"Congratulations to {p3}!")
                print("Thank you for playing!!")
                break
        if total[0] == total[3] >= n*4 and total[0] > total[1] and total[0] > total[2]:
            if len(List1) < len(List4):
                # end = True
                print(f"Congratulations to {p1}!")
                print("Thank you for playing!!")
                break
            if len(List4) < len(List1):
                # end = True
                print(f"Congratulations to {p4}!")
                print("Thank you for playing!!")
                break
        if total[1] == total[2] >= n*4 and total[1] > total[0] and total[1] > total[3]:
            if len(List2) < len(List3):
                # end = True
                print(f"Congratulations to {p2}!")
                print("Thank you for playing!!")
                break
            if len(List3) < len(List2):
                # end = True
                print(f"Congratulations to {p3}!")
                print("Thank you for playing!!")
                break
        if total[1] == total[3] >= n*4 and total[1] > total[0] and total[1] > total[2]:
            if len(List2) < len(List4):
                # end = True
                print(f"Congratulations to {p2}!")
                print("Thank you for playing!!")
                break
            if len(List4) < len(List2):
                # end = True
                print(f"Congratulations to {p4}!")
                print("Thank you for playing!!")
                break
        if total[2] == total[3] >= n*4 and total[2] > total[0] and total[2] > total[1]:
            if len(List3) < len(List4):
                # end = True
                print(f"Congratulations to {p3}!")
                print("Thank you for playing!!")
                break
            if len(List4) < len(List3):
                # end = True
                print(f"Congratulations to {p4}!")
                print("Thank you for playing!!")
                break
        if total[0] == total[1] == total[2] >= n*4 and total[3] < n*4:
            if len(List1) < len(List2) and len(List1) < len(List3):
                # end = True
                print(f"Congratulations to {p1}!")
                print("Thank you for playing!!")
                break
            if len(List2) < len(List1) and len(List2) < len(List3):
                # end = True
                print(f"Congratulations to {p2}!")
                print("Thank you for playing!!")
                break
            if len(List3) < len(List1) and len(List3) < len(List2):
                # end = True
                print(f"Congratulations to {p3}!")
                print("Thank you for playing!!")
                break
        if total[0] == total[1] == total[3] >= n*4 and total[2] < n*4:
            if len(List1) < len(List2) and len(List1) < len(List4):
                # end = True
                print(f"Congratulations to {p1}!")
                print("Thank you for playing!!")
                break
            if len(List2) < len(List1) and len(List2) < len(List4):
                # end = True
                print(f"Congratulations to {p2}!")
                print("Thank you for playing!!")
                break
            if len(List4) < len(List1) and len(List4) < len(List2):
                # end = True
                print(f"Congratulations to {p4}!")
                print("Thank you for playing!!")
                break
        if total[0] == total[2] == total[3] >= n*4 and total[1] < n*4:
            if len(List1) < len(List3) and len(List1) < len(List4):
                # end = True
                print(f"Congratulations to {p1}!")
                print("Thank you for playing!!")
                break
            if len(List3) < len(List1) and len(List3) < len(List4):
                # end = True
                print(f"Congratulations to {p3}!")
                print("Thank you for playing!!")
                break
            if len(List4) < len(List1) and len(List4) < len(List3):
                # end = True
                print(f"Congratulations to {p4}!")
                print("Thank you for playing!!")
                break
        if total[1] == total[2] == total[3] >= n*4 and total[0] < n*4:
            if len(List2) < len(List3) and len(List2) < len(List4):
                # end = True
                print(f"Congratulations to {p2}!")
                print("Thank you for playing!!")
                break
            if len(List3) < len(List2) and len(List3) < len(List4):
                # end = True
                print(f"Congratulations to {p3}!")
                print("Thank you for playing!!")
                break
            if len(List4) < len(List2) and len(List4) < len(List3):
                # end = True
                print(f"Congratulations to {p4}!")
                print("Thank you for playing!!")
                break

        else:
            draw == True
        break
    return draw


def printHeart():
    n = 14
    m = n+1

    for i in range(n//2-1): # looping for upper heart
        for j in range(m):
            if i == n//2-2 and (j == 0 or j == m-1):
                print("*", end=" ")
            elif j <= m//2 and ((i+j == n//2-3 and j <= m//4) \
                            or (j-i == m//2-n//2+3 and j > m//4)):
                print("*", end=" ")
            elif j > m//2 and ((i+j == n//2-3+m//2 and j < 3*m//4) \
                           or (j-i == m//2-n//2+3+m//2 and j >= 3*m//4)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print("         DISCARDIFIED") #the spacing is to print the string in the middle


    for i in range(n//2-1, n): #looping for lower heart
        for j in range(m):
            if (i-j == n//2-1) or (i+j == n-1+m//2):
                print('*', end=" ")
             
            elif i == n//2-1:
             
                if j == m//2-1 or j == m//2+1:
                    print('', end=" ")
                elif j == m//2:
                    print('', end=" ")
                else:
                    print('', end=" ")

            else:
                print(' ', end=" ")
             
        print()


def wannaplay():
    # global draw
    printHeart()    
    print("\nYou have been disCARDified!")

    draw = winner(total, List1, List2, List3, List4) # find the winner

    while True:
        if draw == True:
            print("No winner!")
        player_more = input("Let's play one more round? (yes or no) ") # then ask whether to play more or not
        if player_more == "yes":
            end = False
            break
        elif player_more == "no":
            print("Thank you for playing!!")
            end = True
            break
        else:
            print("Invalid error. Please input again")
    return end


def main():
    while True: # running to play more or not
        runAgain = False
        startGame()
        ending = False
        while ending == False: # running the game for once
            firstRound(player)
            playerRun()
            print()
            # player = playerList[thisPlayer%n]
            # wannaplay() #prints our heart and returns end value
            if wannaplay() == True:
                ending = True
                break
            elif wannaplay() == False:
                runAgain = True
                break
        if runAgain == True:
            # raise ValueError #debug
            continue # continue running "while ending == False"

        if ending == True:
            print("-End-") #cannot put it inside the nested while loop 
            break
            # draw()
            # global player_more
            # if draw() == True and player_more == "no":
                # break
            # endGame()
main()
