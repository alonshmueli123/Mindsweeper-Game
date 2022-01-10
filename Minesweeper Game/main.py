from tkinter import *
from cell import Cell
from settings import *


root = Tk()
root.geometry(f'{width}x{height}')
root.configure(bg='black')
root.title("Minesweeper")
root.resizable(False, False)


# Creating the frames
top_frame = Frame(
    root,
    bg='black',
    width=width,
    height=height/4
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='black',
    width=width/4,
    height=height
)
left_frame.place(x=0, y=height/4)

main_frame = Frame(
    root,
    bg='black',
    width=(width/4) * 3,
    height=(height/4) * 3
)
main_frame.place(x=width/4, y=height/4)


# Creating the cells
for x in range(grid_size):
    for y in range(grid_size):
        c1 = Cell(x, y)
        c1.create_button(main_frame)
        c1.cell_button.grid(
            column=x, row=y
        )

Cell.random_mines()  #Picking mines
for c in Cell.all_cells:
    print(c.is_mine)

root.mainloop()

