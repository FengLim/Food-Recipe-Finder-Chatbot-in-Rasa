# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import json

from rasa_sdk import Action, Tracker
from typing import Any, Text, Dict, List

from rasa_sdk.executor import CollectingDispatcher
import requests


#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("I am Feng")
        dispatcher.utter_message(text="Hello World!i am here!")

        return []


class ActionSearchRecipe(Action):

    def name(self) -> Text:
        return "action_search_recipe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        for e in entities:
            if e['entity'] == 'main':
                name = e['value']

        return []


class ActionFindRecipe(Action):

    def name(self) -> Text:
        return "action_find_recipe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        # print("Last Message Now", entities)
        main = None

        for e in entities:
            if e['entity'] == "main":
                main = e['value']

        url = "https://tasty.p.rapidapi.com/recipes/auto-complete"
        querystring = {"prefix": main}
        headers = {
            'x-rapidapi-key': "655af94497mshbaf02cc26ad7dc5p1b655djsnb6afbbfe4883",
            'x-rapidapi-host': "tasty.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        response = response.json()

        print(response)

        chicken_list = []
        dispatcher.utter_message(text="LIST OF RECIPE\n")
        for result in response['results']:
            # print(result['display'])
            dispatcher.utter_message(text=result['display'])

        return []


class ActionFindRecipe(Action):

    def name(self) -> Text:
        return "action_search_recipe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        # print("Last Message Now", entities)
        main = None
        duration = None
        recipes = []
        num = 0

        for e in entities:
            if e['entity'] == "main":
                main = e['value']

        for f in entities:
            if f['entity'] == "duration":
                duration = f['value']

        print(duration)
        print(main)

        try:
            url = "https://tasty.p.rapidapi.com/recipes/list"

            querystring = {"from": "0", "size": "10", "tags": duration, "q": main}

            headers = {
                'x-rapidapi-key': "655af94497mshbaf02cc26ad7dc5p1b655djsnb6afbbfe4883",
                'x-rapidapi-host': "tasty.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            response = response.json()

            if main is None and duration is None:
                dispatcher.utter_message(text="Sorry, I haven't got anything matching that")

            else:
                dispatcher.utter_message(text="-----<LIST OF RECIPE>------\n")
                for result in response['results']:

                    recipes.append(result['name'])
                    num = num + 1
                    for x in recipes:
                        print(num)

                    print(result['name'])
                    dispatcher.utter_message(text="   (ID: " + str(result['id']) + ")   " + result['name'])

                dispatcher.utter_message(text="-----<END>-----\nPlease Enter the recipe ID you like")


        except:
            dispatcher.utter_message(text="Sorry, I haven't got anything matching that")

        return []


class ActionShowRecipe(Action):

    def name(self) -> Text:
        return "action_show_recipe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        # print("Last Message Now", entities)
        main = None

        for e in entities:
            if e['entity'] == "id":
                id = e['value']

        url = "https://tasty.p.rapidapi.com/recipes/detail"

        querystring = {"id": id}

        headers = {
            'x-rapidapi-key': "655af94497mshbaf02cc26ad7dc5p1b655djsnb6afbbfe4883",
            'x-rapidapi-host': "tasty.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        response = response.json()

        print(response)

        dispatcher.utter_message(text="-----<Ingredients>------\n")
        for section in response['sections']:
            for component in section['components']:
                print(component['raw_text'])
                dispatcher.utter_message(text="-->" + component['raw_text'])
        dispatcher.utter_message(text="-----<END>-----\n\n")

        dispatcher.utter_message(text="-----<RECIPE>------\n")
        for result in response['instructions']:
            print(result['display_text'])

            dispatcher.utter_message(text="-->" + result['display_text'])
        dispatcher.utter_message(text="-----<END>-----\n\n")

        return []


class ActionFindEasyRecipe(Action):

    def name(self) -> Text:
        return "action_find_easy_recipe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        # print("Last Message Now", entities)
        main = None

        for e in entities:
            if e['entity'] == "duration":
                duration = e['value']

        url = "https://tasty.p.rapidapi.com/recipes/list"
        querystring = {"from": "0", "size": "10", "tags": duration}
        headers = {
            'x-rapidapi-key': "655af94497mshbaf02cc26ad7dc5p1b655djsnb6afbbfe4883",
            'x-rapidapi-host': "tasty.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        response = response.json()

        print(response)

        dispatcher.utter_message(text="LIST OF RECIPE\n")

        for result in response['results']:
            print(result['name'])
            dispatcher.utter_message(text=result['name'])

        return []
