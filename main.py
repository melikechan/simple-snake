from textual.app import App


class SnakeGameApp(App):
    """A snake game written in Textual."""

    BINDINGS = [
        ("w,up", "move_up", "Move up"),
        ("s,down", "move_down", "Move down"),
        ("a,left", "move_left", "Move left"),
        ("d,right", "move_right", "Move right"),
        ("p", "pause", "Pause the game"),
        ("q", "quit", "Quit the game"),
    ]


if __name__ == "__main__":
    game = SnakeGameApp()
    game.run()
