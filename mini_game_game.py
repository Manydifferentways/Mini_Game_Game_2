import random
t = 0
p = 0
_= "_"

usernames = ["Many",]
passwords = ["Many",]
ID = [0]
a = usernames[0]
b = passwords[0]
Accounts = ["Many_Many_0"]
while t == 0:
    c = input("Sign up or Login")
    
    #Sign Up
    if c.casefold() == str("sign up"):
        print("signingup")
        a = input('Username:')
        b = input('password:')
        c = input('print password again:')
        if b == c:
            passwords.extend(b)
            usernames.extend(a)
            if b == c:
                p += 1
                print("Your ID is: " + str(p))
            ID.append(p)
            Accounts.insert(p, a + _ + b + _ + str(p))
            print("Signed Up!")
            for row in Accounts:
                print(row)
            continue
    #Login
    elif c.casefold() == str("login"):
        print("login")
        if t == 0:
            I = int(input("ID:"))
        q = input("Username:")
        w = input("Password:")
        if q == usernames[I] and w == passwords[I]:
            print("Welcome")
            while q == usernames[I] and w == passwords[I]:
                print("Which game do you want to play?")
                print("RPS (rock paper scissors)? Dice? or do you want to leave?")
                print("Choose:")
                c = str(input())
                
                #Dice
                if c == str("Dice") or c == str("dice"):
                    print("Roll a D6, D4, D12, D10, D8, D100 or Leave. Choose:")
                        
                    q = str(input())
                        #D20
                    if q == str("Roll D20") or q == str("roll d20") or q == str("roll D20") or q == str("Roll d20") or q == str("d20") or q == str("D20"):
                            #player
                        v = int(random.randint(1,20))
                        print("You rolled " + str(v))
                            #Computer
                        l = int(random.randint(1,20))
                        print("Computer rolled " + str(l))
                            
                        if v < l:
                            print("you lost by " + str(l-v))
                        elif v > l:
                            print("you won by " + str(v-l))
                        elif v == l:
                            print("tie")
                        else:
                            print("error")
                
                        #D6
                    elif q == str("Roll D6") or q == str("roll d6") or q == str("roll D6") or q == str("Roll d6") or q == str("d6") or q == str("D6"):
                            #player
                        v = int(random.randint(1,6))
                        print("You rolled " + str(v))
                            #Computer
                        l = int(random.randint(1,6))
                        print("Computer rolled " + str(l))
                            
                        if v < l:
                            print("you lost by " + str(l-v))
                        elif v > l:
                            print("you won by " + str(v-l))
                        elif v == l:
                            print("tie")
                        else:
                            print("error")
                
                        #D4
                    elif q == str("Roll D4") or q == str("roll d4") or q == str("roll D4") or q == str("Roll d4") or q == str("d4") or q == str("D4"):
                            #player
                        v = int(random.randint(1,4))
                        print("You rolled " + str(v))
                            #Computer
                        l = int(random.randint(1,4))
                        print("Computer rolled " + str(l))
                            
                        if v < l:
                            print("you lost by " + str(l-v))
                        elif v > l:
                            print("you won by " + str(v-l))
                        elif v == l:
                            print("tie")
                        else:
                            print("error")
                
                        #D12
                    elif q == str("Roll D12") or q == str("roll d12") or q == str("roll D12") or q == str("Roll d12") or q == str("d12") or q == str("D12"):
                            #player
                        v = int(random.randint(1,12))
                        print("You rolled " + str(v))
                            #Computer
                        l = int(random.randint(1,12))
                        print("Computer rolled " + str(l))
                            
                        if v < l:
                            print("you lost by " + str(l-v))
                        elif v > l:
                            print("you won by " + str(v-l))
                        elif v == l:
                            print("tie")
                        else:
                            print("error")
                
                        #D10
                    elif q == str("Roll D10") or q == str("roll d10") or q == str("roll D10") or q == str("Roll d10") or q == str("d10") or q == str("D10"):
                            #player
                        v = int(random.randint(1,10))
                        print("You rolled " + str(v * 10) + "%")
                            #Computer
                        l = int(random.randint(1,10))
                        print("Computer rolled " + str(l * 10) + "%")
                            
                        if v < l:
                            print("you lost by " + str((l-v)*10) + "%")
                        elif v > l:
                            print("you won by " + str((v-l)*10) +"%")
                        elif v == l:
                            print("tie")
                        else:
                            print("error")
                
                        #D8
                    elif q == str("Roll D8") or q == str("roll d8") or q == str("roll D8") or q == str("Roll d8") or q == str("d8") or q == str("D8"):
                            #player
                        v = int(random.randint(1,8))
                        print("You rolled " + str(v))
                            #Computer
                        l = int(random.randint(1,8))
                        print("Computer rolled " + str(l))
                            
                        if v < l:
                            print("you lost by " + str(l-v))
                        elif v > l:
                            print("you won by " + str(v-l))
                        elif v == l:
                            print("tie")
                        else:
                            print("error")
                
                        #D100
                    elif q == str("Roll D100") or q == str("roll d100") or q == str("roll D100") or q == str("Roll d100") or q == str("d100") or q == str("D100"):
                            #player
                        v = int(random.randint(1,100))
                        print("You rolled " + str(v))
                            #Computer
                        l = int(random.randint(1,100))
                        print("Computer rolled " + str(l))
                            
                        if v < l:
                            print("you lost by " + str(l-v))
                        elif v > l:
                            print("you won by " + str(v-l))
                        elif v == l:
                            print("tie")
                        else:
                            print("error")
                            break
                        #leave
                    elif q == str("Leave") or  q == str("leave"):
                        print("Leaving...")
                
                
                    #rockpaperscissors
                elif c == str("RPS") or c == str("rps"):
                    rock = str("rock") or str("Rock")
                    paper = str("paper") or str("Paper")
                    scissors = str("scissors") or str("Scissors")
                    print("Choose... rock, paper, or scissors?")
                    v = str(input())
                    
                    if v == rock:
                        v = 1
                    elif v == paper:
                        v = 2
                    elif v == scissors:
                        v = 3
                    elif v == str("Gun") or v == str("gun"):
                        v = 4
                    elif v == str("kill") or v == str("Kill"):
                        print("that is not an option")
                        
                    else:
                        print("error")
                        break
                    l = random.randint(1,4)
                
                    if l == 1:
                        print("computer chose rock")
                    elif l == 2:
                        print("computer chose paper")
                    elif l == 3:
                        print("computer chose scissors")
                    elif l == 4:
                        print("computer chose kill")
                    else:
                        print("error")
                        break
                    if v == 1 and l == 3:
                        l-=3
                    elif l == 1 and v == 3:
                        v-=3
                
                    elif l == 4 and v == 4:
                        print("you both decide to cheat and bring a gun out, but decide to call it a draw so there isn't blood shed")
                    elif l == 4:
                        print("computer decided to kill you out of pity, next time, don't trust a computer to not cheat")
                    elif v == 4:
                        print("!@$%@$^&*$#@!#!%%&*%^&*!$^")
                        print("congratz! you killed the computer out of rage and instantly won. How do you feel now? you committed murder")
                    elif v < l:
                        print("You lost, better luck next time!")
                    elif v > l:
                        print("You WON! Congratz!")
                    elif v == l:
                        print("tie! try again")
                    else:
                        print("error")
                        break
                else:
                    print("Leaving...")
                    break