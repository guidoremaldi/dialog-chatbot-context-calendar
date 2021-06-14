from os.path import join

from Classes.Slot_Stack_class import Slot_Stack
from Classes.Intent_class import Intent
from Classes.Message_class import Message
import re
import os
from os import path
import os
import clr
from System import DateTime

pathDLL = "C:\\PyTest\\NewProjectorChat\\CHATBOTMAGA\\HorsLib\\Hors.dll"
clr.AddReference(pathDLL)
import datetime
from Hors import HorsTextParser

from DateTime_Parser_class import DateTime_Parser
from Calendar_DataBase_interaction_class import Calendar_Interaction

hors = HorsTextParser()

file_intent_array = [r"C:\CHATBOT_DIPLOM\Intents\Delete.txt",
                     r"C:\CHATBOT_DIPLOM\Intents\Create.txt"]


# DIALOG STATE TRACKER
class DST:
    default_directory = r"C:\PyTest\NewProjectorChat\CHATBOTMAGA\Modules\Intents"

    def __init__(self):
        self.current_intent = "Нет интента"
        self.Slot_Stack = Slot_Stack()  # КЛАСС СТЕКА С ДАННЫМИ ИНИЦИАЛИЗИРУЕМ
        self.DateTime = DateTime_Parser()
        self.intent_dict = {}
        # Каталог из которого будем брать файлы
        self.directory = DST.default_directory
        # Получаем список файлов интентов(json-ы и исполняемые) в переменную files
        self.files = os.listdir(self.directory)

        self.initialize_intents()

        self.Message = Message()

        self.current_user_message = ''

    def work(self):
        self.Message.Hello(self.intent_dict)
        self.Message.Input_intent()
        while True:
            if self.get_and_digest_message() == False:
                self.Message.Good_Bye()
                break

    def get_and_digest_message(self):
        self.current_user_message = input()
        # user_message = self.split_user_message(user_input)
        if self.current_user_message == 'Stop':
            return False
        self.parse_intent(self.current_user_message)
        self.Slots_Recognize(self.current_user_message)
        #self.Slot_Stack.print_slot_stack()
        if self.current_intent != 'Нет интента':
            self.check_intent_slots_fulfilled()

    def initialize_intents(self):
        for file_name in self.files:
            if file_name.endswith('.json'):
                name_of_intent = path.basename(file_name).split('.')[0]
                self.intent_dict[name_of_intent] = Intent(os.path.join(self.default_directory, file_name))
        # print(self.intent_dict)  # ВЫВОД ЧТО ТАМ НАХОДИТСЯ В СЛОВАРЕ ИНТЕНТОВ

    # Вытаскивалка интента из слова-неслота в строке СООБЩЕНИЯ
    # Распознавалка интента из строки сообщения пользователя
    def parse_intent(self, message_from_user):
        if message_from_user:
            for intent in self.intent_dict:
                if self.intent_dict[intent].isMe(message_from_user)[0] == True:
                    self.current_intent = intent
                    intent_keyword = self.intent_dict[intent].isMe(message_from_user)[1]
                    regex = re.compile(intent_keyword, flags=re.IGNORECASE)
                    self.current_user_message = regex.sub('', self.current_user_message)
                    self.Slot_Stack.Check_and_Append(self.current_intent, "Intent_name")
                    return self.current_intent
        if self.current_intent == "Нет интента":
            self.Message.No_intent()
        return "Нет интента"

    def get_time(self, string):
        string_parsed = hors.Parse(string, DateTime.now)
        if string_parsed:
            pass

    def parse_datetime(self, string):
        types = {0: "Fixed",
                 1: "Period",
                 2: "SpanForward",
                 3: "SpanBackward"
                 }
        datetime_parsed_raw = {}
        datetime_parsed = {"Type": "undefined", "HasTime": "undefined", "Duration": -1,
                           "DateFrom": {"year": 0, "month": 0, "day": 0, "hour": 0, "minute": 0},
                           "DateTo": {"year": 0, "month": 0, "day": 0, "hour": 0, "minute": 0}}
        result = hors.Parse(string, DateTime.Now)

        if result.Dates:


            datetime_parsed_raw["DateFrom"] = datetime.datetime.strptime(str(result.Dates[0].DateFrom),
                                                                         "%d.%m.%Y %H:%M:%S")
            datetime_parsed_raw["DateTo"] = datetime.datetime.strptime(str(result.Dates[0].DateTo),
                                                                       "%d.%m.%Y %H:%M:%S")

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
                duration = (datetime_parsed["DateTo"]["hour"] - datetime_parsed["DateFrom"]["hour"]) * 60 + (
                            datetime_parsed["DateTo"]["minute"] - datetime_parsed["DateFrom"]["minute"])
                # for component in datetime_parsed["DateTo"]:
                #   duration[component] = abs(datetime_parsed["DateTo"][component] - datetime_parsed["DateFrom"][component])
                datetime_parsed["Duration"] = duration
        else:
            datetime_parsed = "undefined"

        if result.Text.replace(" ", ''):
            rest_of_the_input = result.Text
        else:
            rest_of_the_input = "undefined"

        return datetime_parsed, rest_of_the_input

    # Распознавалка слотов из строки #СООБЩЕНИЯ
    def Slots_Recognize(self, message_from_user):
        # Разбиваем строку(сообщение пользователя) на слова
        parsed_list = self.parse_datetime(message_from_user)
        self.Slot_Stack.Check_and_Append(parsed_list[0], "time")
        self.Slot_Stack.Check_and_Append(parsed_list[1], "name_of_event")

    def split_user_message(self, user_input):
        message_from_user_splitted = [str(s) for s in user_input.split()]
        return message_from_user_splitted

    # Достаточно ли слотов в стеке для выполнения интента
    def check_intent_slots_fulfilled(self):
        can_be_executed = True
        missing_slots = []
        for intent_var in self.intent_dict[self.current_intent].variables:
            if self.Slot_Stack.check_var_exist(intent_var) != True:
                missing_slots.append(self.intent_dict[self.current_intent].variables[intent_var]["name_for_request"])
                # missing_slots.append(self.intent_dict[self.current_intent].variables[intent_var]["name_for_request"]) ДОДЕЛАТЬ!!!!!!!!!!!!!!!!!!!!!
                can_be_executed = False
        if can_be_executed == False:
            self.Message.Slot_request(missing_slots)  # если слотов недостаточно - запросить слоты
        else:
            slots_for_intent = []  # ИСПРАВИТь
            for element_of_stack in self.intent_dict[self.current_intent].attributes_for_execution:
                element_to_append = self.Slot_Stack.return_var(element_of_stack)
                if type(element_to_append)==dict:
                    string_time = '.'.join(str(element_to_append[key]) for key in element_to_append)
                    element_to_append=string_time
                slots_for_intent.append(str(element_to_append))
            # print(slots_for_intent)

            slots_for_intent = ','.join(slots_for_intent)
           # print(slots_for_intent)
            self.intent_dict[
                self.current_intent].run_intent(
                slots_for_intent)  # slots_for_intent если достаточно - исполнить интент и обнулить текущий интент   создай name=АЛЛАХ time=12345
            self.Slot_Stack.Intent_Fulfilled()
            self.Message.Intent_done(self.current_intent)
            self.Message.Anything_else()
            self.current_intent = 'Нет интента'

        # return can_be_executed

    def Print_Current_Slots(self):
        self.Slot_Stack.Print_Slot_Stack()


ChatBot = DST()
ChatBot.work()

"""
       
   ДОХОРСОВОЕ РЕШЕНИЕ
        message_from_user_splitted = self.split_user_message(message_from_user)
        for i in range(len(message_from_user_splitted)):
            if (message_from_user_splitted[i].find('=') != -1):
                self.Slot_Stack.Check_and_Append(message_from_user_splitted[i])
               """

"""




Системные сообщения

Выполнение команд
Интенты(с последовательным аргументом тоже)

НЕНУЖНЫЙ КОД



    # Вытаскивалка интента из слова-неслота в строке СООБЩЕНИЯ
    def parse_intent(self, message_from_user_splitted):
        for i in range(len(message_from_user_splitted)):
            if message_from_user_splitted[i].find('=') == -1:
                intent_word = message_from_user_splitted[i]
                self.current_intent = self.intent_keyword_search(intent_word)


    def intent_keyword_search(self, intent_word):
        for intent in self.intent_dict:
            if (self.intent_dict[intent].isMe2(intent_word) == True):
                return intent
        self.Message.No_intent()
        return "Нет интента"

"""
