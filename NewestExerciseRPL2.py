import string 

#dictionary
start = 8 
end = 17
#variable
Basefee = 0
x = 0
Addfee = 0

#function
x = int(input("Please input the computer-amount : "))
time = int(input("input your time now:"))
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
if (time < start and time> end):
    Basefee = Basefee * 2
    
drop = input("Are you willing to drop off and pick up type : ")
if (drop == "yes"):
    Basefee = Basefee / 2
    
else : 
    print("Total fee : ",Basefee + Addfee)


print("Total fee : ",Basefee + Addfee)
