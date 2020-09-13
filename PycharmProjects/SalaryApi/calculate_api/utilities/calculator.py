
valid_states = ("NY", "CA", "FL", "NC", "TX")
exp_salaries = {"NY": 70000, "CA": 70000, "FL": 50000, "NC": 50000, "TX": 60000}


def calculate_expected_salary(num_of_exp_years, usr_information, number_of_edu_years,
                              is_developer, is_designer, usr_coding_langs, sw_pkgs):
    try:
        exp_sal = exp_salaries[usr_information["state"].upper()]
        number_of_education_years_as_int = int(number_of_edu_years)
    except KeyError:
        return "******** INPUT ERROR: Please enter a valid state ********"
    except ValueError:
        return "******** INPUT ERROR: Please enter a valid number for years of learning experience *********"
    except Exception:
        return "Something went wrong. Please Refresh or contact support: help@unlock.academy"
    else:  # this else only gets executed if the exception is not raised/called

        output = {
            "Tally_msg": list(),
            "res": list()
            # "Result_msg": ""
        }
        new_exp_sal = 0

        if num_of_exp_years == 1:
            new_exp_sal = exp_sal - 5000
            output["Tally_msg"].append("Deduct $5k because the user only has one year of experience")
        elif num_of_exp_years == 2:
            new_exp_sal = exp_sal - 3000
            output["Tally_msg"].append("Deduct $3k because the user only has 2 years of experience")
        elif num_of_exp_years == 3:
            new_exp_sal = exp_sal + 1000
            output["Tally_msg"].append("Add 1k because they have 3yrs of experience")
        elif num_of_exp_years == 4:
            new_exp_sal = exp_sal + 5000
            output["Tally_msg"].append("Add 5k because the user has 4+ yrs of experience")
        else:
            return 10 * "*" + "Sorry. Please enter one of the valid options [number of " \
                                                          "experience years]" + 10 * "*"


        if is_developer == True:
            if len(usr_coding_langs) < 3:
                new_exp_sal = new_exp_sal - 10000
                output["res"].append("learn some more languages: $10k deducted from expected salary")

            elif len(usr_coding_langs) > 3:
                new_exp_sal = new_exp_sal + 10000
                output["res"].append("$10k added to your expected salary")
            else:
                new_exp_sal = new_exp_sal + 5000

        if is_designer == True:
            if len(sw_pkgs) < 3:
                new_exp_sal = new_exp_sal - 10000
                output["res"].append("learn some more design tools: $10k deducted from expected salary")

            elif len(sw_pkgs) > 3:
                new_exp_sal = new_exp_sal + 10000
                output["res"].append("$10k added to your expected salary")
            else:
                new_exp_sal = new_exp_sal + 5000


        if int(number_of_education_years_as_int) > 3:
            new_exp_sal = new_exp_sal + 5000
        else:
            new_exp_sal = new_exp_sal - 5000

        result_msg = ""

        for state in exp_salaries:
            salary = exp_salaries[state]

            # The '\n' character is replaced in the main file w/an html <br> tag

            result_msg = result_msg + 'Your starting salary living in ' + state + \
                         ' could have been $' + str(salary) + "." + '\n'

            result = result_msg.replace('\n', '<br>')

            # baseSal = state + ": " + str(base_salary)

            output["BaseSalary"] = result

        expSal = "Expect $" + str(new_exp_sal) + " for your level of experience." + "\n"

        output["Expected_Salary"] = expSal.replace('\n', '<br>')

        # result_msg = result_msg + "Expect $" + str(new_exp_sal) + " for your level of experience. "

        return output

