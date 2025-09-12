import random
rand_no=random.randint(1,101)
print(rand_no)
l=0
y=100
def no_guess():
    guess_no=int(input("enter guess b/w 1-100: "))
    global l
    global y
    
    if(guess_no >= 1 and guess_no <= 100):
        
        if guess_no == rand_no:
            print("!!!HURRAY!!!\nyour guess is correct , you have won the game")
            exit() 
            
        elif guess_no < rand_no:
            l= guess_no if guess_no>l else l
            if(guess_no<l):
                print(f"choose above {l}")
                no_guess()
            else:    
                print(f"Too low , number is greater than {l}")
                no_guess()
                
        else:
            y=guess_no if guess_no < y else y
            if(guess_no > y):
                print(f"choose below {y}")
                no_guess()
            else:    
                print(f"Too high , number is lesser than {y}")   
                no_guess()
    
    else:
        print("invalid guess ,please choose b/w 1-100")            
        no_guess() 
           
print("***WELCOME TO NUMBER GUESSING GAME***")    
no_guess()

