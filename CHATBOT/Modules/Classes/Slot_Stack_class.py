class Slot_Stack:
    def __init__(self):
        self.intent_and_vars = [{"Intent": {"Intent_name": "undefined", "Status": "InProgress"},
                                 "Attributes": {
                                     "name_of_event": "undefined",
                                     "time": "undefined"}}]
        self.current_stack_element_number = 0
        self.new_stack_element = {
            "Intent": {"Intent_name": "undefined", "Status": "InProgress"},
            "Attributes": {
                "name_of_event": "undefined",
                "time": "undefined"}}

    def Check_and_Append(self, var_value, var_name):
        self.Check_current_slot_stack_element()

        if var_name == "Intent_name":
            if self.intent_and_vars[self.current_stack_element_number]["Intent"]["Intent_name"] == "undefined":
                self.intent_and_vars[self.current_stack_element_number]["Intent"]["Intent_name"] = var_value

        if var_name == "time":
            if self.intent_and_vars[self.current_stack_element_number]["Attributes"]["time"] == "undefined":
                self.intent_and_vars[self.current_stack_element_number]["Attributes"]["time"] = var_value

        if var_name == "name_of_event":
            if self.intent_and_vars[self.current_stack_element_number]["Attributes"]["name_of_event"] == "undefined":
                self.intent_and_vars[self.current_stack_element_number]["Attributes"]["name_of_event"] = var_value

    def Intent_Fulfilled(self):
        self.intent_and_vars[self.current_stack_element_number]["Intent"]["Status"] = "Fulfilled"
        self.intent_and_vars.append(self.new_stack_element)
        self.current_stack_element_number += 1

    def Check_current_slot_stack_element(self):
        if self.intent_and_vars[self.current_stack_element_number]["Intent"]["Intent_name"] != "undefined" and \
                self.intent_and_vars[self.current_stack_element_number]["Intent"]["Status"] in (
                "Fulfilled", "Declined"):
            self.intent_and_vars.append(self.new_stack_element)
            self.current_stack_element_number += 1

    def check_type(self, something, the_type):
        if the_type == "str":
            if isinstance(something, str):
                return "name"
        if the_type == "dict":
            if isinstance(something, dict):
                return "time"

    def check_var_exist(self, var_name):
        if self.intent_and_vars[self.current_stack_element_number]["Attributes"][var_name] != "undefined":
            return True
        else:
            return False


    def return_var(self,var_name):
        if type(var_name)==list:
            return self.intent_and_vars[self.current_stack_element_number]["Attributes"][var_name[0]][var_name[1]]
        return self.intent_and_vars[self.current_stack_element_number]["Attributes"][var_name]

    def print_slot_stack(self):
        print(self.intent_and_vars)

    def isNotEmptyTrue(self, string):
        if string and (string!="undefined" or string == "True"):
            return True
        else:
            return False



"""

ЕСЛИ УЖЕ ЕСТЬ - ДОПИСАТЬ ВОТ ЭТО
        if slot_variable_name in self.vars:
            self.vars[slot_variable_name] = slot_variable_value
        else:
            self.vars.update({slot_variable_name: slot_variable_value})
"""

"""
 self.intent_and_vars = [{"Intent":
 {"Name": имя, "time": время, "status": fulfilled/declined}}]
  
 
 затравочная штука 
 [{"Intent":"Intent_name,
    "Attributes":{
    "Name": undefined, 
    "time": undefined}}]


declined - если поступил новый интент 
 
 ЧЕМ РАСПОЗНАВАТЬ ДАННЫЕ
 
 
 
 
 
 его же - данные из  self.intent_and_vars[len(self.intent_and_vars)-1]
 
 }







    def Check_and_Append(self, var_name_and_value):
        slot_variable_name = var_name_and_value[:var_name_and_value.find('=')]  # Имя переменной(до знака "=")
        slot_variable_value = var_name_and_value[var_name_and_value.find('=') + 1:]  # Значение переменной (после "=")
        if slot_variable_name in self.vars:
            self.vars[slot_variable_name] = slot_variable_value
        else:
            self.vars.update({slot_variable_name: slot_variable_value})

    def Print_Slot_Stack(self):
        print("Стек текущих слотов:")
        for slot_var_name in self.vars:
            print(slot_var_name, ' = ', self.vars[slot_var_name])

"""
