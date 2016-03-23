from random import shuffle

#initialize the cards and groups

Jack=10
Queen=10
King=10
Ace=1
group_player=[]
group_computer=[]

#define two decks and card groups for player and computer

Deck_player=[Ace,2,3,4,5,6,7,8,9,10,Jack,Queen,King]*4
Deck_computer=Deck_player[:]

#define the procedure of game

def move_player():
    shuffle(Deck_player)
    new_player = Deck_player.pop()
    group_player.append(new_player)
    total_player = sum(group_player)
    print 'The player get a %s, now the total number of player is %s.' % (str(new_player),str(total_player))
    
def move_computer():
    shuffle(Deck_computer)
    new_computer = Deck_computer.pop()
    group_computer.append(new_computer)
    total_computer = sum(group_computer)
    print 'The computer get a %s, now the total number of computer is %s.' % (str(new_computer),str(total_computer))

def check(signal_p,signal_c):
    total_player = sum(group_player)
    total_computer = sum(group_computer)
    if total_player > 21:
        print 'Player blow off. Computer win!'
    elif total_computer >21:
        print 'Computer blow off. Player win!'
    elif total_player == 21:
        print 'Player just reached 21. Player win!'
    elif total_computer == 21:
        print 'Computer just reached 21. Computer win!'
    elif signal_p == 1 and signal_c ==1:
        if total_player > total_computer:
            print 'Player has bigger number. Player win! You must be very happy!'
        elif total_player < total_computer:
            print 'Computer has bigger number. Computer win! Your computer is proud of itself!'
        else:
            print 'No winner, no loser. What a peaceful world!'
    else:
        return 1


def game():
    signal_p = 0
    signal_c = 0
    while check(signal_p,signal_c) == 1:
        total_computer = sum(group_computer)
        order_p = raw_input('Do you want to pick a new card?(Y or N)')
        if order_p == 'N':
            signal_p = 1
        if order_p == 'Y':
            move_player()
        if total_computer < 18:
            move_computer()
        if total_computer >= 18:
            signal_c = 1
        

# wait user to begin the game
raw_input('Press Enter to begin the game!!!')

game()

raw_input('Press Enter to end the game...')






    


    
        
    






    
    
