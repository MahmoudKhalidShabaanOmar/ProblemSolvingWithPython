# write a python program to get user biography description , and then display the count of the total characters , and length of the specific words of the user biography description by using different function methods =>
# user_biography_description = input("please enter the user biography description is : ")
# def get_user_biography_description(user_bio_desc) :
#     print("the user biography description is : \""+user_bio_desc+"\"")
#     print("the total characters of the user biography description is = \""+str(len(user_bio_desc))+" characters\"")
#     user_bio_desc_lista = user_bio_desc . split()
#     print("the user biography description list is : "+str(user_bio_desc_lista))
#     print("the total specific words of the user biography description list is = "+str(len(user_bio_desc_lista))+" words")
# get_user_biography_description(user_biography_description)

def get_user_biography_description(user_bio_desc) :
    print("the user biography description is : \""+user_bio_desc+"\"") 
    print("the total characters of the user biography description is = \""+str(len(user_bio_desc))+" characters\"")
    user_bio_desc_lista = user_bio_desc . split()
    print("the user biography description list is : "+str(len(user_bio_desc_lista)))
    return("the length of the words of the user biograohy description list is = "+str(len(user_bio_desc_lista))+" words")
user_biography_description = input("please enter the user biography description is : ")
bio = get_user_biography_description(user_biography_description)
print(bio)