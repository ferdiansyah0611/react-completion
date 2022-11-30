import sublime

def snippet_init_mui():
	text = ""
	text += 'import { useMemo } from "react";\n'
	text += 'import { useSelector } from "react-redux";\n'
	text += 'import { ThemeProvider } from "@mui/material/styles";\n'
	text += 'import { CssBaseline } from "@mui/material";\n'
	text += 'import palette from "@service/color";\n\n'
	text += 'function Mui(props) {\n'
	text += '\tconst stateTheme = useSelector((state) => state.theme);\n\n'
	text += '\tconst theme = useMemo(() => {\n'
	text += '\t\treturn palette(stateTheme.theme);\n'
	text += '\t}, [stateTheme.theme]);\n'
	text += '\treturn (\n'
	text += '\t\t<>\n'
	text += '\t\t\t<CssBaseline />\n'
	text += '\t\t\t<ThemeProvider theme={theme}>{props.children}</ThemeProvider>\n'
	text += '\t\t</>\n'
	text += '\t);\n'
	text += '}\n\n'
	text += 'export default Mui;'
	return text

mui = [
	sublime.CompletionItem(
		"use,theme",
		annotation="mui",
		completion="const theme = useTheme();",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use,mediaquery",
		annotation="mui",
		completion="const fullScreen = useMediaQuery(theme.breakpoints.down('md'));",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"mui,import,styles",
		annotation="mui",
		completion="import { $0 } from \"@mui/material/styles\";",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"mui,import",
		annotation="mui",
		completion="import { $0 } from \"@mui/material\";",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"mui,import,icon",
		annotation="mui",
		completion="import NameIcon$0 from \"@mui/icons-material/Name\";",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"mui,snippet,init",
		annotation="mui snippet",
		completion=snippet_init_mui(),
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
]