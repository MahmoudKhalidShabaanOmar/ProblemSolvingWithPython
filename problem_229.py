# write a python program to get six identify numbers of students as input and display in descending order =>
# # lista_of_student_identify_numbers = []
# # for i in range(6) :
# #     number_of_identify = int(input("please enter the number of the identify of the student is : "))
# #     lista_of_student_identify_numbers. append(number_of_identify)
# lista_of_student_identify_numbers = [int(input("please enter the number of the identify of the student is : ")) for i in range(6)]
# print("the list of the different identify numbers is : "+str(lista_of_student_identify_numbers))
# for j in lista_of_student_identify_numbers :
#     print(j)
# lista_of_student_identify_numbers . sort(reverse = True) 
# print("the reversing(descending) sequecne of the list of the student identify numbers is : "+str(lista_of_student_identify_numbers))
# for k in lista_of_student_identify_numbers : 
#     print(k)

# lista_of_student_identify_numbers = []
# for i in range(6) :
#     number_of_identify = int(input("please enter the different number of the identify of the student is : "))
#     lista_of_student_identify_numbers . append(number_of_identify)
lista_of_student_identify_numbers = [int(input("please enter the identify numbers of the student is : ")) for i in range(6)]
print("the list of the different identify numbers of the student is : "+str(lista_of_student_identify_numbers))
for j in lista_of_student_identify_numbers :
    print(j)
lista_of_student_identify_numbers . reverse()
print("the reversing (descending) sequence of the list of the different identify of the student is : "+str(lista_of_student_identify_numbers))
for k in lista_of_student_identify_numbers : 
    print(k)