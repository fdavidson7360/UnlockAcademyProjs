from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
from calculate_api.utilities import calculator

days_of_week={
    "1": "Sunday",
    "2": "Monday",
    "3": "Tuesday",
    "4": "Wednesday",
    "5": "Thursday",
    "6": "Friday",
    "7": "Saturday"
}

app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    return 'Hello, World!'


@app.route('/')
def candidate_form():
    return render_template("index.html")


@app.route('/calculate_salary', methods=["POST"])
def calculate_salary():
    if request.method == "POST":
        numeric_day_of_appointment = request.form['appDay']
        time_of_appointment = request.form['appTime']
        service_type = request.form['serviceType']

        day_of_appointment = days_of_week[numeric_day_of_appointment]

        if day_of_appointment == "Sunday":
            return render_template("weAreClosed.html")

        else:
            result = calculator.calculate_services_price(day_of_appointment,
                                                time_of_appointment,
                                                service_type)

            #make dictionary here

            # result = {"date": day_of_appointment, "time_of_appointment": time_of_appointment,
            #           "service_type": service_type}

            print(result)

        return render_template("appointmentDetails.html", result=result)  # result=final_msg)

    else:  # if a GET request was attempted
        return "Please submit a POST request"


if __name__ == '__main__':
 app.run(debug=True)