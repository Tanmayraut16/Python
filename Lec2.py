# String ✅
# Indexing✅
# Slicing✅
# String Functions✅
# Conditional Statements✅

# -----------------------------------------------------
# Que 1 WAP to input user name and print its length
# name = input()
# print("User name is : ",name , "\nIts Length = " , len(name))

# -----------------------------------------------------
# Que 2. WAP to find ocurrences of $ in a String
# str = "jhciu$$$$hgfyfg$$$$$srfeawol$$$$xgfd$$$$$$$$$$$$$$$$$$$$$$$$"
# print("Occurences = ", str.count('$'))

# -----------------------------------------------------
# Que 3. Grade Students based on their marks. Take input of marks from student.
maths = int(input("Enter Maths mark : "))
phy = int(input("Enter Physics mark : "))
chem = int(input("Enter Chemistry mark : "))
bio = int(input("Enter Biology mark : "))
eng = int(input("Enter English mark : "))
percent = (maths+phy+chem+bio+eng)/5

if(percent >= 90):
    print("You Have A+ Grade")
elif(percent >= 81 and percent < 90):
    print("You have A Grade")
elif(percent >= 71 and percent < 80):
    print("You have B+ Grade")
elif(percent >= 61 and percent < 70):
    print("You have B Grade")
elif(percent >= 51 and percent < 60):
    print("You have C+ Grade")
elif(percent >= 41 and percent < 50):
    print("You have C Grade")
elif(percent >= 31 and percent < 40):
    print("You have D Grade")
elif(percent < 33):
    print("You have F Grade")