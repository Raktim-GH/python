# 1. Write a program to find the sum of the length of all the 
# string data items present inside the given tuple if sum is greater then 50,
# then print all the string data items present inside the tuple in the form of list collection, 
# else print cube of sum.

# tup = eval(input("rtghh"))
# s=0
# l=[]
# for i in tup:
#     if type(i)==str:
#         # p=len(i)
#         s+=len(i)
#         l.append(i)
# if s>15:
#     print(l)
# else:
#     print(s**3)


# 71. WAP to print all the integers present in a list.

# l=eval(input())
# for i in l:
#     if isinstance(i,int):
#         print(i)

# 72.WAP to find the length of homogenenous tuple without len().

# t=eval(input())
# count=0
# for i in t:
#     count+=1
# print(count)

# 73. WAP to extract all the even numbers present in a list.

# l=eval(input())
# for i in l:
#     if i%2==0:
#         print(i)

# 74.WAP to remove duplicates from a list.

# l=eval(input())
# s=set(l)
# l2=list(s)
# print(l2)
        
        
# 75.WAP to reverse a string without using slicing.

# s=str(input())
# rev_string=""
# for i in s:
#     rev_string = i+rev_string

# print(rev_string)    

# 76.WAP to extract all the lowercase charcaters in a string only if the ASCII value os even.

# s=eval(input())
# for i in s:
#     if i.islower():
#         if ord(i)%2==0:
#             print(i)
            
# 77.WAP to check whether the last digit of an integer is even or not.

# i=int(input())
# last_digit = i%10

# if(last_digit%2==0):
#     print("Last digit is even")
# else:
#     print("last digit is odd")

# 78.WAP to extract all the key value pairs from the dictionary
# only if the keys are of string datatype and values are int.

# d = eval(input("Enter a dictionary: "))

# for k, v in d.items():
#     if isinstance(k, str) and isinstance(v, int):
#         print(k, ":", v)

        
    
# 79.wap to reverse a given number without using type casting and slicing.

# n=int(input())
# rev=0
# digit = 0
# while n>0:
#     digit = n%10
#     rev = rev*10+digit
#     n//=10
# print(rev)

# 80.WAP tp extract key value pairs from the dictionary 
# only if both keys and values are exactly the same


# d = eval(input("Enter a dictionary: "))
# for k, v in d.items():
#     if isinstance(k, int) and isinstance(v, int):
#         if k==v:
#             print(k, ':', v)

# 81. WAP to check the number is prime or not using break.

# n=int(input("Enter any Number:"))
# c=0
# for i in range(2,n):
#     if n%i==0:
#         c+=1
#         break
# if c==0:
#     print("Prime")
# else:
#     print("Composite")
    
    
# 82.WAP to get the following output using len function.
# S='power star'
# out = {'power':5,'star':4}

# def check(n):
#     dict={}
#     word=''
#     for i in n:
#         if i!=' ':
#             word+=i
#         else:
#             if word:
#                 dict[word] = len(word)
#                 word = ''
#     print(dict)

# i=str(input("Enter any string:"))
# i=i+' '
# check(i)        
    
 
 
# 83.WAP to get the following output using len function.
# S='power star'
# out = {'power':'rewop','star':'rats'}
   
# def check(n):
#     dict={}
#     word=''
#     for i in n:
#         if i!=' ':
#             word+=i
#         else:
#             if word:
#                 dict[word] = word[::-1]
#                 word = ''
#     print(dict)

# i=str(input("Enter any string:"))
# i=i+' '
# check(i)


# 84. WAP to extract all the non default values from a list.

# l=eval(input("Enter any List:"))
# l1=[]
# for i in l:
#     if i!=[]:
#         l1.append(i)
#     else:
#         continue
# print(l1)

# 85.WAP to check whether the list is homogenious or not.

# def homo_check(l):
#     c=d=0
#     for i in l:
#         if all(type(x)==type(l[0]) for x in l):
#             c+=1
#         else:
#             d+=1
            
#     if(c>1):
#         print("Homogenous")
#     elif(d>0):
#         print("Heterogenous")
# l=eval(input("Enter any list:"))
# homo_check(l)
 
 
#86.WAP to replace the spaces by * present in a string.

# def replacer(s):
#     s1="" 
#     for i in s:
#         if i==' ':
#             s1+="*"
#         else:
#             s1+=i
#     print(s1)        
               
# s=str(input("Enter any string:"))
# replacer(s)


# 87.WAP to count the number of occurances of a specified character.

# def occ_check(s,s1):
#     c=0 
#     s2=s.lower()
#     s1=s1.lower()
#     for i in s2:
#         if i==s1:
#             c+=1

#     print(c)        
               
# s=str(input("Enter any string:"))
# s1=str(input("The Character you want to check the occurance:"))
# occ_check(s,s1)

# 88.WAP to get the following output.
# S='always keep smiling'
# out = 'syawla peek gnilims'

# def reverse(s):
#     word=''
#     s1=''
#     for i in s:
#         if i!=' ':
#             word+=i
#         else:
#                 s1+=word[::-1]+' '
#                 word = ''
#     print(s1)   
    
# s=str(input("Enter any String:"))
# s+=' '
# reverse(s)

# 89. WAP tp get the following output.
# S='push maadi kushi padi'
# out= {'push':'ph','maadi':'a','kushi':'s','padi':'pi'}

# def word_dict(s):
#     word=''
#     dict={}
#     for i in s:
#         if i !=' ':
#             word+=i
#         else:
#             if word:
#                 if len(word)%2==0:
#                     dict[word]=word[0]+word[-1]
#                 elif len(word)%2!=0:
#                     length=(len(word))//2
#                     dict[word]=word[length]
#                 word=''
#     print(dict)
            

# s=str(input("Enter any string:"))
# s+=' '
# word_dict(s)     


# 90. WAP to extract all the even numbers between 1 to 1000 using continue..

# for i in range(1,100):
#     if i%2==0:
#         print(i)
#         continue   


# 91.WAP to toggle a string.

# def word_dict(s):
#     result=''
#     for i in s:
#         if 'a'<=i<='z':
#             result += chr(ord(i)-32)
#         elif 'A'<=i<='Z':
#             result+=chr(ord(i)+32)
#         else:
#             result+=i
#     print(result)                     

# s=str(input("Enter any string:"))
# word_dict(s)    


# 92.WAP to extract all the digits present inside a given string collection. 

# def digit_extract(s):
#     result=''
#     for i in s:
#         if '0'<=i<='9':
#             result+=i
#             continue
#     print(result)       

# s=str(input("Enter any string:"))
# digit_extract(s) 

# 93.WAP extract upper, lower, digit, special characters present in a string to different output variable.

def diff_extract(s):
    res_upper=''
    res_lower=''
    res_digit=''
    res_special=''
    for i in s:
        if 'A'<=i<='Z':
            res_upper+=i
        elif 'a'<=i<='z':
            res_lower+=i
        elif '0'<=i<='9':
            res_digit+=i
        else:
            res_special+=i
    print("Upper case:",res_upper,"Lower case:",res_lower,"Digit:",res_digit,"Special character:",res_special)
            
s=str(input("Enter Mixed string:"))
diff_extract(s)    