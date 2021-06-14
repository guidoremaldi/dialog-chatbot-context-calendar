import subprocess
import calendar
import datetime
import re
now=datetime.datetime.now()
from os import path
import os
import clr
from System import DateTime
pathDLL = "C:\\PyTest\\NewProjectorChat\\CHATBOTMAGA\\HorsLib\\Hors.dll"
clr.AddReference(pathDLL)
import datetime
from Hors import HorsTextParser

hors = HorsTextParser()

class DateTime_Parser:
    verbal_days = {"позапозавчера": -3, "позавчера": -2, "вчера": -1, "сегодня": 0, "завтра": 1, "послезавтра": 2,
                   "послепослезавтра": 3}

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



    def __init__(self):
        self.date=''
        self.time=''
        self.raw_string = ''
        self.duration = 'undefined'
        self.year = now.year
        self.month = now.month
        self.day = now.day
        self.hour = now.hour
        self.minute = now.minute


    def format_date(self):
        formats={}


    def get_span(self,A,B):
        pass

    def get_date(self):
        """ЕСЛИ ДАТА РАЗДЕЛЁННАЯ ТОЧКАМИ ИЛИ СЛЕШАМИ"""
        if self.date.find('.') != -1 or self.date.find('/') != -1:
            date_list = re.split('[. /]', self.date)
            print(date_list)
            if len(date_list) == 3:
                if int(date_list[0])//2000==1:
                    self.year = date_list[0]
                    self.month = date_list[1]
                    self.day = date_list[2]
                else:
                    if int(date_list[2])//2000==1:
                        self.year = date_list[2]
                        self.month = date_list[1]
                        self.day = date_list[0]
                    else:
                        return print("НЕПРАВИЛЬНЫЙ ФОРМАТ")
                    """ЕСЛИ С МЕСЯЦЕМ СТРОКОЙ"""
            if len(date_list) == 2:
                for element in date_list:
                    if element.isalpha():
                        print(element)
                        for month_number in DateTime_Parser.verbal_month:
                            if DateTime_Parser.verbal_month[month_number].lower().find(element[:3].lower())!=-1:
                                self.month = month_number
                                if date_list.index(element) == 0:
                                    self.day = date_list[1]
                                else:
                                    self.day = date_list[0]
                                return
                """ЕСЛИ ДЕНЬ МЕСЯЦ ЧИСЛАМИ"""
                self.day = date_list[0]
                self.month = date_list[1]
            return


        """ЕСЛИ ВЧЕРА СЕГОДНЯ ЗАВТРА И ТД"""
        if self.date.lower() in DateTime_Parser.verbal_days:  # строка с датой всеми нижними буковками
            self.day += DateTime_Parser.verbal_days[self.date.lower()]
            """НА ПРОШЛЫЕ ВЕЩИ"""
            if self.day <= 0:
                self.month -= 1
                if self.month == 0:
                    self.year = self.year-1
                    self.month = 12
                self.day = calendar.mdays[self.month] - self.day
            """НА БУДУЮЩИЕ ВЕЩИ"""
            if self.day > calendar.mdays[self.month]:
                self.month += 1
                if self.month > 12:
                    self.year = self.year + 1
                    self.month = 1
                self.day = self.day - calendar.mdays[self.month-1]

    """ДЛЯ КОНКРЕТНОГО ВРЕМЕНИ ИЛИ ДЛЯ ВСЕГО """

    def get_datetime(self, string):
        self.raw_string = string
        self.datetime = self.raw_string.split(".")
        self.year = self.datetime[0]
        self.month = self.datetime[1]
        self.day = self.datetime[2]
        self.hour = self.datetime[3]
        self.minute = self.datetime[4]
        #self.duration = self.datetime[5]


    def get_time(self):
        if self.raw_string.find('.') != -1:
                self.hour = self.time[:self.time.find('.')].lower()
                self.minute = self.time[self.time.find('.') + 1:].lower()
        else:
            if "all" in self.time.lower():
                self.hour = "all"
                self.minute = "all"


    def break_string(self):
        if self.raw_string.find('#') != -1:
            self.datetime = self.raw_string[:self.raw_string.find('#')]  # Имя переменной(до знака "#")
            self.duration = self.raw_string[self.raw_string.find('#') + 1:]  # Значение переменной (после "#")
        else:
            return print(ValueError)

    def process_time_arguments_for_create(self, string):
        self.raw_string = string
        self.datetime = self.raw_string
        self.get_datetime(self.datetime)
        DateTime = {"year": str(self.year), "month": str(self.month), "day": str(self.day), "hour": str(self.hour),
                    "minute": str(self.minute), "Duration": str(self.duration)}
        return DateTime

    def process_string(self, string):
        self.raw_string = string
        # print(self.raw_string)
        self.break_string()
        # print(self.date,'/',self.time)
        self.get_date()
        self.get_time()
        DateTime = {"year": str(self.year), "month": str(self.month), "day": str(self.day), "hour": str(self.hour), "minute": str(self.minute), "Duration": str(self.duration)}
        return DateTime
        #self.print_time()

    def print_time(self):
        print(self.year, '.', self.month, '.', self.day, '/', self.hour, ':', self.minute)

    def parse_datetime(self, string):
        types = {0: "Fixed",
                 1: "Period",
                 2: "SpanForward",
                 3: "SpanBackward"
                 }
        datetime_parsed_raw={}
        datetime_parsed = {"Type": "undefined", "HasTime": "undefined", "Duration": "undefined",
                           "DateFrom": {"year": 0, "month": 0, "day": 0, "hour": 0, "minute": 0},
                           "DateTo": {"year": 0, "month": 0, "day": 0, "hour": 0, "minute": 0}}
        result = hors.Parse(string, DateTime.Now)
        print("Я тут")
        if result.Dates:
            print("Дата есть")

            datetime_parsed_raw["DateFrom"] = datetime.datetime.strptime(str(result.Dates[0].DateFrom), "%d.%m.%Y %H:%M:%S")
            datetime_parsed_raw["DateTo"] = datetime.datetime.strptime(str(result.Dates[0].DateTo), "%d.%m.%Y %H:%M:%S")

            datetime_parsed["Type"] = types[result.Dates[0].Type]
            datetime_parsed["HasTime"] = result.Dates[0].HasTime
            datetime_parsed["DateFrom"]["year"] = datetime_parsed_raw["DateFrom"].year
            datetime_parsed["DateFrom"]["month"] = datetime_parsed_raw["DateFrom"].month
            datetime_parsed["DateFrom"]["day"] = datetime_parsed_raw["DateFrom"].day
            datetime_parsed["DateFrom"]["hour"] = datetime_parsed_raw["DateFrom"].hour
            datetime_parsed["DateFrom"]["minute"] = datetime_parsed_raw["DateFrom"].minute

            datetime_parsed["DateTo"]["year"] = datetime_parsed_raw["DateTo"].year
            datetime_parsed["DateTo"]["month"] = datetime_parsed_raw["DateTo"].month
            datetime_parsed["DateTo"]["day"] = datetime_parsed_raw["DateTo"].day
            datetime_parsed["DateTo"]["hour"] = datetime_parsed_raw["DateTo"].hour
            datetime_parsed["DateTo"]["minute"] = datetime_parsed_raw["DateTo"].minute
            if result.Dates[0].HasTime:
                duration = {}
                for component in datetime_parsed["DateTo"]:
                    duration[component] = abs(datetime_parsed["DateTo"][component]-datetime_parsed["DateTo"][component])
                datetime_parsed["Duration"]=duration
        else:
            datetime_parsed = "undefined"
        rest_of_the_input=result.Text
        return datetime_parsed, rest_of_the_input


    def diff_vs_now(self, datetime_parsed):
        now=datetime.datetime.now()
        negative_difference_data = False
        diff_year=datetime_parsed.year-now.year
        diff_month = datetime_parsed.month - now.month
        diff_day = datetime_parsed.day - now.day
        diff_hour = datetime_parsed.hour - now.hour
        diff_minute = datetime_parsed.minute - now.minute
        difference = {"year": diff_year, "month": diff_month, "day": diff_day, "hour": diff_hour, "minute": diff_minute}
        for key in difference:
            if difference[key]<0:
                negative_difference_data=[True, key, difference[key]]
                break
        return negative_difference_data



