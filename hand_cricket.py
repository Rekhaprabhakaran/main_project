import random
p_score=0
c_score=0

player_selection=input("player's selection: Odd or even??").lower()
player_hand=int(input("player Enter a number between 1 and 6:"))
while player_hand>6:
        player_hand=int(input("player Enter a number between 1 and 6:"))
computer_hand=random.randint(1,6)  
total=player_hand+computer_hand
print(total)
if total%2==0:
        odd_even="even"
        print("even")
else:
        odd_even="odd" 
        print("odd")    
def player_bat(): 
        global p_score
        global c_score
         
        print("player is batting ,computer is bowling")
        player_score=int(input("player enter a number between 1 and 6:"))
        computer_score=random.randint(1,6)
        while player_score !=computer_score:
                        p_score+=player_score
                        player_score=int(input("player enter a number between 1 and 6:"))
                        computer_score=random.randint(1,6)
        print("player is out.player score:",p_score) 
        print("computer is batting and player is bowling")
        computer_score=random.randint(1,6)    
        player_score=int(input("computer enter a number between 1 and 6:")) 
        while player_score !=computer_score:
                        c_score+=computer_score
                        computer_score=random.randint(1,6)
                        player_score=int(input("computer enter a number between 1 and 6:"))
                        
        print("computer is out.computer score:",c_score)  
def computer_bat():
        global p_score
        global c_score

        print("computer is batting and player is bowling")
        computer_score=random.randint(1,6)    
        player_score=int(input("computer enter a number between 1 and 6:")) 
        while player_score !=computer_score:
                        c_score+=computer_score
                        computer_score=random.randint(1,6)
                        player_score=int(input("computer enter a number between 1 and 6:"))
                        
        print("computer is out.computer score:",c_score)
        print("player is batting ,computer is bowling")
        player_score=int(input("player enter a number between 1 and 6:"))
        computer_score=random.randint(1,6)
        while player_score !=computer_score:
                        p_score+=player_score
                        player_score=int(input("player enter a number between 1 and 6:"))
                        computer_score=random.randint(1,6)
        print("player is out.player score:",p_score)            
if player_selection==odd_even:
        p_bat_bowl_selection=input("player Choose to bat or bowl..:").lower()
        if p_bat_bowl_selection=="bat":
                player_bat()
        else:
                computer_bat()
          
else:
        c_bat_bowl_selection=input("computer choose to bat or bowl..:").lower()
        if c_bat_bowl_selection=='bat':
                computer_bat()
        else:
                player_bat()
                     
if p_score>c_score:
                
                print("player won")
elif c_score>p_score:
                print("computer won")
else:
                print("Its a tie")                


                        
                
                
                       
                
                        
                                
                        
                                 
    
    
        
