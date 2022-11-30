import sublime

redux = [
	sublime.CompletionItem(
		"redux,createSlice",
		annotation="react-redux",
		completion="import { createSlice } from \"@reduxjs/toolkit\";\n\nconst initialState = {\n\tvalue: 0,\n}\n\nexport const exampleSlice = createSlice({\n\tname: \"example\",\n\tinitialState,\n\treducers: {\n\t\tincrement: (state) => {\n\t\t\tstate.value += 1\n\t\t},\n\t\tdecrement: (state) => {\n\t\t\tstate.value -= 1\n\t\t},\n\t},\n})\n\nexport const { increment, decrement } = exampleSlice.actions\nexport default exampleSlice.reducer;",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"redux,import",
		annotation="react-redux",
		completion="import { useSelector, useDispatch } from \"react-redux\";",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use,selector",
		annotation="react-redux",
		completion="const name = useSelector((state) => state.name);",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use,dispatch",
		annotation="react-redux",
		completion="const dispatch = useDispatch();",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"redux,component",
		annotation="component react-redux",
		completion="<Provider store={store}>$0</Provider>",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
]