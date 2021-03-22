import re
# Expressões regulares não aceitam recursão

STRING = re.compile(r'"(( |!|[#-[]|[\]-\U0010FFFF])+|\\(["\\\/bfnrt]|u[0-9a-zA-Z]{4}))*"')

def is_string(src: str) -> bool:
  return bool(STRING.fullmatch(src))

def parse_string(src: str) -> str:

  if is_string(src):
    return eval(src)
  else:
    raise SyntaxError

exemplos = r"""
"hello\u0020\"world\"!\n(or not)"
"""
for st in exemplos.strip().splitlines():
  print("In: ", st)
  if not is_string(st):
    print('**erro**')
  else:
    print('Out: ', repr(parse_string(st)))  