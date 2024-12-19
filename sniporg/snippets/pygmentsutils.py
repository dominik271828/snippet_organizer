from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import HtmlFormatter

def formatC(code):
    formatter = HtmlFormatter(style='sas', full=True)
    #print(formatter.get_style_defs())
    return highlight(code, CLexer(), formatter)