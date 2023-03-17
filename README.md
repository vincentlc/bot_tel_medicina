# bot_tel_medicina
Bot to record to take a medecine periodically

## How to set up
1) download ngrok[https://ngrok.com/download] and install it in this folder
2) install the python package 
`python -m pip install -r requirements.txt`
3) create a config.py file with your telegram token
`TOKEN='MyTelegramTokenOfTypeAAAAAAA-BBBBBBBBBBBBBBB'`
4) then you can start the bot 
`python bot.py`
5) you should also have your ngrok server running :
`ngrok http 8080`

## This script is base on the following :
(source)[https://djangostars.com/blog/how-to-create-and-deploy-a-telegram-bot/#page]
