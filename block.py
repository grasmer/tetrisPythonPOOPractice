from colors import Colors
import pygame
from position import Position
    
#Clase padre
class Block():
    def __init__(self, id):
        self.id = id
        self.cells = {}  #Diccionari vacio que tendra la composicion del block
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0 #Posicion que tendra el block
        self.colors = Colors.get_cell_colors()  #Obtencion de colores de la case colors

    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles
    
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0
    
    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) -  1

    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()  #Muestra la rotacion del block
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, offset_y + tile.row * self.cell_size,
                                    self.cell_size -1, self.cell_size -1 )
            pygame.draw.rect(screen, self.colors[self.id], tile_rect) #Dibuja cada cuadro(tile=mosaico) con el color y la posicion
