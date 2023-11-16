import random

class Color:
  @property
  def default(self): return 0x000000
  @property
  def teal(self): return 0x1ABC9C
  @property
  def dark_teal(self): return 0x11806A
  @property
  def brand_green(self): return 0x57F287
  @property
  def green(self): return 0x2ECC71
  @property
  def dark_green(self): return 0x1F8B4C
  @property
  def dark_blue(self): return 0x206694
  @property
  def purple(self): return 0x9B59B6
  @property
  def dark_purple(self): return 0x71368A
  @property
  def magenta(self): return 0xE91E63
  @property
  def dark_magenta(self): return 0xAD1457
  @property
  def gold(self): return 0xF1C40F
  @property
  def dark_gold(self): return 0xC27C0E
  @property
  def orange(self): return 0xE67E22
  @property
  def dark_orange(self): return 0xA84300
  @property
  def red(self): return 0xE74C3C
  @property
  def dark_red(self): return 0x992D22
  @property
  def lighter_grey(self): return 0x95A5A6
  @property
  def dark_grey(self): return 0x607D8B
  @property
  def light_grey(self): return 0x979C9F
  @property
  def darker_grey(self): return 0x546E7A
  @property
  def blurple(self): return 0x5865F2
  @property
  def og_blurple(self): return 0x7289DA
  @property
  def greyple(self): return 0x99AAB5
  @property
  def dark_theme(self): return 0x36393F
  @property
  def fuchsia(self): return 0xEB459E
  @property
  def yellow(self): return 0xFEE75C
  @property
  def pink(self): return 0xED4245
  def random(self): return random.choice([self.default, self.teal, self.dark_teal, self.brand_green, self.green, self.dark_green, self.dark_blue, self.purple, self.dark_purple, self.magenta, self.dark_magenta, self.gold, self.dark_gold, self.orange, self.dark_orange, self.red, self.dark_red, self.lighter_grey, self.dark_grey, self.light_grey, self.darker_grey, self.blurple, self.greyple, self.random])