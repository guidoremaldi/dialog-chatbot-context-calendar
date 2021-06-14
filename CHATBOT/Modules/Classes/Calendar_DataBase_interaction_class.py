import collections

"""
event_data={"time": time, "event_info": new_event}
"""
class Calendar_Interaction:
    def __init__(self,  calendar_database):
        #self.event_data = event_data
        self.calendar_database = calendar_database

    def month_to_str(month):
        verbal_month = {1: "Январь",
                        2: "Февраль",
                        3: "Март",
                        4: "Апрель",
                        5: "Май",
                        6: "Июнь",
                        7: "Июль",
                        8: "Август",
                        9: "Сентябрь",
                        10: "Октябрь",
                        11: "Ноябрь",
                        12: "Декабрь"}
        if verbal_month[month][len(verbal_month[month]) - 1] == 'ь' or verbal_month[month][
            len(verbal_month[month]) - 1] == 'й':
            month_out = verbal_month[month][:len(verbal_month[month]) - 1] + "е"
            return month_out
        else:
            month_out = verbal_month[month] + "e"
            return month_out


    def delete_event(self, event_data):
        time = event_data["time"]
        del self.calendar_database[time["year"]][time["month"]][time["day"]][time["hour"]][time["minute"]]

    def check_coincidence(self, event_data):
        time = event_data["time"]
        if time["year"] in self.calendar_database:
            if time["month"] in self.calendar_database[time["year"]]:
                if time["day"] in self.calendar_database[time["year"]][time["month"]]:
                    if time["hour"] in self.calendar_database[time["year"]][time["month"]][time["day"]]:
                        if time["minute"] in self.calendar_database[time["year"]][time["month"]][time["day"]][time["hour"]]:
                            if "Event_name" in self.calendar_database[time["year"]][time["month"]][time["day"]][time["hour"]][time["minute"]]:
                                print("Есть событие")
                                return True

        #print("Нет события")
        return False

    def check_what_is_there(self,  event_data):
        time = event_data["time"]
        if len(time)==5:
            if self.check_coincidence(time):
                return self.calendar_database[time["year"]][time["month"]][time["day"]][time["hour"]][time["minute"]]
            else:
                print("СВОБОДНО")
                return "СВОБОДНО"
        if len(time)==4:
            return print(self.calendar_database[time["year"]][time["month"]][time["day"]][time["hour"]])
        if len(time)==3:
            return print(self.calendar_database[time["year"]][time["month"]][time["day"]])
        if len(time)==2:
            return print(self.calendar_database[time["year"]][time["month"]])
        if len(time)==1:
            return print(self.calendar_database[time["year"]])

    def insert_new_event(self, event_data):
        if "all" in event_data["time"].values():
            return print("НЕМОЖНО СОЗДАТИ")
        time=event_data["time"]
        if time["year"] in self.calendar_database:
            if time["month"] in self.calendar_database[time["year"]]:
                if time["day"] in self.calendar_database[time["year"]][time["month"]]:
                    if time["hour"] in self.calendar_database[time["year"]][time["month"]][time["day"]]:
                        #if minute in self.calendar_database[year][month][day][hour]:
                         #   pass
                            #self.calendar_database[year][month][day][hour][minute]["Event_name"] = "Аллах ОЧЕНЬ велик"
                        #else:
                        self.calendar_database[time["year"]][time["month"]][time["day"]][time["hour"]][time["minute"]] = event_data["event_info"]
                    else:
                        self.calendar_database[time["year"]][time["month"]][time["day"]][time["hour"]] = {time["minute"]: event_data["event_info"]}
                else:
                    self.calendar_database[time["year"]][time["month"]][time["day"]] = {time["hour"]: {time["minute"]: event_data["event_info"]}}
            else:
                self.calendar_database[time["year"]][time["month"]] ={time["day"]: {time["hour"]: {time["minute"]: event_data["event_info"]}}}
        else:
            self.calendar_database[time["year"]] = {time["month"]:
                                                             {time["day"]: {time["hour"]: {time["minute"]: event_data["event_info"]}}}}

    def sort_calendar(self):
        for year in self.calendar_database:
            for month in self.calendar_database[year]:
                for day in self.calendar_database[year][month]:
                    for hour in self.calendar_database[year][month][day]:
                        sorted_minutes = {minute: self.calendar_database[year][month][day][hour][minute] for minute in
                                          sorted(self.calendar_database[year][month][day][hour])}
                        self.calendar_database[year][month][day][hour] = sorted_minutes
                    sorted_hours = {hour: self.calendar_database[year][month][day][hour] for hour in sorted(self.calendar_database[year][month][day])}
                    self.calendar_database[year][month][day] = sorted_hours
                sorted_days = {day: self.calendar_database[year][month][day] for day in sorted(self.calendar_database[year][month])}
                self.calendar_database[year][month] = sorted_days
            sorted_months = {month: self.calendar_database[year][month] for month in sorted(self.calendar_database[year])}
            self.calendar_database[year] = sorted_months
        sorted_years = {year: self.calendar_database[year] for year in sorted(self.calendar_database)}
        self.calendar_database = sorted_years
        return self.calendar_database

"""



year, month, day, hour, minute = (2021, 12, 3, 15, 00) #Тут я время получаю
time={"year": year,
  "month": month,
  "day": day,
      "hour": hour,
      "minute": minute
      }
standart_event = dict({"Event_name": "Я очень больщой писюн имею - закачаетесь...", "Event_Duration": 1, "Event_Location": "Неизвестно", "Event_Description": "Неизвестно"})
# Either
time1={"year": year,
      "month": month,
      "day": day
       }

""""""


new_event=standart_event
db={}
event_data={"time": time, "event_info": new_event}
Calendar_Interaction=Calendar_Interaction(db)
Calendar_Interaction.check_what_is_there(event_data["time"])
Calendar_Interaction.insert_new_event(event_data)
print(Calendar_Interaction.calendar_database)
#Calendar_Interaction.check_coincidence(event_data["time"])
#Calendar_Interaction.check_what_is_there(event_data["time"])
#Calendar_Interaction.check_what_is_there(time1)
Calendar_Interaction.delete_event(event_data["time"])
#Calendar_Interaction.check_coincidence(event_data["time"])
#Calendar_Interaction.check_what_is_there(event_data["time"])
#print(Calendar_Interaction.calendar_database)











def month_to_str(month):
    verbal_month = {1: "Январь",
                    2: "Февраль",
                    3: "Март",
                    4: "Апрель",
                    5: "Май",
                    6: "Июнь",
                    7: "Июль",
                    8: "Август",
                    9: "Сентябрь",
                    10: "Октябрь",
                    11: "Ноябрь",
                    12: "Декабрь"}
    if verbal_month[month][len(verbal_month[month])-1]=='ь' or verbal_month[month][len(verbal_month[month])-1]=='й':
        month_out = verbal_month[month][:len(verbal_month[month]) - 1] + "е"
        return month_out
    else:
        month_out = verbal_month[month]+"e"
        return month_out



event_data={"time": time, "event_info": new_event}
print(self.calendar_database)
{"Event_name": "Допригався на новий год..."}

dd = collections.defaultdict(dict)
dd['a']['b'] = "foo"

self.calendar_database = dict({2021: {
    12: {
        3: {
            15: {
                00: {
                    "Event_name": "Аллах велик"
                }
            }
        }

    }
}})



"""
