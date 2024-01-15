from config import NAME
from datetime import datetime
from random import randrange


def get_random_hi():
    return hi_list[randrange(len(hi_list))]


def get_random_question():
    return pill_question_message_list[randrange(len(pill_question_message_list))]


def get_random_reminder():
    return pill_question_reminder_message_list[randrange(len(pill_question_reminder_message_list))]


def question_message(pill):
    return get_random_hi() + " " + NAME + ", " + get_random_question() + " " + pill + " ?"


def reminder_message(pill):
    return get_random_hi() + " " + NAME + ",\n" + get_random_reminder() + " "+pill+" ?"


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


reply_valid = ['si', 'yep', 'yes', 'ok', "oui"]
celebrate_message = '🥳, wow, que buena noticia, nos vemos pronto '
reply_invalid_message = 'Disculpa no entendi esta respuesta'
reply_invalid_command = 'Disculpa no entendi esta comanda'
reception_of_message_deactivated = 'recepcion de mensaje deactivados'
pill_question_message_list = ['tomaste ya ', 'ya capturaste con tu boca',  'Tu as déjà pris']
pill_question_reminder_message_list = ['no hemos recibido tu respuesta, ya tomaste',
                                       'Yo,¿ lo tomaste o que ?', "tu l'as prix ou quoi"]


hi_list = ["Hola", "Yo", "Saludos", "Buenos días", "Buenas tardes", "Buenas noches","Buenas dias buenas tardes", "wena",
           "weeeeenaaaaa", "wena wena", 'Bonjour', 'Bonsoir', "Hi", "Hello", "Hey", "Greetings", "Howdy", "Hi there",
           "What's up", "How's it going", "Hiya", "G'day",
           "Bonjour", "Salut", "Coucou", "Allô", "Hé", "Bien le bonjour", "Bonsoir", "Ça va", "Coucou toi", "Salutations"
           "Quoi de neuf docteur",
            "Ciao (Italian)", "Guten Tag (German)", "Namaste (Hindi)", "Konnichiwa (Japanese)",
           "Annyeonghaseyo (Korean)", "Sawasdee (Thai)", "Merhaba (Turkish)",
           "Nǐ hǎo (Mandarin)", "Salam (Arabic)", "Privet (Russian)", "Jambo (Swahili)", "Aloha (Hawaiian)",
           "Szia (Hungarian)", "Zdravo (Serbian)", "Gia'sou (Greek)", "Shalom (Hebrew)", "Sveiki (Latvian)",
           "Szia (Hungarian)", "Dobrý den (Czech)", "Buna ziua (Romanian)", "Hej (Swedish)",
           "Ahoj (Slovak)", "Kamusta (Filipino)", "Bok (Croatian)", "Selamat (Indonesian)",
           "Merhaba (Azerbaijani)", "Sawubona (Zulu)"
            ]

