from config import NAME
from datetime import datetime


def question_message(pill):
    return "Hola " + NAME + ", tomaste ya "+pill+" ?"


def reminder_message(pill):
    return "Hola " + NAME + ",\nno hemos recibido tu respuesta, ya tomaste "+pill+" ?"


def insisting_message(pill):
    return NAME + ", todavia no he recibido tu respuesta, lo ha tomado ("+pill+") ?"


def pill_stringify(pill):
    if type(pill) is dict:
        return " y ".join("{0} ({1} dosis)".format(k, v) for k, v in pill.items())
    else:
        return str(pill)


def get_extra_string_time():
    return " \n" + str(datetime.now().strftime("%m/%d/%Y, %H:%M"))


def alert_message(pill):
    return "¡¡¡⚠️Cuidado " + NAME + "⚠️!!!\nTe queda poco de " + pill_stringify(pill) + " deberia ir a comprar"


def get_pill_remaining(pill):
    return "💊️¡Te queda " + pill_stringify(pill) + " !"


reply_valid = ['si', 'yep', 'yes', 'ok']
celebrate_message = '🥳, wow, que buena noticia, nos vemos pronto '
reply_invalid_message = 'Disculpa no entendi esta respuesta'
reply_invalid_command = 'Disculpa no entendi esta comanda'
reception_of_message_deactivated = 'recepcion de mensaje deactivados'

