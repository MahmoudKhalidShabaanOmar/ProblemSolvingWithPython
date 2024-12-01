# write a python program to get user name , and user password and make sure that password only contains alphabetic , or numeric characters , and the length of the user password is less than or equal to 8 =>
user_name = input("please enter the name of the user is : ")
user_password = input("please enter the password of the user is : ")
print("the name of the user is : \""+user_name+"\"")
print("the password of the user is : \""+user_password+"\"")
if((user_password . isalnum()) and (len(user_password) <= 8)) :
    print("HI \""+user_name+"\" , your user password is OKAY , because it contains numeric , or alphabetic characters , and the length of the user password is less than , or equal to eight , because the user password is : \""+user_password+"\" , and the length of the user password is : \""+str(len(user_password))+" characters\"")
else :
    print("SORRY \""+user_name+"\" , your user password is NOT-OKAY , because it contains numeric , or alphabetic characters , and it also contains special characters, and the length of the password is grater than eight , because the user password is : \""+user_password+"\" , and the length of the user password is : \""+str(len(user_password))+" characters\"")