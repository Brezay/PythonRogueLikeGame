from typing import Optional

#the use of tcod event system
import tcod.event

#imports the Action class and its subclasses
from actions import Action, EscapeAction, MovementAction

#subclass of EventDispatch that allows us to send an event to its proper method
#based on the type of event
class EventHandler(tcod.event.EventDispatch[Action]):
    #in event of "X" on window being pressed
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()
    
    #receives keys pressed
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        #if no valid key
        action: Optional[Action] = None

        #holds the key pressed 
        key = event.sym
        
        #on what key is pressed, describe direction for character
        if key  == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy = 0)

        #if escape key is pressed
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()
        
        return action