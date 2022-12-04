import sublime, re, os
import sublime_plugin

from .completion.react import react
from .completion.redux import redux
from .completion.router import router

class ReactCommand(sublime_plugin.EventListener):
	def __init__(self):
		self.all_completions = react + redux + router
		self.attr_completions = []
		self.mui_completions = []
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
		last_line 	= in_line[-1]
		on_string 	= view.match_selector(locations[0], "meta.string.js")
		on_attr 	= view.match_selector(locations[0], "meta.tag.attributes.js")
		
		if view.match_selector(locations[0], "meta.tag.attributes.js meta.interpolation.js source.js.embedded.jsx meta.mapping.js"):
			from .dataset.style import style_object
			return [("%s \tStyle" % s, "{0}: $0,".format(s)) for s in style_object]
		if on_string or (on_attr and last_line[-1] == '{'):
			return out
		if on_attr and last_line[-1] != '{':
			if len(self.attr_completions) == 0:
				from .dataset.event import event, attribute
				self.attr_completions = [("%s \tEvent" % s, "{0}={{$0}}".format(s)) for s in event] + [("%s \tAttr" % s, 'dangerouslySetInnerHTML={{ __html: "" }}' if s == "dangerouslySetInnerHTML" else "{0}={{$0}}".format(s)) for s in attribute]
			return self.attr_completions
		if '// mui' in in_line[0:2]:
			if len(self.mui_completions) == 0:
				from .completion.mui import mui
				from .dataset.mui_dataset import mui_dataset
				self.mui_completions = mui + [("%s \tComponent MUI" % s, "<{0}>$0</{0}>".format(s)) for s in mui_dataset]
			out = out + self.mui_completions
		for completion in self.all_completions:
			if completion and completion.trigger.find(r'{prefix}'):
				out.append(completion)

		return out
