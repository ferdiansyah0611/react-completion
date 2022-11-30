import sublime

router = [
	sublime.CompletionItem(
		"router,import",
		annotation="import react-router",
		completion="import { BrowserRouter, Route, Routes } from \"react-router-dom\";",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use,navigate",
		annotation="react-router",
		completion="const to = useNavigate();",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use,params",
		annotation="react-router",
		completion="const param = useParams();",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use,location",
		annotation="react-router",
		completion="const location = useLocation();",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use,searchparams",
		annotation="react-router",
		completion="const [searchParams, setSearchParams] = useSearchParams();",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
]