from key import pill_list_key, pill_time_key
from datetime import time
import pytz
TOKEN = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
CHAT_ID = '-123456789'
NAME = 'BOB'
PILL_1 = 'paracetamol'
PILL_2 = 'pillForStomac'
alert_counter = 7  # if then is less than this value thread an alert

timezone = pytz.timezone('America/Santiago')
delta_time = 3


MORNING_PILL = {pill_list_key: [PILL_1, PILL_2], pill_time_key:  time(9, 0, tzinfo=timezone)}
AFTERNOON_PILL = {pill_list_key: [PILL_1], pill_time_key: time(16, 00, tzinfo=timezone)}
LATE_PILL = {pill_list_key: [PILL_2], pill_time_key: time(22, 00, tzinfo=timezone)}

PILL_PROGRAMMING = [MORNING_PILL, AFTERNOON_PILL, LATE_PILL]
TOTAL_PILL_LIST = [PILL_1, PILL_2]
