# UserProfile.py


'''
Class that will contain all the canidates
information that was obtained through the
raw input in main.py

'''
from datetime import datetime

class UserProfile:
    def __init__(self, dob, full_name, country, state, number_of_education_years, age):
        self.password = "bad_password"
        self.email = None
        self.is_active = True
        self.date_created = datetime.now()
        self.trial_expiration_date = datetime(2021, 10, 1)
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

    def create_unique_id(self):
        random_id = id(self.full_name)
        return random_id


class Developer(UserProfile):
    pass

class Designer(UserProfile):
    pass
