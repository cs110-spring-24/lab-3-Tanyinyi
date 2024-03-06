print("Options:1,2,3,4,5,6,7,8,9,10")
run=input("Enter the problem you want to run: ")
run=int(run)
if run==1:
    #1. Write a program that prints out the numbers 1 to 1000.
    print("Running problem 1:")
    for x in range(1,1001):
        print(x)

if run==2:
    #2. Write a program that prints out the odd numbers between 1 and 1000.
    print("Running problem 2:")
    for x in range(1,1001,2):
        print(x)

if run==3:
    #3. Write a program that prints out the numbers between 0 and 1000 that are divisible by 3.
    print("Running problem 3:")
    for x in range(0,1001):
        if x%3==0 and x!=0:
            print(x)

if run==4:
    #4. Write a program that prints out the numbers between 1 and 1000 that are divisible by 3 or 5.
    print("Running problem 4:")
    for x in range(1,1001):
        if x%3==0:
            print(x)
        elif x%5==0:
            print(x)

if run==5:
    #5. Write a program that asks the user to enter a number and prints out all the numbers between 1 and that number that are divisible by 11 or 13. The number entered should be greater than 200. (+10 points) Extra credit if the programs asks again if the number is less than 200. (+5 points)
    print("Running problem 5:")
    user=int(input("Enter a number greater than 200:"))
    while user<=200:
        print("your answer less than or equal to 200, please enter again.")
        user=int(input("Enter a number greater than 200:"))
    for x in range(1,user):
        if x%11==0:
            print(x)
        elif x%13==0:
            print(x)

if run==6:
    #6. Write a program that prints out each letter of a string line by line (+5 points)
    print("Running problem 6: ")
    string=input("Enter a word:")
    for x in (string):
        print(x)

if run==7:
    #7. Write a program that asks the user to enter a string and outputs every second letter. The string must be more than 10 letters long. (+10 points)
    print("Running problem 7:")
    string=input("Enter a string (more than 10 letters):")
    for i in range(1,len(string),2):
        print(string[i])


if run==8:
    #8. Write a program that rolls 1000 dice and prints out the number of times each number was rolled.
    print("Running problem 8:")
    import random
    dice1=0
    dice2=0
    dice3=0
    dice4=0
    dice5=0
    dice6=0
    for rolls in range(1,1000):
        dice=random.randint(1,6)
        if dice==1:
            dice1 +=1
        elif dice==2:
            dice2 +=1
        elif dice==3:
            dice3 +=1
        elif dice==4:
            dice4 +=1
        elif dice==5:
            dice5 +=1
        elif dice==6:
            dice6 +=1
    print(f"you rolled {dice1} times dice 1,{dice2} times dice 2,{dice3} times dice 3,{dice4} times dice 4,{dice5} times dice 5,{dice6} times dice 6,")

if run==9:
    #Write a program that checks if a given number is a prime number. A prime number is a number that is only divisible by 1 and itself. The user enters a number and the programs prints out whether the number is a prime number or not.
    print("Running problem 9:")
    num=int(input("Enter a number:"))
    x=False
    if num>1:
        for i in range(2,num):
            if num%i==0:
                x=True
                break
        if x==True:
            print("it is not a prime number")
        else:
            print("it is a prime number")

    else:
        print("it is not a prime number")

if run==10:
    #Write a program that prints out the prime numbers less than 1000. (+20 points)
    for x in range(2,1000):
        prime=1
        for i in range(2,x):
            if x%i ==0:
                prime=0
                break
            else:
                prime=1
        if prime==1:
            print(x)

        
