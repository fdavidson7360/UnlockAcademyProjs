from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime

from calculate_api.utilities import calculator
import json

app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    return "<b>Hello, Tribe</b>"


@app.route('/')
def candidate_form():
    return render_template("index.html")


# @app.route('/open-jobs')
# def open_jobs():
#     f = open("data.json", "r")  # opens file in read mode
#     data_contents = f.read()  # Reads data from file and stores in variable as raw text
#     jobs_json = json.loads(data_contents)  # turns raw text into python object
#
#     result_msg = ""
#     for job in jobs_json:
#         print(job)
#         print(job["job_title"])
#         print(job["location"])
#         result_msg = result_msg + job["job_title"] + "\n"
#
#         result_msg = result_msg.replace('\n', '<br>')
#
#     return render_template("result.html", message=result_msg)


@app.route('/calculate_salary', methods=["POST"])
def calculate_salary():
    if request.method == "POST":
        # f = open("my_db.txt", "a")
        profession = request.form['profession']
        # f.write("Profession:" + profession)
        # f.write("\n")
        number_of_exp_yrs = int(request.form['experience'])
        # f.write("Years of experience:" + str(number_of_exp_yrs))
        # f.write("\n")

        langs = request.form['languages']
        usr_coding_langs = langs.split(",")
        # f.write("List of coding languages:" + str(usr_coding_langs))
        # f.write("\n")

        design_tools = request.form['designTools']
        design_tools_split = design_tools.split(",")
        # f.write("Design tools:" + str(sw_pkgs))
        # f.write("\n")
        #
        # f.close()

        dob_input = request.form['dob']
        # Converts a string into a datetime object output: yyyy/mm/dd
        dob_obj = datetime.strptime(dob_input, "%m/%d/%Y")

        # Formats the new datetime object to output: mm/dd/yyyy
        date_ftmd = dob_obj.strftime("%m/%d/%Y")

        full_name = request.form['fullName']

        age = int(request.form['age'])
        country = request.form['country']
        state = request.form['state']
        number_of_edu_yrs = int(request.form['educationYears'])

        is_developer = False
        is_designer = False
        if int(profession) == 1:
            is_developer = True
        else:
            is_designer = True

        usr_info = {
            "dob": date_ftmd, "full_name": full_name, "country": country,
            "state": state, "is_active": True, "number_of_education_years": number_of_edu_yrs,
            "age": age
        }

        calculated_result = calculator.calculate_expected_salary(number_of_exp_yrs, usr_info, number_of_edu_yrs,
                                             is_developer, is_designer, usr_coding_langs, design_tools_split)

        # f = open("data.json", "r")
        # file_contents = f.read()

        # The newline characters only respond in python print(), so when I
        # return my result that is run through flask I replace it with an html line break

        # calculated_result = calculated_result.replace('\n', '<br>')

        final_msg = calculated_result  # + "\n\n"  #  + file_contents +"\n"
        # final_msg = final_msg.replace('\n', '<br>')

        return render_template("result.html", message=final_msg)

    else:  # if GET request was attempted
        return "Please submit a POST request"


if __name__ == '__main__':
 app.run(debug=True)