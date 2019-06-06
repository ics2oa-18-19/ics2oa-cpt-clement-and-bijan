import arcade

WIDTH = 1360
HEIGHT = 710

current_screen = "menu"
spaceship_x = 355
spaceship_y = 100
press_up = False
press_down = False
press_left = False
press_right = False


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    global spaceship_y, spaceship_x, press_up, press_down, press_left, press_right

    if spaceship_y <= HEIGHT:
        if press_up == True:
            spaceship_y += 10
    if  spaceship_y >= 1:
        if press_down == True:
            spaceship_y -= 10
    if spaceship_x >= 1:
        if press_left == True:
            spaceship_x -= 10
    if spaceship_x <= WIDTH:
        if press_right == True:
            spaceship_x += 10



def on_draw():
    arcade.start_render()
    # Draw in here...
    if current_screen == "menu":
        arcade.draw_text("Game", 50, HEIGHT - 50, arcade.color.WHITE)
        arcade.draw_text("Press I for instructions", 50, HEIGHT - 70, arcade.color.WHITE)
        arcade.draw_text("P to play", 50, HEIGHT - 90, arcade.color.WHITE)

    elif current_screen == "instructions":
        arcade.draw_text("Instruction Screen", 50, HEIGHT - 50, arcade.color.WHITE)
        arcade.draw_text("W = up", 50, HEIGHT - 70, arcade.color.WHITE)
        arcade.draw_text("A = left", 50, HEIGHT - 90, arcade.color.WHITE)
        arcade.draw_text("S = down", 50, HEIGHT - 110, arcade.color.WHITE)
        arcade.draw_text("D = right", 50, HEIGHT - 130, arcade.color.WHITE)
        arcade.draw_text("Press ESC to go back to menu", 50, HEIGHT - 150, arcade.color.WHITE)

    elif current_screen == "play":
        arcade.draw_text("Play Screen", 50, HEIGHT - 50, arcade.color.WHITE)
        arcade.draw_text("Press ESC to go back to menu", 50, HEIGHT - 70, arcade.color.WHITE)
        draw_spaceship(spaceship_x, spaceship_y)

def on_key_press(key, modifiers):
    global current_screen, spaceship_x, spaceship_y, press_up, press_down, press_left, press_right
    if current_screen == "menu":
        if key == arcade.key.I:
            current_screen = "instructions"
        elif key == arcade.key.P:
            current_screen = "play"

    elif current_screen == "instructions":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"

    elif current_screen == "play":
        if key == arcade.key.P:
            current_screen = "play"
        if key == arcade.key.ESCAPE:
            current_screen = "menu"
        if key == arcade.key.W:
            press_up = True
        if key == arcade.key.A:
            press_left = True
        if key == arcade.key.S:
            press_down = True
        if key == arcade.key.D:
            press_right = True


def on_key_release(key, modifiers):
    global current_screen, spaceship_x, spaceship_y, press_up, press_down, press_left, press_right
    if current_screen == "play":
        if key == arcade.key.W:
            press_up = False
        if key == arcade.key.A:
            press_left = False
        if key == arcade.key.S:
            press_down = False
        if key == arcade.key.D:
            press_right = False



def on_mouse_press(x, y, button, modifiers):
    pass

def draw_spaceship(spaceship_x, spaceship_y):
    arcade.draw_circle_filled(spaceship_x + 15, spaceship_y + 52.5, 7.5, arcade.color.WHITE)
    arcade.draw_circle_filled(spaceship_x + 15, spaceship_y + 6.5, 7.5, arcade.color.WHITE)
    arcade.draw_circle_filled(spaceship_x - 15, spaceship_y + 6.5, 7.5, arcade.color.RED)
    arcade.draw_circle_filled(spaceship_x - 15, spaceship_y + 52.5, 7.5, arcade.color.RED)
    arcade.draw_rectangle_filled(spaceship_x, spaceship_y + 7, 30, 15, arcade.color.GRAY)
    arcade.draw_rectangle_filled(spaceship_x, spaceship_y + 53, 30, 15, arcade.color.GRAY)
    arcade.draw_triangle_filled(spaceship_x , spaceship_y, spaceship_x, spaceship_y + 60, spaceship_x + 90, spaceship_y + 30, arcade.color.GRAY)
    arcade.draw_rectangle_filled(spaceship_x + 25, spaceship_y + 30, 30, 15, arcade.color.BLACK_OLIVE)
    arcade.draw_circle_filled(spaceship_x + 40, spaceship_y + 29.5, 7.5, arcade.color.BLACK_OLIVE)

if __name__ == '__main__':
    setup()




