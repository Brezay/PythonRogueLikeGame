from typing import Tuple

class Entity:
    #generic object to represent players, enemies, items, etc
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char #what will be used to represent entity
        self.color = color #colour when drawing entity

    #modifies entity position
    def move(self, dx: int, dy: int) -> None:
        #move the entity by a given amount
        self.x += dx
        self.y += dy