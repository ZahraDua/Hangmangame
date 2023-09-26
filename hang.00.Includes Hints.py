import random
import time

# replay   = A loop to restart the game
# pre_body = Initializing the variables.
# body     = All the logics used in the game.


print("\nWelcome to Hangman game\n")
name = input("Player name: ")
print("Greetings " + name + "!!")
print(name,",Guess the codeword to SAVE Hangman")
print("\nYour Time Starts......") 
time.sleep(2)
t1 = time.time()
print("\t\aNow !!!\t")

# Defining Functions

def pre_body():
    global count
    global display
    global word
    global already_guessed
    global length
    global l1
    global l2
    l1= ["pink","red","yellow","green" , "white" , "black" , "brown" , "blue" , "orange" , "purple"]
    l2 =["tiger","lion","dog","cat" , "rat" , "elephant" , "zebra" , "giraffe"]
    lt =[l1,l2]
    lf = random.choice(lt)
    word = random.choice(lf)
    ask = input("do you want a hint (type yes) : ")
    if ask == "yes" or ask == "Yes" or ask == "YES":
        if word in l1:
            print("its a color")
        else:
            print("its an animal")
    else:
        print("then go do it yourself!!")
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []

def replay():
    play_again = input("Type \"y\" to play again : ")
    if play_again == "Y" or play_again == "y" :
        pre_body()
        body()
    else:
        print("\n\tThanks For Playing...\n\t!! BYE !!")
        exit()

def body():
    global length
    global count
    global display
    global word
    global already_guessed
    global l1
    global l2
    limit = 5
    guess = input("\nCodeWord:  " + display + "\nEnter your guess: ")
    guess = guess.strip()
    if len(guess) == 0 or len(guess) >= 2 or guess.isalpha()== False:
        print("Invalid Input, Try a letter\n")
        body()
   
    elif guess in word:
        already_guessed.extend([guess])
        #index = word.find(guess)
        #display = display[:index] + guess + display[index + 1:]
        for i in range (length) :
            if word[i] == guess :
                display = display[:i] + guess + display[i + 1:]
        #print(display + "\n")
        print("\n\t**correct**")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("\t**Wrong guess** \n\tlifes left =",str(limit - count),"\n")


        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
            print("\t**Wrong guess** \n\tlifes left =",str(limit - count),"\n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("\t**Wrong guess** \n\tlifes left =",str(limit - count),"\n")



        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |    \O/\n"
                  "  |     |\n"
                  "  |      \n"
                  "__|__\n")
            print("\t**Wrong guess** \n\tlifes left =",str(limit - count),"\n")



        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |    \O/ \n"
                  "  |     | \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("\t**Wrong guess** \n\tlifes left =",str(limit - count),"\n")
            replay()


    if display == word :
        print("Congrats!! You Saved Hangman.")
        print("codeword : ",word,"\n")
        t2 = time.time()
        t3=t2-t1
        print("Time taken =",t3)
        replay()

    elif count != limit:
        body()
    
#using functions
pre_body()
body()