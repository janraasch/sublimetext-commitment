import sublime
import sublime_plugin

from commit import Commitment

whatthecommit = 'http://whatthecommit.com/'
randomMessages = Commitment()

class CommitmentToClipboardCommand(sublime_plugin.WindowCommand):
    def run(self):
    	commit = randomMessages.get()
    	message = commit.get('message', '')
    	message_hash = commit.get('message_hash', '')

    	if message:
    		print 'Commitment: ' + message + '\n' + 'Permalink: ' + whatthecommit + message_hash
        	sublime.set_clipboard(message)

class CommitmentToStatusBarCommand(sublime_plugin.WindowCommand):
    def run(self):
    	commit = randomMessages.get()
    	message = commit.get('message', '')
    	message_hash = commit.get('message_hash', '')

    	if message:
    		print 'Commitment: ' + message + '\n' + 'Permalink: ' + whatthecommit + message_hash
        	sublime.status_message(message)