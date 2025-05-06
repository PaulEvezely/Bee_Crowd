current_food, current_food2, current_food3 = input().split() 

food, food2, food3 = input().split()

rest = 0
if int(food) > int(current_food):
    rest+=int(food)- int(current_food)
if int(food2) > int(current_food2):
    rest+= int(food2) - int(current_food2)
if int(food3) > int(current_food3):
    rest+= int(food3) - int(current_food3) 
print(rest)