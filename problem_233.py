# write a python program to create a file with extension .txt to get two numbers from the user , and then get the sum of the two numbers => 
createFile = open("sumOfTwoNumbers.txt" , "w+")
frist_number = int(input("please enter the frist number is = "))
createFile . write("the frist number is = "+str(frist_number)+"\n")
second_number = int(input("please enter the second number is = "))
createFile . write("the second number is = "+str(second_number)+"\n")
sum_of_two_numbers = frist_number + second_number 
createFile . write("the sum of the frist number , and second number is = "+str(sum_of_two_numbers)+"\n")
createFile . close()