# 1. Wap to reverse a given string without using Typecasting or Slicing.

# def reverse_string(input_string):
#     reversed_str = ""
#     for char in input_string:
#         reversed_str = char + reversed_str  
#     return reversed_str


# input_string = "hello"
# print("Original String:", input_string)
# print("Reversed String:", reverse_string(input_string))

# 2. Wap to reverse a given number without using Typecasting or Slicing.

# def reverse_number(num):
#     reversed_num = 0 
#     while num > 0:
#         digit = num % 10
#         reversed_num = reversed_num * 10 + digit
#         num //= 10
#     return reversed_num

# print(reverse_number(12345))  

# 3.Wap to check the number is armstrong or not.

# def armstrong(num):
#     arm_no = 0
#     while num > 0:
#         digit = num % 10
#         arm_no += digit * digit * digit
#         num //=10
#     return arm_no

# given = int(input("Enter Any Number to check it is Armstrong or Not:"))
# armstrong(given)
# if (armstrong(given) == given):
#     print( given,"Is Armstrong Number")
# else:
#     print( given,"is not Armstrong Number")

# 4. Wap to check the number is a neon number or not.
# def neon_num(num):
#     sqr = num * num
#     neon = 0
#     while sqr > 0:
#         digit = sqr % 10
#         neon += digit
#         sqr //=10
#     return neon

# num = int(input("Enter Any Number to check it is Neon or Not:"))
# neon_num(num)
# if (neon_num(num) == num):
#     print(num,"Is Neon Number.")
# else:
#     print(num,"Is not Neon Num.")


# 5. WAP to convert decimal to binary.

# def con_binary(n):
#     bi = ""
#     if n == 0:
#         return "0"
#     while n>0:
#         rem = n%2
#         bi = str(rem) + bi
#         n //=2
#     return bi

# num = int(input("Enter a decimal number: "))
# binary = con_binary(num)
# print("Binary equivalent is:", binary)


# 6. WAP to remove the duplicates from a collection without typecasting.

# def remove_duplicates(collection):
#     result = []
#     for item in collection:
#         if item not in result:
#             result.append(item)
#     return result

# l=[]
# n=int(input("Enter the size of the list:"))
# for i in range (n):
#     l.append(int(input("Enter elements in the list:")))
    
# cleaned = remove_duplicates(l)
# print("Original:", l)
# print("After removing duplicates:", cleaned)


#7. WAP to check a number is xylem or phloem.

# def xylem(num):
#     if len(num) <= 2:
#         print("Number must have at least 3 digits.")
#     else:
#         first = int(num[0])
#         last = int(num[-1])

#     middle_sum = 0
#     for digit in num[1:-1]:
#         middle_sum += int(digit)

#     if first + last == middle_sum:
#         print("The number is Xylem Number.")
#     else:
#         print("The number is not Xylem Number.")

    
# num = input("Enter a number: ")
# xylem(num)

        
# 8.WAP to find the longest word in a string without split function.


# def long(n):
#     word=''
#     longest=''
    
#     for chr in n:
#         if chr !=' ':
#             word += chr
#         if len(word)>len(longest):
#             longest = word
#             word=''
#     return longest

# i = str(input("Enter any string:"))
# i=i+' '
# print("Longest word:",long(i))

# 9. WAP to count the number of words without using split function.

# def cou(n):
#     word =''
#     for i in n:
#         if i !=' ':
#             word +=i
#     return len(word)

# n = str(input("Enter any string:"))
# n=n+' '
# print("The number of Words:",cou(n))
    

# 10. WAP to convert binary to decimal

# num = int(input("Enter any Binary Number:"))
# dec = 0
# p=0
# while num>0:
#     digit = num % 10
#     dec +=digit*(2**p)
#     num //=10
#     p+=1
# print(dec)
    

# 11. s='power star' o/p -> {'power':5 , 'star':4}

# def check(n):
#     word=''
#     d={}
#     for chr in n:
#         if chr !=' ':
#             word += chr
#         else:
#             if word:
#                 d[word] = len(word)
#                 word=''
#     print(d)

# i = str(input("Enter any string:"))
# i=i+' '
# check(i)


# 12. input=i am , output = i ma
