from tkinter import Button
import random
from settings import *


class Cell:
    all_cells = []

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_button = None
        self.x = x
        self.y = y
        self.all_cells.append(self)

    @staticmethod
    def random_mines():
        mined_cells = random.sample(
            Cell.all_cells, mines_num
        )
        for x in mined_cells:
            x.is_mine = True

    def create_button(self, location):
        btn = Button(
            location,
            width=14,  # width/(grid_size**2),
            height=4,  # height/(grid_size**2),
        )
        btn.bind('<Button-1>', self.left_click)  # left click
        btn.bind('<Button-3>', self.right_click)  # right click
        self.cell_button = btn

    def left_click(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    #  Showing how many mines surrounding the cell
    def show_cell(self):
        pass


    def show_mine(self):
        self.cell_button.configure(bg='red')

    def right_click(self, event):
        print(event)
