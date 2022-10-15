# PiicoDev SSD1306 demo code
# Show off some features of the PiicoDev OLED driver

import math
from PiicoDev_SSD1306 import PiicoDev_SSD1306
from PiicoDev_Unified import sleep_ms

display = create_PiicoDev_SSD1306()

# Text and numbers
for counter in range(0,101):
    display.fill(0)
    display.text("PiicoDev",30,20, 1)
    display.text(str(counter),50,35, 1)
    display.show()
sleep_ms(500)


# Bargraphs
thick = 15 # thickness of the bar
for val in range(WIDTH+1):
    display.fill(0)
    display.text("Bargraphs", 20, 10, 1)
    display.fill_rect(0, HEIGHT-thick, val, thick, 1) # Filled bar graph
    display.rect(0, int(HEIGHT-2*thick - 5), int(val/2), thick, 1) # no-fill
    display.show()
sleep_ms(500)


# Plots
graphSin = display.graph2D()
graphCos = display.graph2D()
for x in range(128):
    s = int(math.sin(x/10.0)*HEIGHT+HEIGHT+30)
    c = int(math.cos(x/10.0)*HEIGHT+HEIGHT+30)
    display.fill(0)
    display.text("Plots", 50, 10, 1)
    display.updateGraph2D(graphSin,s)
    display.updateGraph2D(graphCos,c)
    display.show()
sleep_ms(1000)
