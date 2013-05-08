import sublime
import sublime_plugin

try:
	# Python 3
	from .commit import Commitment
	from html.parser import HTMLParser

except (ValueError):
	# Python 2
	from commit import Commitment
	from HTMLParser import HTMLParser

whatthecommit = 'http://whatthecommit.com/'
randomMessages = Commitment()
htmlParser = HTMLParser()

class CommitmentCommand(sublime_plugin.WindowCommand):
    def run(self):
        commit = randomMessages.get()
        message = htmlParser.unescape(commit.get('message', '').replace('\n','').replace('<br/>', '\n'))
        message_hash = commit.get('message_hash', '')

        if message:
            print('Commitment: ' + '\n' + message + '\n' + 'Permalink: ' + whatthecommit + message_hash)
            sublime.set_clipboard(message)
            sublime.status_message(message)