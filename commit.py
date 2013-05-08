import random
import sublime

try:
    from hashlib import md5
except ImportError:
    from md5 import md5

commitMessages = 'commit_messages.txt'
messages = {}

st_version = 2
if sublime.version() == '' or int(sublime.version()) > 3000:
    st_version = 3

# Create a hash table of all commit messages
if st_version == 3:
    from zipfile import ZipFile
    messages_file = ZipFile(sublime.installed_packages_path() + '/Commitment.sublime-package').open(commitMessages)
    for line in messages_file.readlines():
        messages[md5(line).hexdigest()] = line
else:
    from os import path
    messages_file = open(path.join(path.dirname(__file__), commitMessages))
    for line in messages_file.readlines():
        messages[md5(line).hexdigest()] = line

# Create list of hashes
message_hashes = list(messages.keys())

names = ['Nick', 'Steve', 'Andy', 'Qi', 'Fanny', 'Sarah', 'Cord', 'Todd',
    'Chris', 'Pasha', 'Gabe', 'Tony', 'Jason', 'Randal', 'Ali', 'Kim',
    'Rainer', 'Guillaume']

class Commitment:
    def get(self, message_hash=None):
        if not message_hash:
            message_hash = random.choice(message_hashes)

        message = messages[message_hash].replace('XNAMEX', random.choice(names))

        message = message.replace('XUPPERNAMEX', random.choice(names).upper())
        message = message.replace('XLOWERNAMEX', random.choice(names).lower())

        return {
            'message': message,
            'message_hash': message_hash
        }