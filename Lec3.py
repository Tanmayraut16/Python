# List in Python ✅
# marks = [24, 12, 15, 88, 99]
# print(type(marks))
# print(marks)
# print(len(marks))
# print(marks[2])
# print(marks[1])

# In python we can store diffrent data types in list e.g given below
# detail = ["Tanmay" , 20, "Engineering", 9.08]
# print(detail)

# ------------------------------------------------------------------------------------

# List Slicing - It is similar to String Slicing ✅
# ------------------------------------------------------------------------------------

# List Methods✅
# arr = [4,2,10,17,3,48,33]

# arr.append(11) #add an element at end
# print(arr)

# arr.sort() #Sort in Ascending order
# print(arr)

# arr.sort(reverse=True) #Sort in Descending order
# print(arr)

# arr.reverse() #Reverse the list

# arr.insert(2 , 19)
# print(arr)

# arr.remove(11) #Removes the first occurence of 11
# print(arr)

# arr.pop(4) #Removes the  element at an index
# if we do not provide index it will pop the last elemnt of list 

# ------------------------------------------------------------------------------------

# Tuple in python✅
# A built in data type that  lets us create immutable sequence of values

# tup = (10,20,3,0,4,0)
# tup[0] = 0 #shows error

# whenever we want a single ele in tup we write with helpof comma
# tup = (1)
# print(type(tup)) #it shows type as int

# tup = (1,)
# print(type(tup)) #it shows type as tuple

# ------------------------------------------------------------------------------------

# Que WAP to check if a list is palindrome or not (Hint : use copymethod of list)
list1 = [1,2,3,3,2,1]

list2 = list1.copy()
list2.reverse()

if(list1 == list2):
    print("List is Palindrome")
else:
    print("List is not Palindrome")