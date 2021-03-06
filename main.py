#!/usr/bin/env python3
import tcod

#importing from actions and input_handlers
from engine import Engine
from entity import Entity
from input_handlers import EventHandler
from procgen import generate_dungeon

def main() -> None:
    #screen dimensions
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    #using a font from the png
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    #receive events and process them
    event_handler = EventHandler()

    #initalising player and npc from entity class
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    game_map = generate_dungeon(map_width, map_height)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    #creates the screen
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Dungeon Crawler",
        vsync=True,
    )  as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            #console that we will be drawing to
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)

if __name__ == "__main__":
    main()