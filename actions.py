#creating sub-classes for action
class Action:
    pass

#if ESC has been pressed
class EscapeAction(Action):
    pass

#player movement
class MovementAction(Action): 
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy