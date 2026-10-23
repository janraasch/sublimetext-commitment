import random
import re

names = ['Nick', 'Steve', 'Andy', 'Qi', 'Fanny', 'Sarah', 'Cord', 'Todd',
    'Chris', 'Pasha', 'Gabe', 'Tony', 'Jason', 'Randal', 'Ali', 'Kim',
    'Rainer', 'Guillaume', 'Kelan', 'David', 'John', 'Stephen']

num_re = re.compile(r'XNUM([0-9,]*)X')

class RandomCommitment:
    def __init__(self, messages):
        self.messages = messages;
        self.message_hashes = list(messages.keys())

    def get(self, message_hash=None):
        if not message_hash:
            message_hash = random.choice(self.message_hashes)

        message = self.messages[message_hash].replace(
            'XNAMEX', random.choice(names))

        message = message.replace('XUPPERNAMEX', random.choice(names).upper())
        message = message.replace('XLOWERNAMEX', random.choice(names).lower())

        nums = num_re.findall(message)
        while nums:
            start = 1
            end = 999
            value = nums.pop(0) or str(end)
            if ',' in value:
                position = value.index(',')
                if position == 0:
                    end = int(value[1:])
                elif position == len(value) - 1:
                    start = int(value[:position])
                else:
                    start = int(value[:position])
                    end = int(value[position + 1:])
            else:
                end = int(value)
            if start > end:
                end = start * 2

            message = num_re.sub(str(random.randint(start, end)), message, count=1)

        return {
            'message': message,
            'message_hash': message_hash
        }
