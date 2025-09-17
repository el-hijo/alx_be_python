number = int(input("Enter a number to see its multiplication table: "))
for current_number in range(1,11):
    print(str(number),"*",str(current_number),"=",str(number*current_number))