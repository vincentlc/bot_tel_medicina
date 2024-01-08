# bot_tel_medicina
Bot to record to take a medecine periodically

## How to set up
1) download [ngrok](https://ngrok.com/download) and install it in this folder
2) install the python package 
`python -m pip install -r requirements.txt`
3) create a config.py file with your telegram token, chat ID, Name and time zone
`TOKEN='MyTelegramTokenOfTypeAAAAAAA-BBBBBBBBBBBBBBB'`
`CHAT_ID='MYID123'`
`NAME='MYID123'`
`timezone = pytz.timezone('Continent/CITY')`
   
   
4) add the information pill in that file (replace PILL_X by a string of the name of the pill, adapt the time for your need )
`MORNING_PILL = {'pill_list': [PILL_1, PILL_2], pill_time_key: time(10, 20, tzinfo=timezone)}`
`AFTERNOON_PILL = {'pill_list': [PILL_2], pill_time_key: time(16, 30, tzinfo=timezone), 'pill_quantity': [3]}`
`LATE_PILL = {'pill_list': [PILL_2], pill_time_key: time(22, 50, tzinfo=timezone), 'pill_quantity': [4]} `
`PILL_PROGRAMMING = [MORNING_PILL, AFTERNOON_PILL, LATE_PILL] # you can add more or less item in that list depending of your need` 
`TOTAL_PILL_LIST = [PILL_1, PILL_2] # must be the list of all the different type of pill used`

5) creat a pill_file.txt with the following config information :
`PILL1_name,inicial cuantity`
`PILL2_name,inicial cuantity`
That will be for example :
`Paracetamol ,5`
`ibuprofen  ,10`

6) you should have your ngrok server running :
`python server.py` 
7) Then you can start in an other window the bot 
`python bot.py`

8) Important with the new version, you need to make the bot as admin to make it work

## This script is base on the following :
[source](https://djangostars.com/blog/how-to-create-and-deploy-a-telegram-bot/#page)
