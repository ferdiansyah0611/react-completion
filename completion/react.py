import sublime

react = [
	sublime.CompletionItem(
		"use,state",
		annotation="react",
		completion="const [state, setState] = useState({});",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use,effect",
		annotation="react",
		completion="useEffect(() => {\n\t\n}, []);",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use,memo",
		annotation="react",
		completion="const name = useMemo(() => {\n\treturn\n}, []);",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use,callback",
		annotation="react",
		completion="const name = useCallback(() => {\n\t\n}, []);",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use,ref",
		annotation="react",
		completion="const element = useRef(null)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use,reducer",
		annotation="react",
		completion="const [state, dispatch] = useReducer((value, action) => {\n\tswitch(action.type) {\n\t\tcase \"example\":\n\t\t\treturn {test: false}\n\t\tdefault:\n\t\t\treturn value;\n\t}\n}, {\n\ttest: true,\n})",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use,transition",
		annotation="react",
		completion="const [isPending, startTransition] = useTransition();",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use,id",
		annotation="react",
		completion="const id = useId();",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use,context",
		annotation="react",
		completion="const value = useContext(MyContext);",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"flush",
		annotation="react",
		completion="flushSync(() => {\n\t\n});",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"context",
		annotation="react",
		completion="const nameContext = createContext({\n\t\n});",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"suspense",
		annotation="react",
		completion="<Suspense fallback={<div>loading...</div>}></Suspense>",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"lazy",
		annotation="react",
		completion="const name = lazy(() => import(\"$0\"));",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"component,function",
		annotation="react",
		completion="function name(){\n\treturn(\n\t\t<div></div>\n\t)\n};",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"component,class",
		annotation="react",
		completion="class Example extends Component{\n\tconstructor(props) {\n\t\tsuper(props);\n\t\tthis.state = {};\n\t}\n\tcomponentDidMount(){}\n\tcomponentWillUnmount(){}\n\trender() {\n\t\treturn(\n\t\t\t<div>example</div>\n\t\t)\n\t}\n}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"react,import",
		annotation="import react",
		completion="import { useState, useEffect, useMemo, useCallback, useRef } from \"react\";",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"react,map",
		annotation="react",
		completion="{state.map((item, i) => (\n\t\n))}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
]