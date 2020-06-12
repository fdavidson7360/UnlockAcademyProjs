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
user_exp = int(user_exp)

usr_coding_langs = input("What languages do you know? (separate each one by a comma): ")
print("Before Split(): " + usr_coding_langs)

usr_coding_langs = usr_coding_langs.split(",")
print("After split(): " + str(usr_coding_langs))

if user_exp == 1:
    print("Expect between $40,000 and $60,000 for your level of experience")
    if len(usr_coding_langs) < 3:
        print("learn some more languages: deduct $10k from expected salary")
    elif len(usr_coding_langs) > 4:
        print("You should ask for at least $5k more to your expected salary")
elif user_exp == 2:
    print("Expect between $60,000 and $80,000 for your level of experience")
    if len(usr_coding_langs) < 3:
        print("learn some more languages: deduct $5k from expected salary")
    elif len(usr_coding_langs) > 3:
        print("You're in good shape! Don't be afraid to ask for more than the Expected Salary")
elif user_exp == 3:
    print("Expect between $80,000 and $120,000 for your level of experience")
    if len(usr_coding_langs) < 3:
        print("learn some more languages: deduct $2k from expected salary")
    elif len(usr_coding_langs) > 4:
        print("You should ask for at least $10k more to your expected salary")
elif user_exp == 4:
    print("Expect at least $130,000 for your level of experience")
    if len(usr_coding_langs) < 3:
        print("You should probably at at least one more language to your background")
else:
    print("The user entered a number outside of the 1-4 input range.")


dob = input("What's your date of birth? ")
full_name = input("What's your full name? ")
country = input("What country are you from? ")
state = input("What state are you from? ")
is_active = input("Are you an active software devloper? ")

personal_info = {"dob":dob, "full_name":full_name, "country":country ,"state":state ,"is_active":is_active}
print(personal_info)
