import requests
from bottle import Bottle, response, request as bottle_request
from config import TOKEN, CHAT_ID
import schedule
from time import sleep
from threading import Thread
from text import question_message, reply_valid, celebrate_message, reply_invalid_message, insisting_message
from datetime import datetime, timedelta


def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)


def get_test_schedule(extra_time=10):
    now_plus_1 = datetime.now() + timedelta(seconds=extra_time)
    now_plus_1 = now_plus_1.strftime("%H:%M:%S")
    return now_plus_1


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
        """
        send message to default chat ID
        """
        json_data = {
            "chat_id": CHAT_ID,
            "text": message,
        }
        self.send_message(json_data)


class TelegramBot(BotHandlerMixin, Bottle):
    BOT_URL = 'https://api.telegram.org/bot'+TOKEN+'/'

    def __init__(self, *args, **kwargs):
        super(TelegramBot, self).__init__()
        self.route('/', callback=self.post_handler, method="POST")  # init the reading of reply

        self.time_wait_answer = 1  # time in minute
        self.a_question_is_pending = False
        self.received_valid_answer = False
        self.first_time_insisting = True
        self.last_time_question_send = datetime.now()
        self.insisting_task = None

        self.task_check_reply = self.config_wait_reply()  # config reply
        self.config_question()
        Thread(target=schedule_checker).start()

    def config_question(self, time=get_test_schedule()):
        """
        Method to schedule the send of the question at a specific time
        """
        schedule.every().day.at(time).do(self.send_question)

    def config_wait_reply(self):
        """
        Method to schedule the wait of the reply
        """
        next_time = self.time_wait_answer * 60  # conversion minute to second
        return schedule.every().day.at(get_test_schedule(next_time)).do(self.check_reply)

    def check_reply(self):
        """
        Method to check if we have received a valid answer since last time
        """
        if self.received_valid_answer:  # if the bot had received a valid answer we do not re-schedule
            print('no need to reschedule')
        else:
            self.send_insisting_question()
            if self.first_time_insisting:  # if it is the firs time we are insisting
                # schedule check every x minute
                self.insisting_task = schedule.every(self.time_wait_answer).minutes.do(self.check_reply)
                # deactivate first time insisting
                self.first_time_insisting = False
                # schedule.cancel_job(self.task_check_reply)

    def update_last_time(self):
        """
        Method to update the last time a question was send
        """
        self.last_time_question_send = datetime.now()
        self.a_question_is_pending = True  # activate that a reply is pending

    def process_text_input(self, text):
        """
        Method to process the received message
        """
        try:
            reply_valid.index(text.lower())  # check if the reply is valid
            # reset some parameter
            self.a_question_is_pending = False
            self.received_valid_answer = True
            if self.insisting_task is not None:  # deactivate insisting
                schedule.cancel_job(self.insisting_task)
                print('deactivate insisting')
            # return the result message
            return celebrate_message
        except ValueError:
            return reply_invalid_message

    def send_question(self):
        """
        Method to send the question message and activate the different value
        """
        self.send_message_default(question_message + " " + str(datetime.now()))
        self.update_last_time()
        self.received_valid_answer = False
        self.first_time_insisting = True  # reset first time insisting

    def send_insisting_question(self):
        """
        Method to send insisting message
        """
        self.send_message_default(insisting_message + " " + str(datetime.now()))
        self.update_last_time()

    def prepare_data_for_answer(self, data):
        """
        Method to process the received data and return the output data
        """
        message = self.get_message(data)
        answer = self.process_text_input(message)
        chat_id = self.get_chat_id(data)
        json_data = {
            "chat_id": chat_id,
            "text": answer,
        }
        return json_data

    def post_handler(self):
        """
        Method to handle the input
        """
        data = bottle_request.json
        answer_data = self.prepare_data_for_answer(data)
        self.send_message(answer_data)
        return response


if __name__ == '__main__':
    app = TelegramBot()
    print("start")
    app.run(host='localhost', port=8080)
