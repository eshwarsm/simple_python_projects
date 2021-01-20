import random 
while True:     
     print("Roll?")    
     user = str(input("y/n\n"))     
     if user=="y":         
        number = random.randint(1,6)         
        print("\n")
        print(number)
        print("\n")     
     else:         
        break
