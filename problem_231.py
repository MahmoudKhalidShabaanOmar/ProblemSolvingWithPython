# write a python program that accepts six identify numbers of students , clear the list item , and make use of empty method to check it has been empty , or not empty =>
# def isEmptyList(lista) :
#     return not lista
# # lista_of_different_elements = []
# # for i in range(5) :
# #     lista_of_different_elements . append(input("please enter the different elements to store in the list of the different elements is : "))
# lista_of_different_elements = [input("please enter the different elements to store in the list of the different elements is : ") for i in range(5)]
# print("the list of the different elements is : "+str(lista_of_different_elements))
# lista_of_different_elements . clear()
# print("the list of the different elements after clearing all different elements is : "+str(lista_of_different_elements))
# if(isEmptyList(lista_of_different_elements)) :
#     print("it is empty list")
# else :
#     print("it is not empty list")

# def isEmptyList(lista) :
#     return len(lista) == 0
# # lista_of_different_elements = []
# # for i in range(5) :
# #     lista_of_different_elements . append(input("please enter the different elements to store in the list of the different elements is : "))
# lista_of_different_elements = [input("please enter the different elements to store in the list of the different elements is : ") for i in range(5)]
# print("the list of the different elements is : "+str(lista_of_different_elements))
# lista_of_different_elements . clear()
# print("the list of the different elements after clearing all elements from the list of the different elements is : "+str(lista_of_different_elements))
# if(isEmptyList(lista_of_different_elements)) :
#     print("it is empty list")
# else :
#     print("it is not empty list")

lista_of_different_elements = []    
for i in range(5) :
    lista_of_different_elements . append(input("please enter the different elements to store in the list of the different elements is : "))
print("the list of the different elements is : "+str(lista_of_different_elements))
lista_of_different_elements . clear()
print("the list of the different elements inside the list of the different elements after clearing all elements is : "+str(lista_of_different_elements))
if(not lista_of_different_elements) :
    print("it is empty")
else :
    print("it is not empty")