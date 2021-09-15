# Food-Recipe-Finder-Chatbot-in-Rasa
Using Rasa model to build an artificial intelligent based chatbot to help user finding recipe


## Introduction
In this project, an Artificial Intelligence (AI) chatbot is developed based on 
RASA model and Python language. A chatbot is a software built for interaction 
between human and computer by using written or verbal language. While AI chatbot 
is a chatbot that has been designed with Artificial Intelligence features, it may learn 
from training data, apply algorithms, and then respond to users.

## Requirment
Firstly, You need to install Rasa and Django with the suitable python version.
You can open an environment to use this system and the python I used in this system is **Python 3.6.13**

```ts
      pip install rasa
      pip install Django
```

## Recipes Database
- [Tasty](https://rapidapi.com/apidojo/api/tasty)

## How to use
after all requirements and files was downloaded. You can start running the code by using the command on your cmd. Using cmd is more simple and easy or you can run it on Pychram.

```ts
      rasa run -m models --enable-api --cors "*" --debug

      python manage.py runserver

      rasa run actions
```

Then you can find the localhost in the Django server and use that server to open the website. So, you can start to use the systetm.

## GUI
**Website page**
![GUI](https://user-images.githubusercontent.com/58298216/133365424-72c9028f-aac2-4df6-9c47-8d8ea5f9fff4.png)

**Chatroom**
![GUI2](https://user-images.githubusercontent.com/58298216/133365579-e30f066a-5b41-4bbf-b5c2-389aac5c6a4f.png)

**Response**
![response](https://user-images.githubusercontent.com/58298216/133365715-9c64445b-faae-4b9f-80dc-e3829ea9da4f.png)
