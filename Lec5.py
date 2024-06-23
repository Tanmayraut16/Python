# Loop 
# While loop 
# n = int(input("Enter the number of which you want its table : "))
# i = 1
# while i <= 10:
#     print(n*i)
#     i+=1

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("Enter the number you want o search : "))
# i = 0
# while i < len(nums):
#     if(x == nums[i]):
#         print(x , " is at index ", i)
#     i+=1

# print("Number not found")

# name = "Tanmay Raut I.T"
# for ch in name:
#     print(ch)

# for e in range(5) : print(e)
# for e in range(2 , 5) : print(e)
# for e in range(1,10, 3) : print(e)

# ------------------------------------------------------------------------------------

# Sum of n numbers
# n = int(input("Enter the number : "))
# sum = 0
# for i in range(1 , n+1, 1) :
#     sum += i

# print("Sum for number's [1 ,",n,"] is" , sum)

# ------------------------------------------------------------------------------------

# Factorial of number
n = int(input("Enter the number : "))
fact = 1
for i in range(1 , n+1, 1) :
    fact *= i

print("Factorial of ",n," is" , fact)