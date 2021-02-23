# Pico F-Won

# Imports
import picodisplay as display
import utime
import math
import random


# Clear the screen
def clear_screen(background="black"):
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
    clear_screen("white")
    # Display "Pico"
    pico_x_base = 30  # 93 works well for centre, 70 original
    pico_y_base = 20
    display.set_pen(0, 0, 0)
    display.text("Pico", pico_x_base, pico_y_base, 0, 3)
    # Display "F-Won"
    logo_x_base = 30  ## 70  original
    logo_y_base = 50
    display.set_pen(255, 0, 0)
    display.text("F-Won", logo_x_base, logo_y_base, 0, 4)
    display.set_pen(0, 0, 0)
    display.text("o", logo_x_base + 60, logo_y_base, 0, 4)
    display.set_pen(255, 255, 255)
    display.rectangle(logo_x_base + 76,logo_y_base +4,4,4)
    # Display "By CT"
    name_x_base = 140  # 100 original
    name_y_base = 100
    display.set_pen(0, 0, 0)
    display.text("By CT", name_x_base, name_y_base, 240, 3)
    display.update()
    utime.sleep(3)
    
    
def time_user(side,max_time):
    # Time user's reactions
    t1 = utime.ticks_ms()  # Start timer
    while True:
        utime.sleep_ms(1)
        if ( (side == "<") and (display.is_pressed(display.BUTTON_B)) and (display.is_pressed(display.BUTTON_Y) == False) ) \
                or ( (side == ">") and (display.is_pressed(display.BUTTON_Y)) and (display.is_pressed(display.BUTTON_B) == False) ):
            t2 = utime.ticks_ms()  # End timer
            break
        elif utime.ticks_diff(utime.ticks_ms(),t1) > max_time:  # If 3 seconds has passed
            t2 = utime.ticks_add(t1,max_time)    # End timer, set to max time even if it's slightly passed 3 seconds
            break
    # Calculate reaction time and display results
    reaction_time = utime.ticks_diff(t2,t1) / 1000
    time_text = "T: " + "{:0<5}".format(str(reaction_time))  # Display reaction time to 3 decimals (ms)
    clear_screen()
    display.set_pen(255, 255, 255)
    display.text(time_text, 50, 30, 240, 4)
    display.update()
    utime.sleep(1)  # Pause to read reaction time
    return reaction_time
    
    
def start(lap_timer, max_time):
    
    # Draw the red start lights one at a time
    clear_screen()
    display.set_pen(255, 0, 0)
    for light in range(5):
        display.circle(40+(light * 40), 50, 10)
        display.update()
        utime.sleep(1)
    delay = math.fmod(utime.ticks_ms(), 4) + 1
    utime.sleep(delay)  # Random delay before go lights out
    
    # Remove lights
    display.set_pen(0, 0, 0)
    display.rectangle(20,35,200,30)
    # No effect until next display.update()

    # Click the correct side to "Go"
    display.set_pen(0, 255, 0)  # Green for GO
    # Pick side randomly for the start button, indicated by GO
    #sides = ["<",">"]
    #chosen_side = sides[int(math.fmod(utime.ticks_ms(), 2))]
    side = random.choice(["<",">"])
    if side == "<":
        display.text("G0", 20, 105, 240, 2)
    else:
        display.text("G0", 200, 105, 240, 2)
    # Cover up start lights and display "Go"
    display.update()
    
    # Time the user's reaction
    lap_timer += time_user(side,max_time)
    return lap_timer
    
    
def next_turn(lap_timer, max_time, direction, lead_time):
    clear_screen()
    utime.sleep_ms(500)
    # Show straight-ahead until a turn
    display.set_pen(255, 255, 0)
    display.text("^", 118, 42, 240, 4)
    display.text("/\\", 110, 50, 240, 4)
    #display.text("", 110, 70, 240, 4)
    display.update()
    # Prepare the turn
    display.set_pen(0, 0, 0)
    display.clear()  # Chosen to not clear screen immediately
    turn_text = direction * 3
    # Display large chevrons indicating turn direction
    display.set_pen(255, 255, 255)
    display.text(turn_text, 100, 50, 240, 4)
    # Label correct key with chevrons for the turn
    display.set_pen(0, 255, 0)
    if direction == "<":
        display.text(turn_text, 20, 105, 240, 2)
    else:
        display.text(turn_text, 200, 105, 240, 2)
    # Wait before displaying the chevrons, simulates waiting to arrive at the corner
    utime.sleep(lead_time)
    display.update()  # Show the turn direction now
    # Time the user's reaction
    lap_timer += time_user(direction,max_time)
    return lap_timer
    

# Main Menu
def menu():
    clear_screen()
    display.set_pen(255, 255, 255)
    display.text("Select Track:", 20, 20, 240, 2)
    display.text("  Spa", 20, 50, 240, 2)
    display.text("  Monaco", 20, 70, 240, 2)
    display.set_pen(0, 255, 0)
    display.text("Start Game", 115, 105, 240, 2)
    display.update()
    while True:
        utime.sleep_ms(1)
        if display.is_pressed(display.BUTTON_Y):
            break


## Main Program
while True:
    lap_timer = 0
    max_time = 2000
    
    setup_screen()
    #intro()
    menu()
    # Each race section adds time to the race_timer
    lap_timer = start(lap_timer, max_time)
    
    ## Testing a single turn
    lead_time = 5
    direction = ">"
    lap_timer = next_turn(lap_timer, max_time, direction, lead_time)
    ##
    
    clear_screen()
    display.set_backlight(0)
    #utime.sleep(5)
    break


