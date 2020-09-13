
from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
from Appointment_Api.utilities import schedular

days_of_week = {
    "1": "Sunday",
    "2": "Monday",
    "3": "Tuesday",
    "4": "Wednesday",
    "5": "Thursday",
    "6": "Friday",
    "7": "Saturday",
}

app = Flask(__name__)


@app.route('/')
def appointment_form():
    return render_template("index.html")


@app.route('/schedule_app', methods=['POST'])
def schedule_app():
    if request.method == 'POST':
        numeric_day_of_appointment = request.form["day_appt"]
        time_of_appointment = request.form['time_appt']
        service_type = request.form['serviceType']
        day_of_appointment = days_of_week[numeric_day_of_appointment]
        if day_of_appointment == "Sunday":
            return render_template("WeAreClosed.html")
        else:
            schedular.calculate_services = schedular.calculate_services_price(day_of_appointment,
                                                                              time_of_appointment,
                                                                              service_type)

        return render_template("AD.html",
                               output=schedular.calculate_services)


if __name__ == '__main__':
    app.run(debug=True)