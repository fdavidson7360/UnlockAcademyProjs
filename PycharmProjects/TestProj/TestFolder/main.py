class UserProfile:
    def __init__(self, dob, full_name, country, state, number_of_education_years, age, ):
        self.password = "bad_password"
        self.email = None
        self.is_active = True

        self.dob = dob
        self.full_name = full_name
        self.country = country
        self.state = state
        self.number_of_education_years = number_of_education_years
        self.age = age

    def get_age(self):
        return self.age

    def set_password(self, new_password):
        self.password = new_password
        #TODO: self.password needs to be returned here

    def get_password(self):
        return self.password

    def user_id_number(self):
        user_id = id(self.full_name)
        return user_id


valid_states = ("FL", "NY", "CA", "TX", "NC")

expected_salaries = {"NY": 70000, "CA": 70000, "FL": 50000, "NC": 50000, "TX": 60000}


def calculate_expected_salary(number_of_experience_years, user_information, number_of_edu_years, ):
    try:
        # The red line at user_info should be updated to the variable user_information that's
        # in the function argument list
        expected_salary = expected_salaries[user_info["state"].upper()]
        number_of_education_years_as_int = int(number_of_edu_years)

    except KeyError:
        print("Please Enter A Valid State")
    except ValueError:
        print("Please Enter A Valid Number For Learning Experience")
        # TODO: possibly move the else statement from line 57 to here then give
        # new_expected_salary an initial value this will remove red lines from 63, 66, 68
        if number_of_experience_years == 1:
            new_expected_salary = expected_salary - 5000

        elif number_of_experience_years == 2:
            new_expected_salary = expected_salary - 3000

        elif number_of_experience_years == 3:
            new_expected_salary = expected_salary + 1000

        elif number_of_experience_years == 4:
            new_expected_salary = expected_salary + 5000
        else:
            print("Sorry. Please enter a valid option.")
    else:

        if len(user_coding_languages) < 3:
            new_expected_salary = new_expected_salary - 10000
            print("Please learn more languages. $10K deducted from salary.")
        elif len(user_coding_languages) > 3:
            new_expected_salary = new_expected_salary + 10000
        else:
            new_expected_salary = new_expected_salary + 5000
        if number_of_education_years_as_int > 3:
            new_expected_salary = new_expected_salary + 5000
        else:
            new_expected_salary = new_expected_salary - 5000

        print("Expect $" + str(new_expected_salary) + "for your level of experience")
        for state in expected_salaries:
            salary = expected_salaries[state]
            print("Your starting salary living in" + state + "could have been $" + str(salary) + ".")


while True:
    try:
        users_experience = input("How many years do you have developing software?\n[1] 1-3 years\n""[2] 4-6 years\n"
                                 "[3]7-10 years\n[4] 10+ years of experience\n")

        users_experience = int(users_experience)

        user_coding_languages = input("Which coding languages do you know? (separate each with a comma.)\n")
        if user_coding_languages == '':
            raise ValueError
        user_coding_languages = user_coding_languages.split(',')

        dob = input("Please enter your date of birth (MM/DD/YYYY)\n")

        full_name = input("Please enter your Full Name:\n")

        age = input("Please enter your current age:\n")
        age = int(age)

        country = input("Please enter the country you reside:\n")

        for state in valid_states:
            print(state)

        state = input("Choose your state using the appropriate abbreviations:\n")
        if len(state) > 2:
            raise ValueError

        number_of_education_years = input("Please enter the number of years you have been learning to code:\n")
        is_active = True

        user_profile = UserProfile(dob, full_name, country, state, number_of_education_years, age)

        user_password = user_profile.get_password()
        print("Your initial password was", user_password)

        new_password = input("enter a new password\n")

        user_profile.set_password("good_password")

        print("Your new password is", new_password)

        user_password = user_profile.get_password()

        user_id = user_profile.user_id_number()

        print("Your Unique Id is", user_id)

        # user_info = {
        #               "dob": dob, "full_name": full_name, "country": country, "state": state, "is_active": is_active,
        #                "number_of_education_years": number_of_education_years, "age": age, "id": user_id(full_name)
        #          }
        # Instantiating an Object aka create a new instance of the class

        break
    except ValueError:
        print("Please enter all valid values")

# calculate_expected_salary(users_experience, user_info, number_of_education_years)