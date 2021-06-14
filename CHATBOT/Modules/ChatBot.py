# Подключаем модуль
import os
from os import path
from Classes.Intent_class import Intent
from Classes.DST_class import DST


class ChatBot():
    default_directory = r"C:\PyTest\NewProjectorChat\CHATBOTMAGA\Modules\Intents"

    def __init__(self):
        self.intent_dict = {}
        self.DST = DST()  # КЛАСС DST С ДАННЫМИ ИНИЦИАЛИЗИРУЕМ
        # Каталог из которого будем брать файлы
        self.directory = ChatBot.default_directory
        # Получаем список файлов в переменную files
        self.files = os.listdir(self.directory)

    def initialize_intents(self):
        for file_name in self.files:
            name_of_intent = path.basename(file_name).split('.')[0]
            self.intent_dict[name_of_intent] = Intent(os.path.join(self.default_directory, file_name))
        #print(self.intent_dict)  # ВЫВОД ЧТО ТАМ НАХОДИТСЯ В СЛОВАРЕ ИНТЕНТОВ




ChatBot = ChatBot()
ChatBot.initialize_intents()
ChatBot.intent_dict["Create"].isMe("Bubunga")
