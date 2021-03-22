import pyxel

def update():
  ...

def draw():
  pyxel.cls(4)

pyxel.init(180, 120)
pyxel.run(update, draw)