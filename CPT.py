import arcade

WIDTH = 1360
HEIGHT = 710

current_screen = "menu"
ball_x = 0
spaceship_x = 0
spaceship_y = 1
spaceship_radius = 2
spaceship_color = 3

spaceship = [300, 300, 200, arcade.color.YELLOW]

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
    global ball_x
    if current_screen == "play":
        ball_x += 1


def on_draw():
    arcade.start_render()
    # Draw in here...
    if current_screen == "menu":
        arcade.draw_

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
        draw_spaceship(spaceship)
        arcade.draw_circle_filled(ball_x, 100, 30, arcade.color.BLUE)


def on_key_press(key, modifiers):
    global current_screen
    print(key)
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


def on_key_release(key, modifiers):
    pass

def on_mouse_press(x, y, button, modifiers):
    pass

def draw_spaceship(spaceship):
    arcade.draw_circle_filled(spaceship[spaceship_x], spaceship[spaceship_y], spaceship[spaceship_radius],
                              spaceship[spaceship_color])

if __name__ == '__main__':
    setup()
