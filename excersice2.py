from datetime import datetime
from datetime import time
import string 

#dictionary
currentime = datetime.now()
star = time(8,0,0)
end = time(17,0,0)
#variable
Basefee : int
x : int
Addfee : int
drop : string

#function
x = int(input("Please input the computer-amount : "))
if (x == 1 or x == 2):
    Basefee += 50
    Addfee = 0
elif (x >= 3 and x <= 10):
    Basefee += 50 
    for i in range(0,x):
        Addfee += 10
elif (x >10):
    Basefee += 500
    for i in range(0,x):
        Addfee += 10
if (currentime < star and currentime > end):
    Basefee = Basefee * 2
drop = input(string("Are you willing to drop off and pick up type (yes): "))
if (drop == "yes"):
    Basefee = Basefee / 2

print("Total fee : ",Basefee + Addfee)