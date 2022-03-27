import random
import time
def print_board(a):
    q = 0
    print("|",end="")
    for i in a:
        q += 1
        print(i,end ="|")
        if q == 3 or q == 6:
            print("\n|",end="")
    print("")
def computer_zeka_movement(player_list,computer_list):
    b = player_list
    if (1 in player_list and 2 in player_list and (0 not in computer_list)) or (4 in player_list and 8 in player_list and (0 not in computer_list)) or (3 in player_list and 6 in player_list and (0 not in computer_list)):
        return 0
    
    if (0 in player_list and 2 in player_list and (1 not in computer_list)) or (4 in player_list and 7 in player_list and (1 not in computer_list)):
        return 1
    
    if (0 in player_list and 1 in player_list and (2 not in computer_list)) or (4 in player_list and 6 in player_list and (2 not in computer_list)) or (5 in player_list and 8 in player_list and (2 not in computer_list)):
        return 2

    if (0 in player_list and 6 in player_list and (3 not in computer_list)) or (4 in player_list and 5 in player_list and (3 not in computer_list)):
        return 3
    
    if (0 in player_list and 8 in player_list and (4 not in computer_list)) or (2 in player_list and 6 in player_list and (4 not in computer_list)) or (3 in player_list and 5 in player_list and (4 not in computer_list)) or (1 in player_list and 7 in player_list and (4 not in computer_list)):
        return 4
    
    if (3 in player_list and 4 in player_list and (5 not in computer_list)) or (2 in player_list and 8 in player_list and (5 not in computer_list)):
        return 5
    
    if (0 in player_list and 3 in player_list and (6 not in computer_list)) or (2 in player_list and 4 in player_list and (6 not in computer_list)) or (7 in player_list and 8 in player_list and (6 not in computer_list)):
        return 6
    
    if (1 in player_list and 4 in player_list and (7 not in computer_list)) or (6 in player_list and 8 in player_list and (7 not in computer_list)):
        return 7
    
    if (0 in player_list and 4 in player_list and (8 not in computer_list)) or (6 in player_list and 7 in player_list and (8 not in computer_list)) or (2 in player_list and 5 in player_list and (8 not in computer_list)):
        return 8

    return 9
def winCheck(liste):
    if (0 in liste and 1 in liste and 2 in liste) or (3 in liste and 4 in liste and 5 in liste) or (6 in liste and 7 in liste and 8 in liste) or (0 in liste and 3 in liste and 6 in liste) or (1 in liste and 4 in liste and 7 in liste) or (2 in liste and 5 in liste and 8 in liste) or (0 in liste and 4 in liste and 8 in liste) or (2 in liste and 4 in liste and 6 in liste):
        return True
    else:
        return False



while True:
    a = [0,1,2,3,4,5,6,7,8]
    b = [" "," "," "," "," "," "," "," "," "]
    player_list = []
    computer_list = []
    print_board(a)
    i = 0
    print("""\t__________
    \tNEW GAME """)
    while True:
        time.sleep(1)
        player_number = int(input("Player: "))
        a.remove(player_number)
        player_list.append(player_number)
        b[player_number] = "X"
        print_board(b)
        print("**********")
        if winCheck(player_list):
            print("Player Wins! ")
            print_board(b)
            break
        time.sleep(1)
        i += 1
        if i == 5:
            print("Draw Game")
            break
        print("p: ",player_list)

        if i == 1 and 4 not in player_list:
            coop = 4
            b[coop] = "O"
        else:
            coop = computer_zeka_movement(computer_list,player_list)
            if coop == 9:
                coop = computer_zeka_movement(player_list,computer_list)
                if coop == 9:
                    coop = random.choice(a)
                if b[coop] != "O" and b[coop] != "X":
                    b[coop] = "O"
                else:
                    coop = random.choice(a)
                    b[coop] = "O"

        print("computer:",coop)
        computer_list.append(coop)
        a.remove(coop)
        print_board(b)
        print("**********")
        print("c: ",computer_list)
        
        if winCheck(computer_list):
            print("Computer Wins")
            b[coop] = "O"
            print_board(b)
            break

















        






        

