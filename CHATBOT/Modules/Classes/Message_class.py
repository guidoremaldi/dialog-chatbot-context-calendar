class Message:

    def Hello(self, intents):
        print("Здравствуйте! Я чатбот для работы с календарём. Я умею:")
        print('Записывать события в календарь - просто напишите "Создай", время и название события')
        print("Также я умею выводить сведения о событиях, удалять их, менять местами друг с другом")
        print("Можете поэксперементировать со мной!")

    def Input_intent(self):
        print("Введите команду:")

    def No_slot(self, slots):
        for slot in slots:
            print(slot, ' нету')

    def No_intent(self):
        print("Не нашёл интент в строке. Может, попробуете ещё раз?")

    def Anything_else(self):
        print("Что-нибудь ещё?")

    def Slot_request(self, slots):
        print("Уточните пожалуйста ", slots)

    def Clairify(self): #Уточнить, вероятно вы имеете ввиду этот интент, надо дополнить слоты
        print()

    def Deleted(self, event_info):
        print("Удалено:", event_info)

    def Good_Bye(self):
        print("До свидания!")

    def Intent_done(self, intent_name):
        print("Интент ",intent_name," исполнен")

    def Insigned(self, event_info):
        print("Записал,", event_info)