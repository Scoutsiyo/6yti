import random

carga = ["saved","saved","saved","cooked","saved","saved"]
random.shuffle(carga)
sufle = input("Do you want to shuffle? ").lower()
if sufle == "yes":
    random.shuffle(carga)
    sufle = input("Do you want to shuffle? ").lower()
    
    while sufle == "yes":
        
        random.shuffle(carga)
        sufle = input("Do you want to shuffle?").lower()
     
        
print("Let's play") 
def shoot():
    click = input("Shoot ")

for status in carga:
    shoot()
    if status == "saved":
        print("You're alive")
    else:
        print("YOU LOST") 
        break
    

