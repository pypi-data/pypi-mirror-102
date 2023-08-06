import random
class match():
    def __init__(self):
        ans = "yes"
        while(ans == "yes" or ans == "Yes" or ans == "YES"):
            i = 0
            score = 0
            score1 = 0
            #for repeation if any information for toss is wrong
            while i == 0:
                toss = random.randrange(1,7)
                toss2 = input("Enter Number for toss in range 1 - 6: ")
                #print(toss2,type(toss2))
                if toss2 != '1' and toss2 != '2' and toss2 != '3' and toss2 != '4' and toss2 != '5' and  toss2 != '6':
                    print('Wrong Input!!\nEnter Again\n')
                    continue
                else:
                    toss2 = int(toss2)
                    i = 1
                #repeat if value entered is not in range
            i = 0
            while i == 0:
                #increment so that loop doesn't repeat
                i = 1
                sum = toss + toss2
                d = 0
                while d == 0:
                    a = input("Odd or even? ")
                    #veryfying desission of toss
                    if a != "odd" and a !="Odd" and a != "even" and a != "Even" and a != "o" and a != "e":
                        print("Wrong input")
                        d = 0
                        continue
                    elif a == "odd" or a == "Odd" or a == "ODD" or a == "o":
                        if sum % 2 == 0:
                            print("You lost the toss\n")
                            k = random.randrange(0 , 2)
                            d = 1
                            
                        else:
                            print("You won the toss\n")
                            k = eval(input("Enter your option \"0\" for batting \"1\" for bowling\n "))
                            d = 1

                    elif a == "even" or a == "Even" or a == "EVEN" or a == "e":
                        if sum % 2 == 0:
                            print("You won the toss\n")
                            k = eval(input("Enter your option \"0\" for batting \"1\" for bowling \n"))
                            d = 1
                        else:
                            print("You lost the toss\n")
                            k = random.randrange(0 , 2)
                            d = 1

        #if user doesn't enter odd or even repeating the loop
        
        #score of team current innings
            score = 0

        #score of team previous innings
            score1 = 0

        #to execute if condition again
            p = 0

        #in order to repeat whle loop , if value is more than 2 so it will end
            l = 0

            while(l < 2):
            #k is input of bowling or batting
            #user batting part
                if k == 0 and score1 >= score:
                    print("Time for you to bat \n")
                    #repeated loop till batsman is not out and score of previous total is not covered
                    while k == 0 and score1 >= score:
                        run = (input("Enter your number between 1-6 for batting "))
                        if run != '1' and run != '2' and run != '3' and run != '4' and run != '5' and run != '6':
                            print("Wrong input!!\n")
                            continue

                        run = int (run)
                        bowl = random.randrange(1,7)

                        #if bowl and run both are equal then batsman is out

                        if  bowl == run:
                            print("OUT!!!")
                            print("Your score is : {} \n".format(score))

                        #to check what is last inning

                            p = 1
                            l += 1
                            k = 1
                            if l == 1:
                                score = 0
                        else :
                            score += run
                            print("You scored {} runs \n Your score is : {} ".format(run,score))
                            if l == 0:
                                score1 = score
            #user boling part
                elif k == 1 and score1 >= score :
                    print("Time or you to bowl\n")
                    #repeated loop till batsman is not out and score of previous total is not covered
                    while k == 1 and score1 >= score:
                        bowl = random.randrange(1,7)
                        run = (input("Enter your number between 1-6 for bowling  "))
                        if run != '1' and run != '2' and run != '3' and run != '4' and run != '5' and run != '6':
                            print("Wrong input!!\n")
                            continue
                        run = int (run)
                        if  bowl == run:
                            print("OUT!!!")
                            print("My score is : {}\n ".format(score))
                            l += 1
                            k = 0
                            #to check what is last inning
                            p = 2
                            if l == 1:
                                score = 0
                        else :
                            score += bowl
                            print("I scored {} runs \n My score is :{} ".format(bowl,score))
                            if l == 0:
                                score1 = score
                        continue
            print("Match Ended!!")
            if p == 2:
                q = "Bowl"
            elif p == 1:
                q ="Bat"
            print(" last inning : {}\n last score {} \n first score {}".format(q,score,score1))
            if p == 1 and score1 > score:
                print("\nI won!!\n")
            elif p == 2 and score1 > score:
                print("\nYou won!!\n")
            elif p == 1 and score1 > score:
                print("\nYou won!!\n")
            elif p == 2 and score1 > score:
                print("\nI won!!\n")
            else :
                print("Match draw\n")
                
            ans = input(" DO YOU WANNA PLAY AGAIN? (yes/no):\n ")
            print('_____________________________________________')
            if ans != "yes" and ans != "Yes" and ans != "YES" and ans != "y":
                print("Have a nice day!")
