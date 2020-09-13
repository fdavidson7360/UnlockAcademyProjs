time_Dict = {"Kim": ["8:00 am", "11:00 am", "12:00 pm"],
             "Iesha": ["1:00 pm", "2:00 pm", "4:00 pm"],
             "Dezzy": ["9:00 am", "10:00 am", "3:00 pm", "5:00 pm"],
             "Danielle": ["8:00 am", "9:00 am", "12:00 pm"]}

day_Dict = dict(Sunday=None, Monday=["Kim", "Dee"], Tuesday=["Jane"], Wednesday=["Fran", "Dee"],
                Thursday=["Dee", "Jane"], Friday=["Jane"], Saturday=["Fran", "Jane", "Kim"])

possible_prices = {"New Locs": 300, "Retwist": 150, "Faux Locs": 200}


def calculate_services_price(day_of_appointment,
                             time_of_appointment,
                             service_type):
    try:
        exp_price = possible_prices[service_type]
    except KeyError:
        return "Please enter a valid hairstyle"
    except Exception:
        "Something went wrong. Please Refresh or contact support: help@unlock.academy"
    else:
        exp_price = 0
        if day_of_appointment == "Sunday":
            pass
        elif day_of_appointment == "Monday":
            availableStylists = "Monday"
        elif day_of_appointment == "Tuesday":
            availableStylists = "Tuesday"
        elif day_of_appointment == "Wednesday":
            availableStylists = "Wednesday"
        elif day_of_appointment == "Thursday":
            availableStylists = "Thursday"
        elif day_of_appointment == "Friday":
            availableStylists = "Friday"
        elif day_of_appointment == "Saturday":
            availableStylists = "Saturday"
        else:
            return "Sorry. Please enter a valid day of the week."

        for stylist, time in time_Dict.items():
            if time_of_appointment in time:
                freeStylist = stylist
                break

        if availableStylists in stylist:
            result = {"date": day_of_appointment,
                      "time": time_of_appointment,
                      "service": service_type,
                      "cost": possible_prices[service_type],
                      "employee": freeStylist}

        else:
            result = {"date": day_of_appointment,
                      "time": time_of_appointment,
                      "service": service_type,
                      "cost": possible_prices[service_type],
                      "employee": None}
            # "message": freeStylist + " is not available for that time, please enter another time. "}

        output = {
                "weekday": day_of_appointment,
                "appointment": time_of_appointment,
                "service": service_type,
                "cost": possible_prices[service_type]
            }

        print(output)

    return result