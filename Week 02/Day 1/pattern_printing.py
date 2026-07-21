
#-------------------------
# Pattern 1. Right Triangle
#print("Pattern 1")

#for row in range(1, 6):
    #for col in range(row):
        #print("*", end=" ")
    #print()

#------------------
# Pattern 2. Inverted Triangle
#print("Pattern 2")

#for row in range(5, 0, -1):
    #for col in range(row):
        #print("*", end=" ")
    #print()

#-------------------------
# Pattern 3. Number Triangle
#print("Pattern 3")

#for row in range(1, 6):
    #for col in range(1, row + 1):
        #print(col, end=" ")
    #print()

#-----------------------------
#Pattern 4. Same Number Pattern
#print("Pattern 4")

#for row in range(1, 6):
    #for col in range(row):
        #print(row, end=" ")
    #print()

#--------------------
# Pattern 5. Square Pattern
#print("Pattern 5")

#for row in range(5):
    #for col in range(5):
        #print("*", end=" ")
    #print()

#-----------------------
# Pattern 6. Alphabet Pattern
print("Pattern 6")

for row in range(65, 70):
    for col in range(65, row + 1):
        print(chr(col), end=" ")
    print()