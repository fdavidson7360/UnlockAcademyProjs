"""
##### Lesson 4
Using a For or a While Loop, write the code that will loop over the exp_salaries dictionary
and print out the state they chose.
The message should be printed to the console at the end of the progam and should read:
"Your expected Salary living in key(the state they chose) could have been $ value(the base salary)"

Check to see if the user entered a valid number for a number_of_education_years. If not, raise a value error

"""

valid_states= ("NY", "CA", "FL", "NC", "TX")
exp_salaries = {"NY": 70000, "CA":70000, "FL":50000, "NC":50000, "TX":60000}
while True:
    try:
        user_exp = input("How many years experience do you have developing software? \n"
                        "[1] Less than a year \n"
                        "[2] 1-3 years of experience \n"
                        "[3] 3-8 years of experience \n"
                        "[4] 8+ years of experience \n")

        user_exp = int(user_exp)
        if user_exp > 4 or user_exp < 1:
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

        print("Expect $" + str(new_exp_sal) + " for your level of experience\n")

        for state in exp_salaries:
            salary = exp_salaries[state]
            print("Your starting salary living in "+ state + " --> " + "could have been $" + str(salary) +"\n")

elif user_exp == 2:
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

        for key in exp_salaries:
            print("Your starting salary living in "+ str(key) + " --> " + "could have been $" + str(exp_salaries[key]) +"\n")

elif user_exp == 3:
    try:
        exp_sal = exp_salaries[usr_info["state"].upper()]
        number_of_education_years_as_int = int(number_of_education_years)
    except KeyError:
        print("******** INPUT ERROR: Please enter a valid state ********")
    except ValueError:
        print("******** INPUT ERROR: Please enter a valid number for years of learning experience *********")
    else:
        new_exp_sal = exp_sal + 1000 #Add 1k because they have 3yrs of experience

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

        for key in exp_salaries:
            print("Your starting salary living in "+ str(key) + " --> " + "could have been $" + str(exp_salaries[key]) +"\n")

elif user_exp == 4:
    try:
        exp_sal = exp_salaries[usr_info["state"].upper()]
        number_of_education_years_as_int = int(number_of_education_years)
    except KeyError:
        print("******** INPUT ERROR: Please enter a valid state ********")
    except ValueError:
        print("******** INPUT ERROR: Please enter a valid number for years of learning experience *********")
    else:
        new_exp_sal = exp_sal + 5000 #Add 5k because the user has 4+ yrs of experience

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

        for key in exp_salaries:
            print("Your starting salary living in "+ str(key) + " --> " + "could have been $" + str(exp_salaries[key]) +"\n")


else:
    print(10 * "*" + "Sorry. Please enter one of the valid options" + 10 * "*")
