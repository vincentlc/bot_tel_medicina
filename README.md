# bot_tel_medicina
Bot to record to take a medecine periodically

## How to set up
1) download [ngrok](https://ngrok.com/download) and install it in this folder
2) install the python package 
`python -m pip install -r requirements.txt`
3) create a config.py file with your telegram token, chat ID and Name
`TOKEN='MyTelegramTokenOfTypeAAAAAAA-BBBBBBBBBBBBBBB'`
`CHAT_ID='MYID123'`
`NAME='MYID123'`
4) add the information pill in that file (replace PILL_X by a string of the name of the pill, adapt the time for your need )
`MORNING_PILL = {'pill_list': [PILL_1, PILL_2], 'pill_hour': 19, 'pill_minute': 15, 'pill_quantity': [1, 2]}`
`AFTERNOON_PILL = {'pill_list': [PILL_2], 'pill_hour': 19, 'pill_minute': 46, 'pill_quantity': [3]}`
`LATE_PILL = {'pill_list': [PILL_2], 'pill_hour': 19, 'pill_minute': 59, 'pill_quantity': [4]} `
`PILL_PROGRAMMING = [MORNING_PILL, AFTERNOON_PILL, LATE_PILL] # you can add more or less item in that list depending of your need` 
5) you should have your ngrok server running :
`python server.py` 
6) Then you can start in an other window the bot 
`python bot.py`

7) Important with the new version, you need to make the bot as admin to make it work

## This script is base on the following :
[source](https://djangostars.com/blog/how-to-create-and-deploy-a-telegram-bot/#page)
