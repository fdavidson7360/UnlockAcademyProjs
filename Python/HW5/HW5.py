"""
##### Lesson 5
Write a function to hold repetitious code chunks i.e. try block after user_exp

"""

valid_states= ("NY", "CA", "FL", "NC", "TX")
exp_salaries = {"NY": 70000, "CA":70000, "FL":50000, "NC":50000, "TX":60000}

def calculate_expected_salary(num_of_exp_years, usr_information, number_of_edu_years):
    try:
        exp_sal = exp_salaries[usr_information["state"].upper()]
        number_of_education_years_as_int = int(number_of_edu_years)
    except KeyError:
        print("******** INPUT ERROR: Please enter a valid state ********")
    except ValueError:
        print("******** INPUT ERROR: Please enter a valid number for years of learning experience *********")
    else: #this else olny gets executed if the exception is not raised/called

        if num_of_exp_years == 1:
            new_exp_sal = exp_sal - 5000 #Deduct $5k because the user only has one year of experience
        elif num_of_exp_years == 2:
            new_exp_sal = exp_sal - 3000 #Deduct $3k because the user only has 2 years of experience
        elif num_of_exp_years == 3:
            new_exp_sal = exp_sal + 1000 #Add 1k because they have 3yrs of experience
        elif num_of_exp_years == 4:
            new_exp_sal = exp_sal + 5000 #Add 5k because the user has 4+ yrs of experience
        else:
            print(10 * "*" + "Sorry. Please enter one of the valid options" + 10 * "*")


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

        dob_input = input("Please enter you Date of Birth (MM/DD/YYYY): \n")
        convert = dob_input.split('/')
        monthDict = {1:"January", 2:"February", 3:"March",
                  4:"April", 5:"May", 6:"June",
                  7:"July", 8:"August", 9:"September",
                  10:"October", 11:"November", 12:"December"}
        monthIndex = int(convert[0])
        dob_month = monthDict[monthIndex]

        dob_day = convert[1]
        dob_year = convert[2]

        dobString = str(dob_month) + ", "  + str(dob_day) + ", " + str(dob_year)
        print ("DobConvertedOutput: " + dobString)
        print("\n")

        full_name = input("Please enter your Full Name: \n")

        userOneId = id(full_name)
        print("Username: " + full_name + " Id #: " + str(userOneId))
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

        usr_info={"dob": dobString, "full_name":full_name, "country":country, "state":state,
                  "number_of_education_years":number_of_education_years, "age":int(age)}
        break
    except ValueError:
        print("\n**********Please enter all valid values only************\n")

calculate_expected_salary(user_exp, usr_info, number_of_education_years)


"""
I'm going to give you 3 built-in variables. Use them in your code base:

isinstance
id()
split()


Examples of what you could do:
Give each user a unique id
Convert the date of birth format from MM/DD/YYYY to "Month Day, Year"


Input : 01/01/2020
Output : January 01, 2020

"""
