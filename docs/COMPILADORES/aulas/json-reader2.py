import Lark 
src = ""
pos = 0


def loads(text: str) -> object:
    """
    Carrega um documento JSON e retorna o valor Python correspondente.
    """
    global src, pos

    src = text
    pos = 0
    value = read_value()
    rest = src[pos:]
    if rest == '' or rest.isspace():
        return value
    else:
        raise SyntaxError(f'espera EOF, obteve {rest!r}')


def read_value():
    global pos

    if src.startswith("true", pos):
        pos += 4
        return True
    elif src.startswith("false", pos):
        pos += 5
        return False
    elif src.startswith("null", pos):
        pos += 4
        return None
    elif src[pos] == '-':
        pos += 1
        return -read_number()
    elif src[pos].isdigit():
        return read_number()
    elif src[pos] == '"':
        return read_string()
    elif src[pos] == "[":
        return read_array()
    elif src[pos] == "{":
        return read_object()
    else:
        raise SyntaxError(f"unexpected {src[pos:]!r}")


def read_number():
    global pos

    pos_end = pos
    while pos_end < len(src) and src[pos_end].isdigit():
        pos_end += 1
    n = int(src[pos:pos_end])
    pos = pos_end
    return n


def read_string():
    global pos

    pos_end = src.find('"', pos + 1)
    st = src[pos + 1 : pos_end]
    pos = pos_end + 1
    return st


def read_array():
    global pos

    pos += 1
    if src[pos] == "]":
        pos += 1
        return []

    elements = [read_value()]
    while True:
        if src[pos] == "]":
            pos += 1
            return elements
        read(",")
        elements.append(read_value())


def read_object():
    global pos

    pos += 1
    if src[pos] == "}":
        pos += 1
        return {}

    elements = [read_pair()]
    while True:
        if src[pos] == "}":
            pos += 1
            return dict(elements)
        read(",")
        elements.append(read_pair())


def read_pair():
    key = read_string()
    read(":")
    value = read_value()
    return (key, value)


def read(st):
    global pos

    if not src.startswith(st, pos):
        raise SyntaxError(f"espera {st!r}")
    pos += len(st)


# Exemplos
print(loads("true"))
print(loads("false"))
print(loads("null"))
print(loads("42"))
print(loads("-42"))
print(loads('"Hello World"'))
print(loads("[true,false,null,[1,2,3,[]]]"))
print(loads('{"answer":[1,2,[]]}'))