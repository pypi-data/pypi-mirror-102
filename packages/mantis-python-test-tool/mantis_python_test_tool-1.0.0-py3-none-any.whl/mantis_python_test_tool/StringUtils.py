import random
import string
from urllib3.packages.six import unichr
from random import randrange


class StringUtils:

    def get_random_string(self, length):
        i = 0
        result_str = ''.join(
            random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(length))
        return result_str

    def get_random_sentence(self, length):
        sentence = ""
        while length > 0:
            randNumber = randrange(10)
            sentence = sentence + self.get_random_string(randNumber) + " "
            length = length - 1
        return sentence

    def get_fivech_sentence(self, length):
        sentence = ""
        randString = self.get_random_string(5)
        while length > 0:
            sentence = sentence + self.get_random_string(5) + " "
            length = length - 1
        return sentence

    def get_random_unicode(self, length):
        try:
            get_char = unichr
        except NameError:
            get_char = chr

        # Update this to include code point ranges to be sampled
        include_ranges = [
            (0x0021, 0x0021),
            (0x0023, 0x0026),
            (0x0028, 0x007E),
            (0x00A1, 0x00AC),
            (0x00AE, 0x00FF),
            (0x0100, 0x017F),
            (0x0180, 0x024F),
            (0x2C60, 0x2C7F),
            (0x16A0, 0x16F0),
            (0x0370, 0x0377),
            (0x037A, 0x037E),
            (0x0384, 0x038A),
            (0x038C, 0x038C),
        ]

        alphabet = [
            get_char(code_point) for current_range in include_ranges
            for code_point in range(current_range[0], current_range[1] + 1)
        ]
        return ''.join(random.choice(alphabet) for i in range(length))

    def get_random_sentence_unicode(self, length):
        sentence = ""
        while length > 0:
            randNumber = randrange(10)
            sentence = sentence + self.get_random_unicode(randNumber) + " "
            length = length - 1
        return sentence

