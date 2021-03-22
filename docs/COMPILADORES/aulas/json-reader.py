class Reader:
    def __init__ (self, src, pos=0):
        self.src = src.strip() # elimina os espeaços em branco no início e fim da string
        self.pos = pos

    # Lê uma substring "st" na posição atual
    def read(self, st):
        if not self.src.startswith(st, self.pos):
            raise SyntaxError(f"espera {st!r}")
        self.pos += len(st)
    
    def check_EOF(self):
        rest = self.src[self.pos:]
        if not rest == '' or rest.isspace():
            raise SyntaxError(f'espera EOF, obteve {rest!r}')

class JSAtomMixin(Reader):
    def read_number(self):
        pos_end = self.pos
        while pos_end < len(self.src) and self.src[pos_end].isdigit():
            pos_end += 1
        n = int(self.src[self.pos:pos_end])
        self.pos = pos_end
        return n

    def read_string(self):
        pos_end = self.src.find('"', self.pos + 1)
        st = self.src[self.pos + 1 : pos_end]
        self.pos = pos_end + 1
        return st

class JSONReader(JSAtomMixin, Reader):
    
    def read_value(self):
        if self.src.startswith("true", self.pos):
            self.pos += 4
            return True
        elif self.src.startswith("false", self.pos):
            self.pos += 5
            return False
        elif self.src.startswith("null", self.pos):
            self.pos += 4
            return None
        elif self.src[self.pos].isdigit():
            return self.read_number()
        elif self.src[self.pos] == '-' and self.src[self.pos + 1].isdigit():
          self.pos += 1
          return -self.read_number()
        elif self.src[self.pos] == '"':
            return self.read_string()
        elif self.src[self.pos] == "[":
            return self.read_array()
        elif self.src[self.pos] == "{":
            return self.read_object()
        else:
            raise SyntaxError(f"unexpected {self.src[self.pos:]!r}")

    def read_array(self):
        self.pos += 1
        if self.src[self.pos] == "]":
            self.pos += 1
            return []

        elements = [self.read_value()]
        while True:
            if self.src[self.pos] == "]":
                self.pos += 1
                return elements
            self.read(",")
            elements.append(self.read_value())


    def read_object(self):
        self.pos += 1
        if self.src[self.pos] == "}":
            self.pos += 1
            return {}

        elements = [self.read_pair()]
        while True:
            if self.src[self.pos] == "}":
                self.pos += 1
                return dict(elements)
            self.read(",")
            elements.append(self.read_pair())


    def read_pair(self):
        key = self.read_string()
        self.read(":")
        value = self.read_value()
        return (key, value)



def loads(text: str) -> object:
    """
    Carrega um documento JSON e retorna o valor Python correspondente.
    """
    reader = JSONReader(text)
    value = reader.read_value()
    reader.check_EOF()
    return value

# Exemplos
print(loads("true"))
print(loads("false"))
print(loads("null"))
print(loads("42"))
print(loads("-42"))
#print(loads("3.14"))
print(loads('"Hello World"'))
print(loads('[true,false,null,[1,2,3,[]]]'))
print(loads('{"answer":[1,2,[]]}'))



# Exercícios
# 1. Implemente suporte para números negativos.
# >>> print(loads("-42"))
# 2. Implemente suporte para números com parte decimal. Lembre-se que a parte
#    decimal deve ser opcional.
# >>> print(loads("3.14"))
# >>> print(loads("-10.01"))
# 3. O leitor de JSON deve aceitar espaços em branco entre elementos. Crie uma 
#    função skip_spaces() que pule espaços em branco (" ", "\n", "\r", "\t") e 
#    modifique o código para chamar esta função nos locais apropriados.
# >>> print(loads("  [ 1 , 2 , 3 ]  "))
# >>> print(loads('  { "key" : "value" }  '))