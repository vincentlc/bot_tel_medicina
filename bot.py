import requests
from bottle import Bottle, response, request as bottle_request
from config import TOKEN, CHAT_ID
import schedule
from time import sleep
from threading import Thread
from text import question_message, reply_valid, celebrate_message, reply_invalid_message
import datetime


def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)


class BotHandlerMixin:
    BOT_URL = None

    def get_chat_id(self, data):
        """
        Method to extract chat id from telegram request.
        """
        chat_id = data['message']['chat']['id']
        return chat_id

    def get_message(self, data):
        """
        Method to extract message id from telegram request.
        """
        message_text = data['message']['text']
        return message_text

    def send_message(self, prepared_data):
        """
        Prepared data should be json which includes at least `chat_id` and `text`
        """
        message_url = self.BOT_URL + 'sendMessage'
        requests.post(message_url, json=prepared_data)

    def send_message_default(self, message):
        json_data = {
            "chat_id": CHAT_ID,
            "text": message,
        }
        self.send_message(json_data)


class TelegramBot(BotHandlerMixin, Bottle):
    BOT_URL = 'https://api.telegram.org/bot'+TOKEN+'/'

    def __init__(self, *args, **kwargs):
        super(TelegramBot, self).__init__()
        self.route('/', callback=self.post_handler, method="POST")
        schedule.every().day.at("12:03").do(self.send_question)
        Thread(target=schedule_checker).start()
        

    def change_text_message(self, text):
        try:
            reply_valid.index(text.lower())
            return celebrate_message
        except ValueError:
            return reply_invalid_message


    def send_question(self):
        self.send_message_default(question_message + " " + str(datetime.datetime.now()))

    def prepare_data_for_answer(self, data):
        message = self.get_message(data)
        answer = self.change_text_message(message)
        chat_id = self.get_chat_id(data)
        json_data = {
            "chat_id": chat_id,
            "text": answer,
        }
        return json_data

    def post_handler(self):
        data = bottle_request.json
        answer_data = self.prepare_data_for_answer(data)
        self.send_message(answer_data)
        return response


if __name__ == '__main__':
    app = TelegramBot()
    print("start")
    app.run(host='localhost', port=8080)
