from config import NAME


def question_message(pill):
    return "Hola " + NAME + ", tomaste ya la "+pill+" ?"


def insisting_message(pill):
    return NAME + ", todavia no he recibido tu respuesta, lo ha tomado ("+pill+") ?"


reply_valid = ['si', 'yep', 'yes', 'ok']
celebrate_message = '🥳, wow, que buena noticia, nos vemos pronto '
reply_invalid_message = 'Disculpa no entendi esta respuesta'
reply_invalid_command = 'Disculpa no entendi esta comanda'
reception_of_message_deactivated = 'recepcion de mensaje deactivados'

