import random

names = ['Nick', 'Steve', 'Andy', 'Qi', 'Fanny', 'Sarah', 'Cord', 'Todd',
    'Chris', 'Pasha', 'Gabe', 'Tony', 'Jason', 'Randal', 'Ali', 'Kim',
    'Rainer', 'Guillaume']

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

        return {
            'message': message,
            'message_hash': message_hash
        }