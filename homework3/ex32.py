#Make a loop over integer numbers from 1 to 40.
#If x is divided by 5 then print a message 'x is divided by 5'.
#If x is divided by 7 then print a message 'x is divided by 7'.
#If x is divided by 5 and 7 then print a message 'x is divided by 5 and 7'.
#Skip x = 13.
#If x is not divided by 5 and x is not divided by 7 
#then print a message 'x is not important'.
#Prepare two solutions with 'while' and 'for' loops.

#Solution1 loop for
print("\nSolotion while loop:\n")
for x in range(1,41):
    if x%5 == 0 and x%7 != 0:
        print(x, "is divided by 5")
    elif x%7 == 0 and x%5 != 0:
        print(x, "is divided by 7")
    elif x%5 == 0 and  x%7 == 0:
        print(x, "is divided by 5 and 7")
    elif x == 13:
        pass
    else:
        print(x, "is not important")

#Solution 2 loop while:

print("\n\nSolotion while loop:\n")
x = 1
while x < 41:
    if x%5 == 0 and x%7 != 0:
        print(x, "is divided by 5")
    elif x%7 == 0 and x%5 != 0:
        print(x, "is divided by 7")
    elif x%5 == 0 and  x%7 == 0:
        print(x, "is divided by 5 and 7")
    elif x == 13:
        pass
    else:
        print(x, "is not important")
    x += 1
