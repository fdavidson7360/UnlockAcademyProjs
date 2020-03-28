# ask the user to input their experience by asking them a question using the input() function

# use an if/elif/else statement to check if the user chose option 1, 2, 3 or 4
# if the user chose option 1, print out 'Expect between $40,000 and $60,000 for your level of experience'
# else if the user chose option 2, print out 'Expect between $60,000 and $80,000 for your level of experience'
# else if the user chose option 3, print out 'Expect between $80,000 and $120,000 for your level of experience'
# else if the user chose option 4, print out 'Expect at least $130,000 for your level of experience'

valid_states= ("NY", "CA", "FL", "NC", "TX")
exp_salaries = {"NY": 70000, "CA":70000, "FL":50000, "NC":50000, "TX":60000}
while True:
    try:
        user_exp = input("How many years experience do you have developing software? \n"
                        "[1] Less than a year \n"
                        "[2] 1-3 years of experience \n"
                        "[3] 3-8 years of experience \n"
                        "[4] 3-5 years of experience \n"
                        "[5] 5+ years of experience \n")

        user_exp = int(user_exp)
        if user_exp > 5 or user_exp < 1:
            print("****The user entered a number outside of the 1-5 input range.*****")

        usr_coding_langs = input("What languages do you know? (separate each one by a comma): ")
        if usr_coding_langs == '':
            raise ValueError
        usr_coding_langs = usr_coding_langs.split(",")
        print("\n")

        dob = input("Please enter you Date of Birth (MM/DD/YYYY): \n")
        print("\n")
        full_name = input("Please enter your Full Name: \n")
        print("\n")

        age = input("Enter your age \n")
        age = int(age)

        country = input("Please enter the country you reside in:\n")
        print("\n")

        if len(country) > 3:
            raise ValueError

        for state in valid_states:
            print(state)

        state = input("Choose your State (use the two letter abbr.): \n")

        if len(state) > 2:
            raise ValueError

        is_active = True

        number_of_education_years = input("Please enter the number of years you have been learning to code: \n")

        usr_info={"dob":dob, "full_name":full_name, "country":country, "state":state,
                  "number_of_education_years":number_of_education_years, "age":int(age)}
        break
    except ValueError:
        print("\n**********Please enter all valid values only************\n")

if user_exp == 1:
    try:
        exp_sal = exp_salaries[usr_info["state"].upper()]
        number_of_education_years_as_int = int(number_of_education_years)
    except KeyError:
        print("******** INPUT ERROR: Please enter a valid state ********")
    except ValueError:
        print("******** INPUT ERROR: Please enter a valid number for years of learning experience *********")
    else:
        new_exp_sal = exp_sal - 5000

        if len(usr_coding_langs) < 3:
            new_exp_sal = new_exp_sal - 10000
            print("learn some more languages: $10k deducted from expected salary")

        elif len(usr_coding_langs) > 3:
            new_exp_sal = new_exp_sal + 10000
            print("$10k added to your expected salary")
        else:
            new_exp_sal = new_exp_sal + 5000

        if int(number_of_education_years_as_int) > 3:
            new_exp_sal = new_exp_sal + 5000
        else:
            new_exp_sal = new_exp_sal - 5000

        print("Expect $" + str(new_exp_sal) + " for your level of experience")

elif user_exp == 2:
    try:
        exp_sal = exp_salaries[usr_info["state"].upper()]
        number_of_education_years_as_int = int(number_of_education_years)
    except KeyError:
        print("******** INPUT ERROR: Please enter a valid state ********")
    except ValueError:
        print("******** INPUT ERROR: Please enter a valid number for years of learning experience *********")
    else:
        new_exp_sal = exp_sal - 4000

        if len(usr_coding_langs) < 3:
            new_exp_sal = new_exp_sal - 10000
            print("learn some more languages: $10k deducted from expected salary")

        elif len(usr_coding_langs) > 3:
            new_exp_sal = new_exp_sal + 10000
            print("$10k added to your expected salary")
        else:
            new_exp_sal = new_exp_sal + 5000

        if int(number_of_education_years_as_int) > 3:
            new_exp_sal = new_exp_sal + 5000
        else:
            new_exp_sal = new_exp_sal - 5000

        print("Expect $" + str(new_exp_sal) + " for your level of experience")

elif user_exp == 3:
    try:
        exp_sal = exp_salaries[usr_info["state"].upper()]
        number_of_education_years_as_int = int(number_of_education_years)
    except KeyError:
        print("******** INPUT ERROR: Please enter a valid state ********")
    except ValueError:
        print("******** INPUT ERROR: Please enter a valid number for years of learning experience *********")
    else:
        new_exp_sal = exp_sal - 3000

        if len(usr_coding_langs) < 3:
            new_exp_sal = new_exp_sal - 10000
            print("learn some more languages: $10k deducted from expected salary")

        elif len(usr_coding_langs) > 3:
            new_exp_sal = new_exp_sal + 10000
            print("$10k added to your expected salary")
        else:
            new_exp_sal = new_exp_sal + 5000

        if int(number_of_education_years_as_int) > 3:
            new_exp_sal = new_exp_sal + 5000
        else:
            new_exp_sal = new_exp_sal - 5000

        print("Expect $" + str(new_exp_sal) + " for your level of experience")
elif user_exp == 4:
    try:
        exp_sal = exp_salaries[usr_info["state"].upper()]
        number_of_education_years_as_int = int(number_of_education_years)
    except KeyError:
        print("******** INPUT ERROR: Please enter a valid state ********")
    except ValueError:
        print("******** INPUT ERROR: Please enter a valid number for years of learning experience *********")
    else:
        new_exp_sal = exp_sal - 2000

        if len(usr_coding_langs) < 3:
            new_exp_sal = new_exp_sal - 10000
            print("learn some more languages: $10k deducted from expected salary")

        elif len(usr_coding_langs) > 3:
            new_exp_sal = new_exp_sal + 10000
            print("$10k added to your expected salary")
        else:
            new_exp_sal = new_exp_sal + 5000

        if int(number_of_education_years_as_int) > 3:
            new_exp_sal = new_exp_sal + 5000
        else:
            new_exp_sal = new_exp_sal - 5000

        print("Expect $" + str(new_exp_sal) + " for your level of experience")
elif user_exp == 5:
    try:
        exp_sal = exp_salaries[usr_info["state"].upper()]
        number_of_education_years_as_int = int(number_of_education_years)
    except KeyError:
        print("******** INPUT ERROR: Please enter a valid state ********")
    except ValueError:
        print("******** INPUT ERROR: Please enter a valid number for years of learning experience *********")
    else:
        new_exp_sal = exp_sal - 1000

        if len(usr_coding_langs) < 3:
            new_exp_sal = new_exp_sal - 10000
            print("learn some more languages: $10k deducted from expected salary")

        elif len(usr_coding_langs) > 3:
            new_exp_sal = new_exp_sal + 10000
            print("$10k added to your expected salary")
        else:
            new_exp_sal = new_exp_sal + 5000

        if int(number_of_education_years_as_int) > 3:
            new_exp_sal = new_exp_sal + 5000
        else:
            new_exp_sal = new_exp_sal - 5000

        print("Expect $" + str(new_exp_sal) + " for your level of experience")
else:
    print("The user entered a number outside of the 1-5 input range.")
