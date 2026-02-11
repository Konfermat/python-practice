from rich.console import Console
from rich.text import Text

console = Console()

text = 'Line of text\nLine of text two\nLine of text three' 
seq = '\x1b[J\x1b[6n\x1b[1A\x1b[6n'

print(text + seq)
