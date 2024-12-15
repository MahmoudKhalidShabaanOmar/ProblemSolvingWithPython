# write a python program to get number from the user , and then get the square of the number by using function methods =>
# number = int(input("please enter the number is = "))
# def get_square_of_num(num) :
#     print("the number is = "+str(num))
#     # square_of_num = num * num 
#     # square_of_num = num ** 2
#     square_of_num = pow(num , 2)
#     print("the square of the number is = "+str(square_of_num))
# get_square_of_num(number)

# def get_square_of_num(num , square_of_num ) :
#     print("the number is = "+str(num))
#     return("the square of the number is = "+str(square_of_num))
# number = int(input("please enter the number is = "))
# # square_of_num = num * num 
# # square_of_num = num ** 2
# square_of_number = pow(num , 2)
# square_of_number = get_square_of_num(number , square_of_num)
# print(square_of_number)

# number = int(input("please enter the number is = "))
# def get_square_of_num(num) :
#     print("the number is = ")
#     if(num > 0) :
#         # square_of_num = num * num 
#         # square_of_num = num ** 2
#         square_of_num = pow(num , 2)
#         print("the square of the number is = "+str(square_of_num))
#     else:
#         print("there is no square of the number , because your entered number is = "+str(num))
# get_square_of_num(number)

def get_square_of_num(num , square_of_num) :
    print("the number is = "+str(num))
    if(num > 0) :
        return("the square of the number is = "+str(square_of_num))
    else :
        return("there is no square of the number is , because your entered number is = "+str(num))
number = int(input("please enter the number is = "))
# square_of_number = number * number
# square_of_number = number ** 2
square_of_number = pow(number , 2)
square_of_number = get_square_of_num(number , square_of_number)
print(square_of_number)
