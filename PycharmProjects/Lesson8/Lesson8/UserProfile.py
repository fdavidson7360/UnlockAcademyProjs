# ###UserProfile.Py
# LESSON 8: UserProfile.py
# Class Inheritance


class UserProfile:
    def __init__(self, dob, full_name, country, state, number_of_education_years, age):
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
        return self.password

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def set_email(self, new_email):
        self.email = new_email
        return self.email

    def create_unique_id(self):
        random_id = id(self.full_name)
        return random_id


class Developer(UserProfile):
    def __init__(self, dob, full_name, country, state, number_of_education_years, age, usr_coding_langs):
        super().__init__(dob, full_name, country, state, number_of_education_years, age)
        self.coding_langs = usr_coding_langs

    # Added after watching solution video
    def get_coding_langs(self):
        return self.coding_langs

    # Added after watching solution video
    def set_coding_langs(self, new_coding_langs):
        self.coding_langs = new_coding_langs


class Designer(UserProfile):
    def __init__(self, dob, full_name, country, state, number_of_education_years, age, sw_pkgs):
        super().__init__(dob, full_name, country, state, number_of_education_years, age)
        self.sw_pkgs = sw_pkgs

    # Added after watching solution video
    def get_sw_pkgs(self):
        return self.sw_pkgs

    # Added after watching solution video
    def set_sw_pkgs(self, new_sw_pkgs):
        self.sw_pkgs = new_sw_pkgs


# TODO:
"""
Create a subclass for Developer
Create a subclass for Designer
They both should inherit from
"""

# TODO:
"""
Add a variable/property to the Developer Sublass: a list of languages
"""

# TODO:
"""
Add a variable/property to the Designer Subclass: a list of software programs
e.g.) adobe illustrator, adobe Photo Shop, Canva, GIMP
"""

#  TODO:
"""
-Ask the user (via input) if this candidate is a designer or a developer
- If a designer, ask for software programs
- If a developer, ask what languages they know ( we already have this code. Now update to
ask given the condition that the candidate is a developer


-Based on if the user selected a Designer or Developer, create the appropriate object
for the candidate. So don't call the UserProfile class directly from main.py


-In calculate_expected_salary function, we need to check if this is a designer or a developer
so we know if we should be counting languages or software programs   
"""