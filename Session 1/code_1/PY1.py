# # ######### importing modules ##########

# # import pName
# # pName.printname("Mena",19)

# # from pName import printname
# # printname("Ali",20)

# # from shopping import pay
# # pay.payment(100, "Credit Card")

# # from math import sqrt
# # v2=sqrt(9)
# # print(v2)

# # import pName as pn
# # pn.printname("Sara",25)


# # import math as m
# # v3=m.sqrt(9)
# # print(v3)


# ########### Exception Handling ##########

# # num1=int(input("enter a number: "))
# # num2=int(input("enter a number: "))

# # try:
# #     div=num1/num2
# #     print("the result is: ",div)
# # except :
# #     print("you can't divide by zero")    

# # print("this is the end of the program")

# # try:
# #     x=int(input("enter a number: "))
# #     print("your number is: ",x)
# # except :
# #     print("you must enter a number")    
# # finally:
# #     print("this is the end of the program")

# # num=int(input("enter a number: "))

# # try:
# #     num=int(input("enter a number: "))
# #     print(10/num)  
# # except ZeroDivisionError:
# #     print("you can't divide by zero")
# # except ValueError:
# #     print("you must enter an integer") 
# # except Exception as e:
# #     print (e)      
    
# # finally:
# #     print("Thank you")

# # age=int(input("Enter Your Age: "))


# #### Custom Exceptions ####
# # class invalidAgeError(Exception):
# #     pass
# # class EnglishSpeakers(Exception):
# #     pass
# # try:
# #     lan=input("Enter Your lang: ")
# #     if lan != "English":
# #         raise EnglishSpeakers("lang must be an English")
# #     print("WELCOME")
# # except EnglishSpeakers as e:
# #     print("Error:", e)

# # def add(a,b):
# #     return a+b
# # print(add(5,3))

# # a=lambda a, b: a + b
# # print(a(5,4))

# #lambda function
# # user=input("Enter Your Name: ")
# # var=lambda user:print(f"Hello {user}")
# # var(user)

# # add = lambda a, b: a + b
# # print(add(3, 4))

# # # #Lambda with Built-in Functions
# # numbers=[1,2,3] 
# # result=list(map(lambda x:x-8,numbers))
# # print(result)

# # names = ["ali", "ahmed", "sara"]
# # result1 = list(map(lambda name: name.upper(), names))
# # print(result1)

# # numbers = [1,2,3,4,5] #[2,4]
# # result2 = list(filter(lambda x: x % 2 == 0, numbers)) #
# # print(result2)

# # students = [
# #     ("Ali",90),
# #     ("Sara",70),
# #     ("Omar",95)
# # ]
# # students.sort(key=lambda student: student[1])
# # print(students)

# #Decorator
# def my_decorator(a):
#     def wrapper(name):
#         print("Before the function is called.")
#         a(name)
#         print("After the function is called.")
#     return wrapper
    
# # #with decorator
# # @my_decorator
# # def pname(name):
# #     print(name)

# # pname("Mahmoud")


# def sum2(*args):
#     res=0
#     for i in args:
#         res+=i
#     return res    
# print(sum2(6,43,6,2,48))


# # def sum1(*args):
# #     result=0
# #     for i in args:
# #         result+=i
# #     return result

# # print(sum1(2,4,6,2))
# #### args (tubles) #### important in django(views,CBV) and decorators
# #Before args
# def total(my_list):
#     result=0
#     for i in my_list:
#         result+=i
#     return result
# list1=[2,4,5,6,74,3]
# print(total(list1))    

# # #after args
# def total(*args): 
#     return sum(args)

# print(total(2,4,5,6))  


#### kwargs (dictionaries) #### 
# def user(**kwargs):
#     return kwargs.values()
# user1=user(name="Ali",age=20,city="Karachi")
# print(user1)
# user2=user(name="Seba",salary=100000)
# print(user2)
# # * important 
# def add2(a,b,c):
#     return a+b+c

# list3=[3,6,7,9]
# print(add2(*list3))

# def add2(*num):
#     return sum(num)

# list3=[3,4,6,7]
# print(add2(*list3))


## .split() method

# str="8 4 5 3 6"
# print(str.split())