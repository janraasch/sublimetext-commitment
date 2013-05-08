import sublime
import sublime_plugin
import HTMLParser

try:
    # Python 3
	from .commit import Commitment

except (ValueError):
	# Python 2
	from commit import Commitment

from commit import Commitment

whatthecommit = 'http://whatthecommit.com/'
randomMessages = Commitment()

class CommitmentCommand(sublime_plugin.WindowCommand):
    def run(self):
        commit = randomMessages.get()
        message = HTMLParser.HTMLParser().unescape(commit.get('message', '').replace('\n','').replace('<br/>', '\n'))
        message_hash = commit.get('message_hash', '')

        if message:
            print 'Commitment: ' + '\n' + message + '\n' + 'Permalink: ' + whatthecommit + message_hash
            sublime.set_clipboard(message)
            sublime.status_message(message)
