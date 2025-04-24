# def fact(n):
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i)
            
# n=int(input("Enter Any Number:"))
# fact(n)

# l=list(map(str,input().split()))
# for i in l:
#     if len(i)==1:
#         print(i)
        
        
# n=int(input("Enter the Size of the list:"))
# l = []
# for i in range (n):
#     l.append(input("Enter elements:"))
    
# for i in l:
#     if len(i)==1:
#         print(i)     


# write a code to store the odd and even data from a list into one odd and one even list.

# n=int(input("Enter size of the list:"))
# l=[]
# lodd=[]
# leven=[]
# for i in range(n):
#     l.append(int(input("Enter the number : ")))

# for i in l:
#     if i%2==0:
#         leven.append(i)
#     else:
#         lodd.append(i)
# print(lodd)
# print(leven)   


# write a code to check if the given list is homogeneous or Heterogenous.

# n=int(input("Enter size of the list:"))
# l=[]
# for i in range(n):
#     l.append((eval(input("Enter the number : "))))

# c=0
# for i in range (n-1):
#     if type(l[i]) == type(l[i+1]):
#         c+=1
#     else:
#         c=0
# if c==0:
#     print("heterogenous")
# else:
#     print("homogenous")

#                           OR   
               
# n = int(input("Enter size of the list: "))
# l = [eval(input("Enter elements:")) for _ in range(n)] # we can use "_" in the case of unknown number of test cases #

# if all(type(x) == type(l[0]) for x in l):
#     print("homogenous")
# else:
#     print("heterogenous")



# WAP TO TOGGLE A GIVEN STRING(TO CHANGE UPPERCASE INTO LOWERCASE)

# s=input("Enter any String:")
# s1=""
# for i in range (len(s)):
#     if s[i] in 'abcdefghijklmnopqrstuvwxyz':
#         s1+=s[i].upper()
#     else:
#         s1+=s[i].lower()
# print(s)
# print(s1)    
#                                  OR
    
# s=input("Enter any String:")
# s1=""
# i=0
# while i <len(s):
#     if s[i] in 'abcdefghijklmnopqrstuvwxyz':
#         s1+=s[i].upper()
#     else:
#         s1+=s[i].lower()
#     i+=1
# print(s)
# print(s1)


# st1 = 10110111 and st2 = 11111011 count the unmatched iterates.
# st1 = int(input("Enter first number: "))
# st2 = int(input("Enter second number: "))

# count = 0
# while st1 > 0 and st2 > 0:
#     if st1 % 10 != st2 % 10:
#         count += 1
#     st1 //= 10
#     st2 //= 10

# print("Unmatched digits:", count)
#                               OR

# s1 = 10110111 
# s2 = 11111011
# str1 = str(s1)
# str2 = str(s2)
# c=0
# i=0
# while i<len(str1):
#     if str1[i]!= str2[i]:
#         c+=1
#     i+=1
# print(c)


