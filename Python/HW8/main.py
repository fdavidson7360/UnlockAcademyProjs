"""
##### Lesson 8
# TODO:
Create a class for Developer
Create a claas for Designer
They both should inherit from UserProfile Class

# TODO:
In the Developer subclass a vaiable with a list of languages

# TODO:
In the Designer subclass add a variable with a list of software programs
i.e. adobe illustrator, adobe Photoshop, Canva, GIMP

# TODO:
-via input ask if candidate is a Developer or Designer
--if a Developer, ask what languages they know
--if a Designer, ask for software programs

-Based on if the user selected Designer or Developer, create the appropriate
object for the candidate i.e. Eliminate a direct call to UserProfile in main.py

-Modify calculate_expected_salary to to count languages or software packages
based on if candidate is a developer or designer 


"""

from UserProfile import UserProfile

valid_states= ("NY", "CA", "FL", "NC", "TX")
exp_salaries = {"NY": 70000, "CA":70000, "FL":50000, "NC":50000, "TX":60000}

#remove usr_information the dict from being passed in and passed the state directly in.

def calculate_expected_salary(num_of_exp_years, usr_information, number_of_edu_years):
    try:
        exp_sal = exp_salaries[usr_information["state"].upper()]
        number_of_education_years_as_int = int(number_of_edu_years)
    except KeyError:
        print("******** INPUT ERROR: Please enter a valid state ********")
    except ValueError:
        print("******** INPUT ERROR: Please enter a valid number for years of learning experience *********")
    except Exception:
        print("Sometthing went wrong. Please Refresh or contact support: help@unlock.academy")
    else: #this else olny gets executed if the exception is not raised/called

        new_exp_sal = 0

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



create_a_candidate = True
while create_a_candidate == True:
    try:
        user_exp = input("How many years experience do you have developing software? \n"
                        "[1] Less than a year \n"
                        "[2] 1-3 years of experience \n"
                        "[3] 3-8 years of experience \n"
                        "[4] 8+ years of experience \n")
        print("\n")

        user_exp = int(user_exp)
        if user_exp > 4 or user_exp < 1:
            print("****The user entered a number outside of the 1-5 input range.*****")

        usr_coding_langs = input("What languages do you know? (separate each one by a comma): ")
        if usr_coding_langs == '':
            raise ValueError
        usr_coding_langs = usr_coding_langs.split(",")
        print("\n")

        dob_input = input("Please enter you Date of Birth (MM/DD/YYYY): ")
        convert = dob_input.split('/')
        monthDict = {
                      1:"January", 2:"February", 3:"March",
                      4:"April", 5:"May", 6:"June",
                      7:"July", 8:"August", 9:"September",
                      10:"October", 11:"November", 12:"December"
                   }
        monthIndex = int(convert[0])
        dob_month = monthDict[monthIndex]

        dob_day = convert[1]
        dob_year = convert[2]

        dobString = str(dob_month) + ", "  + str(dob_day) + ", " + str(dob_year)
        #print ("DobConvertedOutput: " + dobString)
        print("\n")

        full_name = input("Please enter your Full Name: ")

        #userOneId = id(full_name)
        #print("Username: " + full_name + " Id #: " + str(userOneId))
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

        number_of_education_years = input("Please enter the number of years you have been learning to code: ")
        print("\n")

        usr_info= {
                  "dob": dobString, "full_name": full_name, "country": country,
                  "state": state, "number_of_education_years": number_of_education_years,
                  "age": int(age)
                  }

        #Instantiating an object aka create a new instance of the Class
        user_profile = UserProfile(dobString, full_name, country, state , number_of_education_years, int(age))

        user_password = user_profile.get_password()         #this will contain default password
        print("Your initial password was: ", user_password) #output of default password
        print("\n")

        new_password = input("Enter a new password: ")   #this will take user input for password
        print("\n")

        user_profile.set_password(new_password)      #this will set the value of new password in class
        user_password = user_profile.get_password()  # this will retrieve the new user input for password
        print("Your new password is: ", user_password) # output of new password
        print("\n")

        user_id = user_profile.create_unique_id()
        print("Your confirmation Id is ", user_id)
        print("\n")

        calculate_expected_salary(user_exp, usr_info, number_of_education_years)

        another_candidate = input("Would you like to create another candidate? Y/N: ")

        if another_candidate == "Y":
            create_a_candidate = True
        else:
            create_a_candidate = False
            #break another solution to break the loop
    except ValueError:
        print("\n**********Please enter all valid values only************\n")

print("Thank you for sharing this information. We will be in touch.")
