import sublime, re, os
import sublime_plugin

from .completion.react import react
from .completion.redux import redux
from .completion.router import router

class ReactCommand(sublime_plugin.EventListener):
	def __init__(self):
		self.all_completions = react + redux + router
	def on_query_completions(self, view, prefix, locations):
		source 		= [
			view.match_selector(locations[0], "source.jsx"),
			view.match_selector(locations[0], "source.tsx"),
		]

		if not True in source:
			return []

		win 		= sublime.active_window()
		current 	= win.active_view().file_name()
		prefix 		= prefix.lower()
		cursor 		= locations[0] - len(prefix)
		line 		= view.substr(sublime.Region(0, cursor))
		active 		= ''
		out 		= []
		in_line  	= line.split('\n')
		on_string 	= view.match_selector(locations[0], "meta.string.js")
		
		if on_string:
			return out
		if '// mui' in in_line[0:2]:
			from .completion.mui import mui
			from .dataset.mui_dataset import mui_dataset
			out = out + mui + [("%s \tComponent MUI" % s, "<{0}>$0</{0}>".format(s)) for s in mui_dataset]
		for completion in self.all_completions:
			if completion and completion.trigger.find(r'{prefix}'):
				out.append(completion)

		return out
