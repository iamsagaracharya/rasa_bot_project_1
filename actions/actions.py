# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionShowAccount(Action):
    def name(self) -> Text:
        return "action_show_account_number"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        account_number = next(tracker.get_latest_entity_values('account_number'), None)


 
        if account_number:
            
            dispatcher.utter_message(text=f"Your account number is {account_number}.")
        else:
            dispatcher.utter_message(text=f"Please enter account number.")

        return []
    
class ActionCheckBalance(Action):
    def name(self) -> Text:
        return "action_checking_balance"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        account_number = next(tracker.get_latest_entity_values('account_number'), None)
        account_holder = next(tracker.get_latest_entity_values('name'), None)
        account_details = {"sagar":{"123456": "20000"}}
 
        if account_number in account_details[account_holder]:
            
            dispatcher.utter_message(text=f"Dear {account_holder} your account {account_number} has balance {account_details[account_holder][account_number]}.")
        else:
            dispatcher.utter_message(text=f"Not found")

        return []