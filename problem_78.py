# write python program to get five year numbers from the user to store in array , and display only leap year =>
# import array as arr 
# array_of_year_numbers = arr . array("i" , [])
# array_of_year_numbers = []
# for i in range(5) :
    # array_of_year_numbers . append(int(input("please enter the year numbers is : ")))
array_of_year_numbers = [int(input("please enter the year number is : ")) for i in range(5)]
print("all year numbers in the properly(ascending) sequence is : ")
for j in range(5) :
    print(array_of_year_numbers[j])
print("only leap year number from the different year number in the properly(ascending) sequence is : ")
for k in range(5) :
    if(array_of_year_numbers[k] %4 == 0) :
        print(array_of_year_numbers[k])