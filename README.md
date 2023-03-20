# bot_tel_medicina
Bot to record to take a medecine periodically

## How to set up
1) download ngrok[https://ngrok.com/download] and install it in this folder
2) install the python package 
`python -m pip install -r requirements.txt`
3) create a config.py file with your telegram token, chat ID and Name
`TOKEN='MyTelegramTokenOfTypeAAAAAAA-BBBBBBBBBBBBBBB'
`CHAT_ID='MYID123'`
`NAME='MYID123'`
5) you should have your ngrok server running :
`python server.py` 
4) Then you can start in an other window the bot 
`python bot.py`


## This script is base on the following :
(source)[https://djangostars.com/blog/how-to-create-and-deploy-a-telegram-bot/#page]
