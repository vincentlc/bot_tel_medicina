from config import NAME


def question_message(pill):
    return "Hola " + NAME + ", tomaste ya la "+pill+" ?"


def reminder_message(pill):
    return "Hola " + NAME + ",\nno hemos recibido tu respuesta, ya tomaste "+pill+" ?"


def insisting_message(pill):
    return NAME + ", todavia no he recibido tu respuesta, lo ha tomado ("+pill+") ?"


def alert_message(pill):
    pill_string=''
    for key, value in pill.items():
        pill_string += str(value) + " " + key + " y "
    return "¡¡¡⚠️Cuidado " + NAME + "⚠️!!!\nTe queda poco de " + str(pill_string) + " deberia ir a comprar"


reply_valid = ['si', 'yep', 'yes', 'ok']
celebrate_message = '🥳, wow, que buena noticia, nos vemos pronto '
reply_invalid_message = 'Disculpa no entendi esta respuesta'
reply_invalid_command = 'Disculpa no entendi esta comanda'
reception_of_message_deactivated = 'recepcion de mensaje deactivados'

