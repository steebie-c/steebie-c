# Display a portable bitmap image (.pbm)
from PiicoDev_SSD1306 import *
display = create_PiicoDev_SSD1306()

display.load_pbm('IMG_0013-01.pbm', 1)
display.show()