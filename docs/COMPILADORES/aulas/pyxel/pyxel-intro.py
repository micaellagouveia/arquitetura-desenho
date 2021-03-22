import pyxel
from math import sqrt
import random

class Ball:
  def __init__(self, x=90, y=10, radius=5, velocity=None) -> None:
    self.x = x

    if y is None:
      y = random.uniform(0, 20)
    self.y = y

    self.radius = radius

    if velocity is None:
      velocity = random.uniform(0.5, 1.5) 
    self.velocity = velocity
    
  def click(self, x, y):
    dx = x - self.x
    dy = y - self.y
    if sqrt(dx**2 + dy**2) < self.radius:
      self.velocity = 0

  def draw(self):
    color = pyxel.COLOR_WHITE
    if self.velocity == 0:
      color = pyxel.COLOR_RED

    pyxel.circ(self.x, self.y, self.radius, color)
  
  def update(self):
    self.y += self.velocity


def update():

  for ball in balls:
    if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
      ball.click(pyxel.mouse_x, pyxel.mouse_y)
    ball.update()


def draw():
  pyxel.cls(pyxel.COLOR_BLACK)

  for ball in balls:
    ball.draw()

  if all(ball.velocity == 0 for ball in balls):
    pyxel.text(70, 90, "Parabens!", pyxel.COLOR_WHITE)

balls = [Ball(10 +i) for i in range(0, 170, 25)]
pyxel.init(180, 120)
pyxel.mouse(True)
pyxel.run(update, draw)