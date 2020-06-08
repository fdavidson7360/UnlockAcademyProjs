# UserProfile.py


'''
usr_info= {
          "dob": dobString, "full_name": full_name, "country": country,
          "state": state, "number_of_education_years": number_of_education_years,
          "age": int(age), "id": create_unique_id(full_name)
          }

'''

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

    def create_unique_id(self):
        random_id = id(self.full_name)
        return random_id
