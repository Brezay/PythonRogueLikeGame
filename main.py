#!/usr/bin/env python3
import tcod

#importing from actions and input_handlers
from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:
    #screen dimensions
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    #using a font from the png
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    #receive events and process them
    event_handler = EventHandler()

    #creates the screen
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Dungeon Crawler",
        vsync=True,
    )  as context:
        #console that we will be drawing to
        root_console = tcod.Console(screen_width,screen_height, order="F")

        #the game loop
        while True:
            #where to place character
            root_console.print(x=player_x, y=player_y, string="@")

            #updates what we see on screen
            context.present(root_console)

            #need to clear console or will show previous characters still on screen
            root_console.clear()

            #to exit the program not crashing it
            for event in tcod.event.wait():
                #sends the event to its proper place
                action = event_handler.dispatch(event)

                #skip over if no key is pressed
                if action is None:
                    continue

                #causes the symbol to move
                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                #if escape is pressed, exit
                elif isinstance(action, EscapeAction):
                    raise SystemExit()

if __name__ == "__main__":
    main()