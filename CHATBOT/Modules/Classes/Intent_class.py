from os import path
import json
import subprocess


class Intent():
    def __init__(self, file_name):
        self.json_file_name = file_name  # Имя json-файла с интентом как поле класса
        self.py_file_name = file_name[:-5] + ".py"  # .json - 5 символов, вычитаем их, добавляем ".py" - получаем
        # исполняемый файл

        self.keywords = []  # Список с ключевыми словами интента
        self.detect_keywords()  # Заполняем список с переменными

        self.variables = {}  # Инициализируем СПИСОК с переменными
        self.detect_variables()  # Заполняем словарь с переменными

        self.attributes_for_execution = []          # инициализируем список с необходимыми для запуска интента слотами
        self.detect_Attributes_For_Execution()      # заполняем его



    def detect_keywords(self):
        with open(self.json_file_name, 'r', encoding='utf-8') as f:
            # открыли файл с данными
            text = json.load(f)  # загнали все, что получилось в переменную
            for var_name in text["Keywords"]:
                self.keywords.append(var_name.lower())
        f.close()

    def detect_variables(self):
        with open(self.json_file_name, 'r', encoding='utf-8') as f:
            # открыли файл с данными
            text = json.load(f)  # загнали все, что получилось в переменную
            # pprint(text)  # вывели результат на экран
            for var_name in text["Variables"]:
                self.variables[var_name] = {}
                self.variables[var_name]["Value"]=text["Variables"][var_name]
                self.variables[var_name]["name_for_request"]= text["Variables"][var_name]["name_for_request"]
        f.close()

    def detect_Attributes_For_Execution(self):
        with open(self.json_file_name, 'r', encoding='utf-8') as f:
            # открыли файл с данными
            text = json.load(f)  # загнали все, что получилось в переменную
            self.attributes_for_execution = text["Attributes_For_Execution"]
        f.close()


    def print_vars(self):
        for var in self.variables:
            print(var, self.variables[var])

    def isMe(self, message_from_user):  # Распознавание интента из сообщения пользователя в синонимах
        for keyword in self.keywords:
            if message_from_user.lower().find(keyword.lower()) != -1:
                return True, keyword
        return False, keyword

    def run_intent(self, args):
        subprocess.call(["python", self.py_file_name, args])


"""
НЕНУЖНЫЙ КОД


    def isMe(self, potential_name_of_intent):              #Распознавание интента из сообщения пользователя в синонимах
        if potential_name_of_intent.lower() in self.keywords:
            return True
        else:
            return False

"""
