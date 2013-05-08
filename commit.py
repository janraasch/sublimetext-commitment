import os
import random

try:
    from hashlib import md5
except ImportError:
    from md5 import md5

names = ['Nick', 'Steve', 'Andy', 'Qi', 'Fanny', 'Sarah', 'Cord', 'Todd',
    'Chris', 'Pasha', 'Gabe', 'Tony', 'Jason', 'Randal', 'Ali', 'Kim',
    'Rainer', 'Guillaume']

messages_file = os.path.join(os.path.dirname(__file__), 'commit_messages.txt')
messages = {}

# Create a hash table of all commit messages
for line in open(messages_file).readlines():
    messages[md5(line).hexdigest()] = line

class Commitment:
    def get(self, message_hash=None):
        if not message_hash:
            message_hash = random.choice(messages.keys())

        message = messages[message_hash].replace('XNAMEX', random.choice(names))

        message = message.replace('XUPPERNAMEX', random.choice(names).upper())
        message = message.replace('XLOWERNAMEX', random.choice(names).lower())

        return {
            'message': message,
            'message_hash': message_hash
        }