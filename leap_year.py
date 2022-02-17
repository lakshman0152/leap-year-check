print("WELCOME !\n")
print("Check leap year \n")

user_year = int(input("Enter the year you want to check : "))

if ( (user_year%4 == 0) & ((user_year%400 == 0)|  (user_year%100 != 0 )) ):
    print(str(user_year) + " is a leap year ")
else:
    print(str(user_year) + " is not a leap year ")

print("")
print("Thank you for using this application")    