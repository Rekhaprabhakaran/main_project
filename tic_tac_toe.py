#tic tac toe
li=['_','_','_','_','_','_','_','_','_']

class Board():
    def pattern():
        for i in range(3):
            print(li[i],end=' ')
        print('')
        for i in range(3,6):
            print(li[i],end=' ')
        print('')
        for i in range(6,9):
            print(li[i],end=' ')
        print('')
b=Board 
b.pattern()
  
player_turn=True
computer_turn=False

while li[0] =='_' or li[1] =='_' or li[2] =='_' or li[3] =='_' or li[4] =='_' or li[5] =='_' == li[6] =='_' or li[7] =='_' or li[8] =='_':
    if player_turn==True:
        
        index=int(input("Player Turn:Enter the index position between 0 to 8 to write your symbol 'X':"))
        if index>8:
            print("please enter an index between 0to 8")
        else:
            if  li[index] =="_":
                li[index]='X'
                player_turn=False
                computer_turn=True
            else:
                print("space is already taken") 
                player_turn=True
                computer_turn=False       
        
            b.pattern()
         
        
        if li[0]=='X' and li[1]=='X' and li[2]=='X':
            print("player  won")
            break
        elif li[3]=='X' and li[4]=='X' and li[5]=='X':
            print("player  won")   
            break 
        elif li[6]=='X' and li[7]=='X' and li[8]=='X':
            print("player  won")
            break
        elif li[3]=='X' and li[3]=='X' and li[6]=='X':
            print("player  won")
            break
        elif li[1]=='X' and li[4]=='X' and li[7]=='X':
            print("player  won")
            break
        elif li[2]=='X' and li[5]=='X' and li[8]=='X':
            print("player  won")
            break
        elif li[0]=='X' and li[4]=='X' and li[8]=='X':
            print("player  won")
            break
        elif li[2]=='X' and li[4]=='X' and li[6]=='X':
            print("player  won")
            break
        elif li[0] !='_' and li[1] !='_' and li[2] !='_' and li[3] !='_' and li[4] !='_' and li[5] !='_' and li[6] !='_' and li[7] !='_' and li[8] !='_':
            print("its a tie")
    elif computer_turn==True:
                index=int(input("Computer Turn:enter the index position between 0 to 8 to wriye your symbol '0':"))
                if index>8:
                    print("please enter an index between 0to 8")
                else:
                    if li[index] =="_":
                        li[index]='0'
                        computer_turn=False
                        player_turn=True
                    else:
                        print("space is already taken") 
                        computer_turn=True
                        player_turn=False
                
                    b.pattern()
                
                if li[0]=='0' and li[1]=='0' and li[2]=='0':
                    print("computer  won")
                    break
                elif li[3]=='0' and li[4]=='0' and li[5]=='0':
                    print("computer  won")   
                    break 
                elif li[6]=='0' and li[7]=='0' and li[8]=='0':
                    print("computer  won")
                    break
                elif li[3]=='0' and li[3]=='0' and li[6]=='0':
                    print("computer  won")
                    break
                elif li[1]=='0' and li[4]=='0' and li[7]=='0':
                    print("computer  won")
                    break
                elif li[2]=='0' and li[5]=='0' and li[8]=='0':
                    print("computer  won")
                    break
                elif li[0]=='0' and li[4]=='0' and li[8]=='0':
                    print("computer  won")
                    break
                elif li[2]=='0' and li[4]=='0' and li[6]=='0':
                    print("computer  won")
                    break
                elif li[0] !='_' and li[1] !='_' and li[2] !='_' and li[3] !='_' and li[4] !='_' and li[5] !='_' and li[6] !='_' and li[7] !='_' and li[8] !='_':
                    print("its a tie")
        
            
       
        





          
        
      
            