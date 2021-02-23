# Pico F-Won

# Imports
import picodisplay as display
import utime
import math


# Clear the screen
def clear(background="black"):
    if background == "white":
        display.set_pen(255, 255, 255)
    else:
        display.set_pen(0, 0, 0)
    display.clear()
    display.update()

# Setup display  for use
def setup_screen():
    # Set up the display screen
    buf = bytearray(display.get_width() * display.get_height() * 2)
    display.init(buf)
    display.set_backlight(1.0)

# Draw the intro screen
def intro():
    clear("white")
    
    pico_x_base = 30  # 93 works well for centre, 70 original
    pico_y_base = 20
    display.set_pen(0, 0, 0)
    display.text("Pico", pico_x_base, pico_y_base, 0, 3)
    
    logo_x_base = 30  ## 70  original
    logo_y_base = 50
    display.set_pen(255, 0, 0)
    display.text("F-Won", logo_x_base, logo_y_base, 0, 4)
    display.set_pen(0, 0, 0)
    display.text("o", logo_x_base + 60, logo_y_base, 0, 4)
    display.set_pen(255, 255, 255)
    display.rectangle(logo_x_base + 76,logo_y_base +4,4,4)
    
    name_x_base = 140  # 100 original
    name_y_base = 100
    display.set_pen(0, 0, 0)
    display.text("By CT", name_x_base, name_y_base, 240, 3)
    display.update()
    utime.sleep(3)
    
def start():
    max_time = 3000
    
    # Lights
    clear()
    display.set_pen(255, 0, 0)  # Red lights
    for light in range(5):
        display.circle(40+(light * 40), 50, 10)
        display.update()
        utime.sleep(1)
    delay = math.fmod(utime.ticks_ms(), 4) + 1
    utime.sleep(delay)  # Random delay for lights out
    
    # Go
    display.set_pen(0, 255, 0)  # Green for GO
    # Pick side randomly for the start button, indicated by GO
    lane = math.fmod(utime.ticks_ms(), 2)
    if lane == 0:
        display.text("G0", 20, 105, 240, 2)
    else:
        display.text("G0", 200, 105, 240, 2)
    # Remove lights
    display.set_pen(0, 0, 0)
    display.rectangle(20,35,200,30)
    display.update()
    
    # Timing
    t1 = utime.ticks_ms()  # Start timer
    while True:
        utime.sleep_ms(1)
        if ( (lane == 0) and (display.is_pressed(display.BUTTON_B)) and (display.is_pressed(display.BUTTON_Y) == False) ) \
                or ( (lane == 1) and (display.is_pressed(display.BUTTON_Y)) and (display.is_pressed(display.BUTTON_B) == False) ):
            t2 = utime.ticks_ms()  # End timer
            break
        elif utime.ticks_diff(utime.ticks_ms(),t1) > max_time:  # If 3 seconds has passed
            t2 = utime.ticks_add(t1,max_time)    # End timer, set to max time even if it's slightly passed 3 seconds
            break
    # Results
    td = utime.ticks_diff(t2,t1) / 1000
    #time_text = "Reaction time: " + str(td)
    time_text = "Reaction time: " + "{:0<5}".format(str(td))
    #clear()
    display.set_pen(255, 255, 255)
    display.text(time_text, 20, 10, 240, 2)
    display.update()
    utime.sleep(5)

# Main Menu
def menu():
    clear()
    display.set_pen(255, 255, 255)
    display.text("Start Game", 115, 105, 240, 2)
    display.update()
    while True:
        utime.sleep_ms(1)
        if display.is_pressed(display.BUTTON_Y):
            break


## Main Program
while True:
    setup_screen()
    intro()
    menu()
    start()
    clear()
    display.set_backlight(0)
    #utime.sleep(5)
    break


