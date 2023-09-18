import os.path

from config import PILL_1, PILL_2, MORNING_PILL, AFTERNOON_PILL, TOTAL_PILL_LIST, alert_counter
import logging
from collections import Counter

log = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
pill_file = "pill_file.txt"


init_value = 0


class PillChecker:
    def __init__(self):
        self.pill_list = TOTAL_PILL_LIST
        self.pill_counter = Counter(self.load_pill())
        # print(self.pill_counter)

    def decrease_quantity(self, pill_list):
        valid_pill_list = []
        for pill in pill_list:  # keep only valid pill
            if pill in self.pill_list:
                valid_pill_list.append(pill)

        self.pill_counter.subtract(Counter(valid_pill_list))
        self.write_pill()
        # print(self.pill_counter)

    def is_alert_level(self):
        alert_pill = {}
        for pill in self.pill_list:
            current_count = self.pill_counter[pill]
            if current_count < alert_counter:
                alert_pill.update({pill: current_count})
        print(alert_pill)
        return bool(alert_pill), alert_pill

        #return alert_pill

    def increase_pill(self, pill, quantity):
        if pill in self.pill_list:
            self.pill_counter.update({pill: quantity})  # update mean here increase of the counter by this value
        self.write_pill()
        # print(self.pill_counter)

    def write_pill(self):
        with open(pill_file, 'w') as f:
            for pill in self.pill_counter:
                f.write('%s,%s\n' % (pill, self.pill_counter[pill]))

    def load_pill(self):
        pill_list_counter = {}
        if os.path.isfile(pill_file):
            try:
                with open(pill_file, 'r') as f:
                    all_lines = f.readlines()
                for line in all_lines:
                    pill = line.rstrip().split(",")
                    pill_list_counter.update({pill[0]: int(pill[1])})
            except:
                for pill in self.pill_list:  # init all the counter at zero
                    pill_list_counter.update({pill: init_value})
        else:
            for pill in self.pill_list:  # init all the counter at zero
                pill_list_counter.update({pill: init_value})
        # print(pill_list_counter)
        return pill_list_counter

    def get_pill_list(self):
        return ' y '.join(self.pill_list)


# a = PillChecker()
#
# # a.decrease_quantity(TOTAL_PILL_LIST)
#
# a.decrease_quantity([PILL_1, PILL_2, 'patate'])
# print(a.get_pill_list())
# a.increase_pill(PILL_1, 14)
# print(a.is_alert_level())

