# ask the user to input their experience by asking them a question using the input() function

# use an if/elif/else statement to check if the user chose option 1, 2, 3 or 4
# if the user chose option 1, print out 'Expect between $40,000 and $60,000 for your level of experience'
# else if the user chose option 2, print out 'Expect between $60,000 and $80,000 for your level of experience'
# else if the user chose option 3, print out 'Expect between $80,000 and $120,000 for your level of experience'
# else if the user chose option 4, print out 'Expect at least $130,000 for your level of experience'

user_exp = input("How many years experience do you have developing software?\n"
                "[1]Less than a year\n"
                "[2]1-3 years of experience \n[3] 3-8 years of experience\n"
                "[4] 8+ years of experience\n")

if int(user_exp) == 1:
    print("Expect between $40,000 and $60,000 for your level of experience")

elif int(user_exp) == 2:
    print("Expect between $60,000 and $80,000 for your level of experience")

elif int(user_exp) == 3:
    print("Expect between $80,000 and $120,000 for your level of experience")

elif int(user_exp) == 4:
    print("Expect at least $130,000 for your level of experience")

else:
    print("The user entered a number outside of the 1-4 input range.")
