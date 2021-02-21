# Pico F-Won

# Imports
import picodisplay as display
import utime


# Sets up a handy function we can call to clear the screen
def clear(background="black"):
    if lower(background) = "white"
        display.set_pen(255, 255, 255)
    else:
        display.set_pen(0, 0, 0)
    display.clear()
    display.update()

def setup_screen():
    # Set up the display screen
    buf = bytearray(display.get_width() * display.get_height() * 2)
    display.init(buf)
    display.set_backlight(1.0)

# Draw the intro screen
def intro():
    clear("white")
    
    pico_x_base = 70  # 93 works well for centre
    pico_y_base = 20
    display.set_pen(0, 0, 0)
    display.text("Pico", pico_x_base, pico_y_base, 0, 3)
    
    logo_x_base = 70
    logo_y_base = 50
    display.set_pen(255, 0, 0)
    display.text("F-Won", logo_x_base, logo_y_base, 0, 4)
    display.set_pen(0, 0, 0)
    display.text("o", logo_x_base + 60, logo_y_base, 0, 4)
    display.set_pen(255, 255, 255)
    display.rectangle(logo_x_base + 76,logo_y_base +4,4,4)
    
    name_x_base = 100  # 93 works well for centre
    name_y_base = 100
    display.set_pen(0, 0, 0)
    display.text("By CT", name_x_base, name_y_base, 240, 3)
    display.update()


def menu():
    clear()
    display.set_pen(255, 255, 255)
    display.text("Start Game", 120, 110, 240, 2)
    display.update()
    menu_loop = true
    while menu_loop = true
        utime.sleep(0.01)
        if display.is_pressed(display.BUTTON_A):
            break

## Main Program

game_loop = true
while game_loop = true
    setup_screen()
    intro()
    clear()
    utime.sleep(1)
