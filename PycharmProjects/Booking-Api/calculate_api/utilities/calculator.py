# available_times = ("8:00 am", "9:00 am", "10:00 am",
#                    "11:00 am", "12:00 pm", "1:00 pm",
#                    "2:00 pm", "3:00 pm", "4:00", "5:00 pm")

timeDict = {"Kim": ["8:00 am", "11:00 am", "12:00 pm"],
            "Fran": ["1:00 pm", "2:00 pm", "4:00 pm"],
            "Dee": ["9:00 am", "10:00 am", "3:00 pm", "5:00 pm"],
            "Jane": ["8:00 am", "9:00 am", "12:00 pm"]}

dayDict = {"Sunday": None,
           "Monday": ["Kim", "Dee"],
           "Tuesday": ["Jane"],
           "Wednesday": ["Fran", "Dee"],
           "Thursday": ["Dee", "Jane"],
           "Friday": ["Jane"],
           "Saturday": ["Fran", "Jane", "Kim"]}

possible_prices = {"New Locs": 300, "Retwist": 150, "Finger Waves": 85}

def calculate_services_price(day_of_appointment,
                             time_of_appointment,
                             service_type):
    try:
        exp_price = possible_prices[service_type]
    except KeyError:
        return "******** INPUT ERROR: Please enter a valid hairstlye ********"
    except Exception:
        "Something went wrong. Please Refresh or contact support: help@unlock.academy"
    else: # this only gets executed if the exception is not raised/called

        # exp_price = 0

        if day_of_appointment == "Sunday":
            pass
        elif day_of_appointment == "Monday":
            available_stylist = dayDict["Monday"]
            # available_stylist = available_stylist.split(",")
        elif day_of_appointment == "Tuesday":
            available_stylist = dayDict["Tuesday"]
            # available_stylist = available_stylist.split(",")
        elif day_of_appointment == "Wednesday":
            available_stylist = dayDict["Wednesday"]
            # available_stylist = available_stylist.split(",")
        elif day_of_appointment == "Thursday":
            available_stylist = dayDict["Thursday"]
            # available_stylist = available_stylist.split(",")
        elif day_of_appointment == "Friday":
            available_stylist = dayDict["Friday"]
            # available_stylist = available_stylist.split(",")
        elif day_of_appointment == "Saturday":
            available_stylist = dayDict["Saturday"]
            # available_stylist = available_stylist.split(",")
        else:
            return 10 + "*" + "Sorry. Please enter a valid day of the week." + 10 + "*"

        for stylist, time in timeDict.items():  # iterates through the key & values
            if time_of_appointment in time:      # sort through the times that matches
                free_stylist = stylist           # give the list of stylist available during that time
                break

        if free_stylist in available_stylist:
            result = {"date": day_of_appointment, "time": time_of_appointment,
                      "service_type": service_type,
                      "cost": exp_price, "employee": free_stylist,
                      "confirmation": "Your appointment is confirmed!!"}
            return result
        else:
            result = {"date": day_of_appointment, "time" : time_of_appointment,
                      "service_type": service_type, "cost": exp_price,
                      "employee": "Sorry no stylist was available"}
            return result





