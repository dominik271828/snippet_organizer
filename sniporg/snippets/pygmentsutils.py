from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

def formatCode(code, lexerAlias):
    formatter = HtmlFormatter(style='sas', full=True)
    return highlight(code, get_lexer_by_name(lexerAlias), formatter)