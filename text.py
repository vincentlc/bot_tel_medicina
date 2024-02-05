from config import NAME
from datetime import datetime
from random import randrange


def get_random_hi():
    return hi_list[randrange(len(hi_list))]


def get_random_question():
    return pill_question_message_list[randrange(len(pill_question_message_list))]


def get_random_reminder():
    return pill_question_reminder_message_list[randrange(len(pill_question_reminder_message_list))]


def get_random_celebrate():
    return celebrate_message_list[randrange(len(celebrate_message_list))]


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
    return "¡¡¡⚠️Cuidado " + NAME + "⚠️!!!\nTe queda poco de " + pill_stringify(pill) + " deberías ir a comprar"


def get_pill_remaining(pill):
    return "💊️¡Te queda " + pill_stringify(pill) + " !"


reply_valid = ['si', 'yep', 'yes', 'ok', "oui", "listo", "ya!", "ya", "sí"]
celebrate_message_list = ['🥳 wow, qué buena noticia, nos vemos pronto',
                          "🙌 Excelente, gracias por avisar", "🎉 Me alegro mucho, hasta más rato!"]
reply_invalid_message = 'Disculpa, no entendí esta respuesta'
reply_invalid_command = 'Disculpa no entendí esta instrucción'
reception_of_message_deactivated = 'Recepción de mensaje deactivado'
pill_question_message_list = ['es la hora! Tomaste la ', 'es ahora! Ya la capturaste con tu boca la',
                              'Tu as déjà pris la']
pill_question_reminder_message_list = ['No he recibido tu respuesta, ya la tomaste?',
                                       'Hola? La tomaste? Sí o qué?', "Tu l'as prix ou quoi?",
                                       "Y? Sigo esperando que la tomes", "Ahora sí que sí?", "Hágale pues!",
                                       "Ya poh! Me estoy cansando", "Di que sí, ya?"]


hi_list = ["Hola", "Yo", "Saludos", "Buenos días", "Buenas tardes", "Buenas noches","Buenas dias buenas tardes", "wena",
           "weeeeenaaaaa", "wena wena", 'Bonjour', 'Bonsoir', "Hi", "Hello", "Hey", "Greetings", "Howdy", "Hi there",
           "What's up", "How's it going", "Hiya", "G'day",
           "Bonjour", "Salut", "Coucou", "Allô", "Hé", "Bien le bonjour", "Bonsoir", "Ça va", "Coucou toi",
           "Salutations", "Quoi de neuf docteur",
            "Ciao (Italian)", "Guten Tag (German)", "Namaste (Hindi)", "Konnichiwa (Japanese)",
           "Annyeonghaseyo (Korean)", "Sawasdee (Thai)", "Merhaba (Turkish)",
           "Nǐ hǎo (Mandarin)", "Salam (Arabic)", "Privet (Russian)", "Jambo (Swahili)", "Aloha (Hawaiian)",
           "Szia (Hungarian)", "Zdravo (Serbian)", "Gia'sou (Greek)", "Shalom (Hebrew)", "Sveiki (Latvian)",
           "Szia (Hungarian)", "Dobrý den (Czech)", "Buna ziua (Romanian)", "Hej (Swedish)",
           "Ahoj (Slovak)", "Kamusta (Filipino)", "Bok (Croatian)", "Selamat (Indonesian)",
           "Merhaba (Azerbaijani)", "Sawubona (Zulu)"
            ]

