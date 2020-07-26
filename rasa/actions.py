# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import sqlite3,re
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet,AllSlotsReset
#
#
class ActionHelloWorld(Action):
#
    def name(self) -> Text:
        return "action_find_address"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            location=tracker.get_slot("location")
            conn=sqlite3.connect('hospital_data.db')
            curr=conn.cursor()
            if re.search(r'[0-9]{6}',location)!=None:
                print("pincode")
                curr.execute("SELECT * FROM data where postal_code is 'IN/{}'".format(location))
            else:
                curr.execute("SELECT * FROM data where location is '{}'".format(location))
            a=curr.fetchall()
            count=0
            addresses=[]
            for row in a:
                count=count+1
                temp=''
                temp=temp+str(row[2])+", "
                temp=temp+str(row[3])+", "
                temp=temp+str(row[1])+", "
                if row[4]!='NULL':
                    temp=temp+'location(latitude'
                    temp=temp+str(row[4])+" longitude"
                    temp=temp+str(row[5])+")"
                addresses.append(temp)
            dispatcher.utter_message(text="There are {} location".format(count))
            count=0
            if count>10:
                dispatcher.utter_message(text="here are the top 3 searches")
            for address in addresses:
                count=count+1
                if count>=10:
                    break
                dispatcher.utter_message(text="{}: {}".format(count,address))

            return []

class ActionSlotReset(Action):
    def name(self):
        return 'action_slot_reset'
    def run(self, dispatcher, tracker, domain):
        return[AllSlotsReset()]
