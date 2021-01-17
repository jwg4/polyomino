from .board import Irregular


def display(piece):
    board = Irregular(piece)
   
    return board.format_tiling([piece]) 
