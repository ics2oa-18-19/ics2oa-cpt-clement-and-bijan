import arcade

WIDTH = 1360
HEIGHT = 710

current_screen = "menu"
spaceship_x = HEIGHT / 2
spaceship_y = 300
spaceship_radius = 200
spaceship_color = arcade.color.RED
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

    if press_up == True:
        spaceship_y += 10
    if press_down == True:
        spaceship_y -= 10
    if press_left == True:
        spaceship_x -= 10
    if press_right == True:
        spaceship_x += 10



def on_draw():
    arcade.start_render()
    # Draw in here...
    if current_screen == "menu":
        arcade.draw_text("Game", WIDTH /2-50, HEIGHT/2, arcade.color.WHITE)
        arcade.draw_text("Press I for instructions", WIDTH/2-50, HEIGHT/2-20, arcade.color.WHITE)
        arcade.draw_text("P to play", WIDTH / 2-50, HEIGHT / 2-40, arcade.color.WHITE)

    elif current_screen == "instructions":
        arcade.draw_text("Instruction Screen", WIDTH/2-50, HEIGHT/2, arcade.color.WHITE)
        arcade.draw_text("W = up", WIDTH / 2 - 50, HEIGHT / 2-20, arcade.color.WHITE)
        arcade.draw_text("A = left", WIDTH / 2 - 50, HEIGHT / 2-40, arcade.color.WHITE)
        arcade.draw_text("S = down", WIDTH / 2 - 50, HEIGHT / 2-60, arcade.color.WHITE)
        arcade.draw_text("D = right", WIDTH / 2 - 50, HEIGHT / 2-80, arcade.color.WHITE)
        arcade.draw_text("Press ESC to go back to menu", WIDTH / 2 - 50, HEIGHT / 2 - 100, arcade.color.WHITE)

    elif current_screen == "play":
        arcade.draw_text("Play Screen", WIDTH/ 2-50, HEIGHT / 2, arcade.color.WHITE)
        arcade.draw_text("Press ESC to go back to menu", WIDTH / 2 - 50, HEIGHT / 2 - 20, arcade.color.WHITE)
        arcade.draw_circle_filled(spaceship_x, spaceship_y, spaceship_radius, spaceship_color)


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



if __name__ == '__main__':
    setup()



