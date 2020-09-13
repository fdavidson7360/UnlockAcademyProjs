# ##main.py
"""
##### Lesson 11
# TODO:
Convert the user date of birth (dob) to a date object. Format it as mm/dd/yyyy.

Store the dob datetime object to the UserProfile class

"""

from datetime import date, datetime, time
from datetime import *
from Lesson11.Models import Developer, Designer


# valid_candidate = ("Developer", "Designer")
valid_states = ("NY", "CA", "FL", "NC", "TX")
exp_salaries = {"NY": 70000, "CA": 70000, "FL": 50000, "NC": 50000, "TX": 60000}

# remove usr_information the dict from being passed in and passed the state directly in.


def calculate_expected_salary(num_of_exp_years, usr_information, number_of_edu_years,
                              is_developer, is_designer):
    try:
        exp_sal = exp_salaries[usr_information["state"].upper()]
        number_of_education_years_as_int = int(number_of_edu_years)
    except KeyError:
        print("******** INPUT ERROR: Please enter a valid state ********")
    except ValueError:
        print("******** INPUT ERROR: Please enter a valid number for years of learning experience *********")
    except Exception:
        print("Something went wrong. Please Refresh or contact support: help@unlock.academy")
    else:  # this else only gets executed if the exception is not raised/called

        new_exp_sal = 0

        if num_of_exp_years == 1:
            new_exp_sal = exp_sal - 5000  # Deduct $5k because the user only has one year of experience
        elif num_of_exp_years == 2:
            new_exp_sal = exp_sal - 3000  # Deduct $3k because the user only has 2 years of experience
        elif num_of_exp_years == 3:
            new_exp_sal = exp_sal + 1000  # Add 1k because they have 3yrs of experience
        elif num_of_exp_years == 4:
            new_exp_sal = exp_sal + 5000  # Add 5k because the user has 4+ yrs of experience
        else:
            print(10 * "*" + "Sorry. Please enter one of the valid options" + 10 * "*")

        if is_developer == True:
            if len(usr_coding_langs) < 3:
                new_exp_sal = new_exp_sal - 10000
                print("learn some more languages: $10k deducted from expected salary")

            elif len(usr_coding_langs) > 3:
                new_exp_sal = new_exp_sal + 10000
                print("$10k added to your expected salary")
            else:
                new_exp_sal = new_exp_sal + 5000

        if is_designer == True:
            if len(sw_pkgs) < 3:
                new_exp_sal = new_exp_sal - 10000
                print("learn some more design tools: $10k deducted from expected salary")

            elif len(sw_pkgs) > 3:
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
            print("Your starting salary living in " + state + " --> " + "could have been $ " + str(salary) + "\n")


create_a_candidate = True

# Added after watching solution video
is_developer = False
is_designer = False

while create_a_candidate == True:
    try:
        candidate_type = input("What is your profession \nType '1' if a Developer \nType '2' if a Designer\n")

        if int(candidate_type) == 1:
            is_developer = True
            is_designer = False

            user_exp = input("How many years experience do you have developing software? \n"
                             "[1] Less than a year \n"
                             "[2] 1-3 years of experience \n"
                             "[3] 3-8 years of experience \n"
                             "[4] 8+ years of experience \n")
            print("\n")


        elif int(candidate_type) == 2:
            is_developer = False
            is_designer = True

            user_exp = input("How many years experience do you have designing? \n"
                             "[1] Less than a year \n"
                             "[2] 1-3 years of experience \n"
                             "[3] 3-8 years of experience \n"
                             "[4] 8+ years of experience \n")

        else:
            raise ValueError

        user_exp = int(user_exp)
        if user_exp > 4 or user_exp < 1:
            print("****The user entered a number outside of the 1-5 input range.*****")

        if is_developer:
            usr_coding_langs = input("What languages do you know? (separate each one by a comma): \n")
            if usr_coding_langs == '':
                raise ValueError
            usr_coding_langs = usr_coding_langs.split(",")
            print("\n")

        else:
            sw_pkgs = input("What software packages do you know?"
                            "e.g.) Adobe Photoshop, Adobe Illustrator, Canva, GIMP"
                            " (separate each one by a comma): \n")
            if sw_pkgs == '':
                raise ValueError
            sw_pkgs = sw_pkgs.split(",")
            print("\n")

        dob_input = input("Please enter you Date of Birth (MM/DD/YYYY): ")

        # Converts a string into a datetime object output: yyyy/mm/dd
        dob_obj = datetime.strptime(dob_input, "%m/%d/%Y")

        # Formats the new datetime object to output: mm/dd/yyyy
        date_ftmd = dob_obj.strftime("%m/%d/%Y")

        print("\n")

        full_name = input("Please enter your Full Name: ")

        print("\n")

        age = input("Enter your age: ")
        print("\n")
        age = int(age)

        country = input("Please enter the country you reside in: ")
        print("\n")

        if len(country) > 3:
            raise ValueError

        for state in valid_states:
            print(state)

        state = input("Choose your State (use the two letter abbr.): ")
        print("\n")
        if len(state) > 2:
            raise ValueError

        is_active = True

        number_of_education_years = input("Please enter the number of years you have been learning this skill set: ")
        print("\n")

        usr_info = {
                  "dob": date_ftmd, "full_name": full_name, "country": country,
                  "state": state, "number_of_education_years": number_of_education_years,
                  "age": int(age)
                  }

        # Instantiating a Developer class
        if is_developer:
            user_profile = Developer(date_ftmd, full_name, country, state, number_of_education_years, age,
                                     usr_coding_langs)

        elif is_designer:
            user_profile = Designer(date_ftmd, full_name, country, state, number_of_education_years, age, sw_pkgs)

        user_password = user_profile.get_password()  # this will contain default password
        print("Your initial password was: ", user_password)  # output of default password
        print("\n")

        new_password = input("Enter a new password: ")  # this will take user input for password
        print("\n")

        user_profile.set_password(new_password)  # this will set the value of new password in class
        user_password = user_profile.get_password()  # this will retrieve the new user input for password
        print("Your new password is: ", user_password)  # output of new password
        print("\n")

        user_id = user_profile.create_unique_id()
        print("Your confirmation Id is ", user_id)
        print("\n")

        calculate_expected_salary(user_exp, usr_info, number_of_education_years,
                                  is_developer, is_designer)

        another_candidate = input("Would you like to create another candidate? Y/N: \n")

        if another_candidate == "Y":
            create_a_candidate = True
        else:
            create_a_candidate = False
            # break another solution to break the loop
    except ValueError:
        print("\n**********Please enter all valid values only************\n")

print("Thank you for sharing this information. We will be in touch.")
