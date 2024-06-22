# Dictionary in Pyhton
# info = {
#     "name" : "Tanmay",
#     "cgpa" : 9.08,
#     "marks" : [97,98,99]
# }
# print(info)
# print(info["marks"])

# info["name"] = "Tanmay Raut"
# print(info["name"])

# # we can initialize null dictionary as follows :
# #Just write 
# dict = {} #Then we can add elements later
# print(dict)
# dict["subject"] = ["c" , "Java", "Javascript", "OPPS"]
# print(dict)

# We cna have nested dictionary as well
# students = {
#     "name" : "Tanmay Raut",
#     "subjects" : {
#         "phy" : 50,
#         "chem" : 60,
#         "math" : 70
#     }
# }

# print(students)
# print(students["subjects"]["phy"])

# Dictonary Methods
# print(students.keys()) #returns all keys of dictionary
# print(len(list(students.keys()))) #way to get total number of keys

# print(students.values()) #return all values of dictionary
# print(students.items()) #return (key , val) pair
# print(students.get("subjects")) #return the val specified with that  key
# newIntem = {
#     "rollno" : "2022bit058",
# }
# students.update(newIntem)
# print(students)

# --------------------------------------------------------------------------------------------------------

# Sets  in Python
# collecton = {1,2,3,4,4,4,4,4,"Hello" , "Hello"}
# print(collecton)

# collecton = set() #Syntax to creat empty  set

# Methods of Set
# collecton.add(1)
# collecton.add(1)
# collecton.add(2)
# collecton.add(2)
# collecton.add(2)
# collecton.add("Hello")
# collecton.add(4)

# collecton.remove(1)
# print(collecton.pop()) 
 
# collecton.clear()

# set1 = {10,11,12,13}
# set2 = {10,11,14,15,16}

# print(set1.union(set2))
# print(set1.intersection(set2))

# --------------------------------------------------------------------------------------------------------

# Que1. WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary and add onr by one . Use subject name as keyand marks as values
marks = {}
x = int(input("Enter phy marks : "))
marks.update({"phy" : x})
x = int(input("Enter chem marks : "))
marks.update({"chem" : x})
x = int(input("Enter math marks : "))
marks.update({"math" : x})

print(marks)

#Que2. You are given a list of subjects for sudents. Assume one classroom in required for 1 subject. How many classroom are needed by all students.
# subjects = {"python" , "java", "C++", "python", "java", "C++", "C", "java"}
# print(len(subjects))

#Que 3. Figure out way to store 9 and 9.0 in a set
#Pyhton recognizes 9 and 9.0 as same as val, if I write 2 and 2.0 it will treat both as same val
values = {9 , "9.0"} 
# OR we acn use tuple
values = {
    ("float" , 9.0) ,
    ("int" , 9)
}