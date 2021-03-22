from lark import Lark, LarkError, Transformer
# Expressões regulares não aceitam recursão

grammar = Lark (r"""
start: "\"" char* "\""

?char : CHARS | "\\" esc

esc : "\""        -> quote
    | "\\"        -> blacklash
    | "/"         -> solidus
    | "b"         -> bs
    | "f"         -> ff
    | "n"         -> nl
    | "r"         -> cr
    | "t"         -> tab
    | "u" HEX~4   -> unicode
  
HEX : "0" .. "9" 
    | "A" .. "F"
    | "a" .. "f"

CHARS: CHAR+

CHAR  : "\u0020"    //todos os caracteres imprimíveis exceto " e \
      | "\u0021"
      | "\u0023" .. "\u005B"
      | "\u005D" .. "\uFFFF"
"""
)

class StringTransformer(Transformer):
  escape = lambda x: lambda *args: x
  quote = escape('"')
  blacklas = escape('\\')
  solidus = escape('/')
  bs = escape('\b')
  ff = escape('\f')
  nl = escape('\n')
  cr = escape('\r')
  tab = escape('\t')

  def unicode(self, args):
    a, b, c, d = args
    return chr((a << 12) + (b << 8) + (c << 4) + d)
  
  def start (self, parts):
    return ''.join(parts)
  
  def HEX(self, tk):
    return int(tk, 16)

def is_string(src: str) -> bool:
  try:
    grammar.parse(src)
    return True
  except LarkError:
    return False

def parse_string(src: str) -> str:
  ast = grammar.parse(src)
  transformer = StringTransformer()
  return transformer.transform(ast)

exemplos = r"""
"hello\u0020\"world\"!\n(or not)"
"""
for st in exemplos.strip().splitlines():
  print("In: ", st)
  if not is_string(st):
    print('**erro**')
  else:
    print('Out: ', repr(parse_string(st)))  