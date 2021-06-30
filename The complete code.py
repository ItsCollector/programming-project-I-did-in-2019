def menu():
    open("accounts.txt","a").close() # creates files if it doesn't exist
    open("leaderboard.txt","a").close()
    print("""
********** Menu **********

A - Make an account

B - Sign in

C - Leaderboard
""")
    choice = input(str("Please select an option: ")).lower().strip()

    if choice == "a":
        print("Account creation selected.")
        account()
    elif choice == "b":
        print("Sign in selected.")
        sign_in()
    elif choice == "c":
        print("Leaderboard selected.")
        view_leaderboard()
    else:
        print("Invalid choice.")
        menu()

def account(): # creates and adds usernames and passwords to file
    username = input(str("Choose a username: "))
    password = input(str("Choose a password: "))
    file = open("accounts.txt","a")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    print("Account saved.")
    menu()

def sign_in():
    global user1
    global user2
    counter1 = 0 # sets up counters for failure tracking
    counter2 = 0
    access = False # sets up while loop requirements
    final_list = []
    with open("accounts.txt","r") as my_file:
        first_list = my_file.readlines() # puts usernames and passwords in array,
        # they are separated based on the fact that \n is still in the string
        for i in first_list: # iterates through the first list and removes \n from any lines, the new list is saved on the next line
            final_list.append(i.strip())
    while counter1 != 3 and counter2 != 3 and access == False:
        user1 = input(str("Enter first username: "))
        pass1 = input(str("Enter password: "))
        user2 = input(str("Enter Second username: "))
        pass2 = input(str("Enter password: "))
        userpass1 = user1 + " " + pass1
        userpass2 = user2 + " " + pass2
        if userpass1 not in final_list or userpass2 not in final_list:
            print("-------------------------------")
            print("Incorrect Credenitals.")
            print("-------------------------------")
            if userpass1 not in final_list and userpass2 not in final_list:
                print("USER 1 - Access Denied")
                print("USER 2 - Access Denied")
                counter1 = counter1 + 1
                counter2 = counter2 + 1
                print("USER 1 -",counter1,"failed attempts")
                print("USER 2 -",counter2,"failed attempts")
                print("")
            if userpass1 not in final_list and userpass2 in final_list:
                print("USER 1 - Access Denied")
                counter1 = counter1 + 1
                print("USER 1 -",counter1,"failed attempts")
                print("USER 2 -",counter2,"failed attempts")
                print("")
            if userpass1 in final_list and userpass2 not in final_list:
                print("USER 2 - Access Denied")
                counter2 = counter2 + 1
                print("USER 1 -",counter1,"failed attempts")
                print("USER 2 -",counter2,"failed attempts")
                print("")
        if userpass1 in final_list and userpass2 in final_list:
            print("Correct Credentials.")
            print("USER 1 - Access Granted")
            print("USER 2 - Access Granted")
            access = True
            game()
    if counter1 == 3 and counter2 == 3 and access == False:
        print("USER with 3 failed attempts - please create an account.")
        menu()
    
import random
def game():
    print("Game loading")
    input("Press ENTER to continue")
    dice1 = 0
    dice2 = 0
    player1_score = 0
    player2_score = 0
    for count in range(1,6):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        total_dice = dice1 + dice2
        print("--------------------------------------------")
        print("Round",[count])
        print(user1,"rolled:")
        print(dice1)
        print(dice2)
        print("Dice total:",total_dice)
        print("")
        input("Press ENTER to continue")
        if total_dice % 2 == 0:
            player1_score = player1_score + total_dice
            player1_score = player1_score + 10
            print("")
            print("Even total: +10")
            print(user1,"score:",player1_score)
            print("")
            input("Press ENTER to continue")
        else:
            player1_score = player1_score + total_dice
            player1_score = player1_score - 5
            print("")
            print("Odd total: -5")
            if player1_score < 0:
                player1_score = 0
                print(user1,"score:",player1_score)
                print("")
                input("Press ENTER to continue")
            else:
                print("")
                print(user1,"score:",player1_score)
                print("")
                input("Press ENTER to continue")
        if dice1 == dice2:
            dice1 = random.randint(1,6)
            player1_score = player1_score + dice1
            print("")
            print("Double!")
            print("Extra roll is",dice1)
            print(user1,"score:",player1_score)
            print("")
            input("Press ENTER to continue")
        dice1 = 0
        dice2 = 0

    for count in range(1,6):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        total_dice = dice1 + dice2
        print("--------------------------------------------")
        print("Round",[count])
        print(user2,"rolled:")
        print(dice1)
        print(dice2)
        print("Dice total:",total_dice)
        print("")
        input("Press ENTER to continue")
        if total_dice % 2 == 0:
            player2_score = player2_score + total_dice + 10
            print("")
            print("Even total: +10")
            print(user2,"score:",player2_score)
            print("")
            input("Press ENTER to continue")
        else:
            player2_score = player2_score + total_dice - 5
            if player2_score < 0:
                player2_score = 0
                print("")
                print(user2,"score:",player2_score)
                print("")
                input("Press ENTER to continue")
            else:
                print("")
                print(user2,"score:",player2_score)
                print("")
                input("Press ENTER to continue")
        if dice1 == dice2:
            dice1 = random.randint(1,6)
            player2_score = player2_score + dice1
            print("")
            print("Double!")
            print("Extra roll is",dice1)
            print(user2,"score:",player2_score)
            print("")
            input("Press ENTER to continue")
        dice1 = 0
        dice2 = 0

    print("--------------------------------------------")
    if player1_score > player2_score:
        print(user1,"has won with a score of",player1_score)
        print(user2,"has",player2_score)
        input("Press ENTER to continue")
    elif player1_score < player2_score:
        print(user2,"has won with a score of",player2_score)
        print(user1,"has",player1_score)
        input("Press ENTER to continue")
    else:
        print("Draw!")
        print("Final roll!")
        input("Press ENTER to continue")
        finished = False
        while finished == False:
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            print(user1,"rolled",dice1)
            print(user2,"rolled",dice2)
            input("Press ENTER to continue")
            if dice1 > dice2:
                print(user1,"has won")
                finished = True
            elif dice1 < dice2:
                print(user2,"has won")
                finished = True
            else:
                print("Draw")
    player1_score = str(player1_score)
    player2_score = str(player2_score)
    file = open("leaderboard.txt","a")
    data1 = player1_score + " - " + user1
    data2 = player2_score + " - " + user2
    with open("leaderboard.txt","a") as file:
        file.write(data1)
        file.write("\n")
        file.write(data2)
        file.write("\n")
        file.close()
        menu()

def view_leaderboard():
    final_list = ["","","","",""]
    with open("leaderboard.txt","r") as file:
        first_list = file.readlines() 
        for i in first_list: 
            final_list.append(i.strip())
        final_list.sort()
        final_list.reverse()
        print("Leader board")
        print("-------------")
        for count in range(0,5):
            a = count + 1
            print(a,".",final_list[count])
    menu()
    
menu()
