# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import json
import random

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




class ActionFindRecipe(Action):
    #find the recipe based on the entities (ingredient)
    #show the recipe and ID to suggest user

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
        recipesID = []

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

            querystring = {"from": "0", "size": "50", "tags": duration, "q": main}

            headers = {
                'x-rapidapi-key': "655af94497mshbaf02cc26ad7dc5p1b655djsnb6afbbfe4883",
                'x-rapidapi-host': "tasty.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            response = response.json()

            if main is None and duration is None:
                dispatcher.utter_message(text="Sorry, I haven't got anything matching that. Can you use other keyword?")

            else:

                for result in response['results']:

                    recipes.append(result['name'])
                    recipesID.append(result['id'])

                print(len(recipes))
                # generate random number
                lis = []
                if len(recipes) < 5:
                    lis = [0, 1, 2, 3]
                    print(lis)
                elif len(recipes) < 4:
                    lis = [0, 1, 2]
                elif len(recipes) < 3:
                    lis = [0, 1]
                elif len(recipes) < 2:
                    lis = [0]
                else:
                    for i in range(5):

                        r = random.randint(0, len(recipes)-1)
                        if r not in lis:
                            lis.append(r)
                            i += 1

                print(lis)

                print(lis[0], lis[1], lis[2], lis[3])

                #try

                rr = ""

                for g in lis:
                    print(g)
                    print(recipes[g])
                    print(recipesID[g])
                    rr = rr + "<ID:" + str(recipesID[g]) + ">" + str(recipes[g]) + "\n"

                print(rr)
                dispatcher.utter_message(text= "------<LIST OF RECIPE>-------\n" + str(rr))
                #try
                dispatcher.utter_message(text= "Please Enter the ID you like")

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

        ingredient = []
        recipe = []
        name = []


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

        for section in response['sections']:
            for component in section['components']:

                ingredient.append(component['raw_text'])

        for result in response['instructions']:
            print(result['display_text'])

            recipe.append(result['display_text'])

        name = response['name']
        video = response['original_video_url']

        print(response['original_video_url'])

        print(ingredient)

        ingredientlist = []

        text = ""
        for ingredients in ingredient:
            text = text + ingredients + "\n"
            ingredientlist.append(ingredients)


        print(text)

        print(recipe)
        print(len(recipe))
        stepNo = []
        for num in range(len(recipe)):

            stepNo.append(num)

        print(stepNo)
        print(recipe[1])
        steplist = []
        recipetext = ""
        for no in stepNo:
                recipetext = recipetext + str(no+1) + ". "+ recipe[no] + "\n"
                steplist.append(recipe[no])

        print(len(ingredientlist))
        print(len(steplist))
        print(recipe)

        a = len(ingredientlist)
        b = len(steplist)

        level = 0
        level = (a+b)/10

        print(level)

        hardness = None
        if level < 3:
            hardness = "Easy"
        elif level < 5:
            hardness = "Normal"
        elif level < 8:
            hardness = "Hard"
        else:
            hardness = "expert"

        dispatcher.utter_message(text="NAME:\t  " + name + "\nLevel: " + hardness + "\n------<LIST of INGREDIENT>-------\n" + text)
        dispatcher.utter_message(text= "-----<RECIPE>------\n" + recipetext)

        if video is None:
            dispatcher.utter_message(text="Sorry, this recipes don't have the relevant video.")
        else:
            dispatcher.utter_message(text= "video link: <" + video + ">")

        return []



