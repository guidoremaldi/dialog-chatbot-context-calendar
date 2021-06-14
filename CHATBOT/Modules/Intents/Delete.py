from sys import argv
import json
import sys

#print(sys.argv[1:])
from DateTime_Parser_class import DateTime_Parser
from Calendar_DataBase_interaction_class import Calendar_Interaction

"""
event_data={"time": time, "event_info": new_event}
"""

DateTime = DateTime_Parser()
args = [str(s) for s in sys.argv[1].split(',')]
#for arg in args:
#    print('Я Create, вот мои аргументы: ', arg)

datetime=DateTime.process_time_arguments_for_create(args[1])

standart_event = {'Event_name': args[0], 'Event_Duration': args[2], 'Event_Location': 'undefined', 'Event_Description': 'undefined'}

event_data={"time": datetime, "event_info": standart_event}

with open(r'C:\PyTest\NewProjectorChat\CHATBOTMAGA\Modules\Calendar_database\Calendar.json') as f:
    data = json.load(f)
Calendar_Interaction=Calendar_Interaction(data)
Calendar_Interaction.sort_calendar()
if not Calendar_Interaction.check_coincidence(event_data):
    Calendar_Interaction.insert_new_event(event_data)
    data = Calendar_Interaction.sort_calendar()
#data["Events"].update(a_dict)

with open(r'C:\PyTest\NewProjectorChat\CHATBOTMAGA\Modules\Calendar_database\Calendar.json', 'w') as f:
    json.dump(data, f, indent = 4, ensure_ascii=False)

''' 

event_dict = dict({ DateTime.year:{
                        DateTime.month:{
                            DateTime.day:{
                                DateTime.hour:{
                                    DateTime.minute:{
                                        "Event_name": args[0]
                                    }
                                }
                            }
                        }
}})



Year:{
    Month:{
        Date:{
            Time{
                Event_name: "BAR MITZVA"
                Event_duration: "Default
                Event_location: "Default"
                Event_description: "Default"
interface = argv[1]
vlan = argv[2]

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print('interface {}'.format(interface))
print('\n'.join(access_template).format(vlan))

    "June": {
      "1": {
        "12.00": "None"
      }
    }
    
    print("Текущий год: %d" % now.year)
print("Текущий месяц: %d"% now.month)
print("Текущий день: %d" % now.day)
print("Текущий час: %d" % now.hour)
print("Текущая минута: %d" % now.minute)
print(now.strftime("%d-%m-%Y %H:%M"))
    
'''