# write a python program to store name , address , contact in dictionary and then update his , or her contact number at the running time by using function methods =>
# dictionary_of_user_information = {
#     "user_name" : "Mahmoud Khalid Shabaan Omar Sallam" ,
#     "user_address" : "8 Nassar Nassif Kafr El Gabal El Haram El Giza Egypt" ,
#     "user_contact_number" : input("please enter the contact number of the user is : ")
# }
# def get_dictionary_of_user_information(dict_of_user_info) :
#     print("the dictionary of the user information before updating the contact number at the running time is : "+str(dict_of_user_info))
#     dict_of_user_info . update({"user_contact_number" : input("please enter the new contact number of the user is : ")})
#     print("the dictionary of the user information after updating the contact number of the user at the running time is : "+str(dict_of_user_info))
# get_dictionary_of_user_information(dictionary_of_user_information)

def get_dictionary_of_user_information(dict_of_user_info) :
    print("the dictionary of the user information before updating the contact number of the user at the running time is : "+str(dict_of_user_info))
    dict_of_user_info . update({"user_contact_number" : input("please enter the new contact number of the user is : ")})
    return("the dictionary of the user information after updating the contact number of the user at the running time is : "+str(dict_of_user_info))
dictionary_of_user_information = {
    "user_name" : "Mahmoud Khalid Shabaan Omar Sallam" ,
    "user_address" : "8 Nassar Nassif Kafr El Gabal El Haram El giza Egypt" ,
    "user_contact_number" : input("please enter the contact number of the user is : ")
}
dictionary_of_user_info = get_dictionary_of_user_information(dictionary_of_user_information)
print(dictionary_of_user_info)