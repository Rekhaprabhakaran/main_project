import os
folder_path='C:\\Users\\DELL\\OneDrive\\Desktop\\python\\recipe'
if not os.path.exists(folder_path): 
    os.makedirs(folder_path) 

food_recipe_name=input("Enter the recipe name:")
ingredients=input("enter the ingredients:")
instructions=input("Enter the instructions to make the dish:")
file_name=f'{food_recipe_name}.txt'


with open (f'{folder_path}/{food_recipe_name}.txt','a') as f:
    f.write(f'Dish Nams:{food_recipe_name} \n\nIngredients:\n{ingredients}\n\nInstructions:\n{instructions}')
