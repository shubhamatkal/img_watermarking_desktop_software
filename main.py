#initial imports
from tkinter import *

#constants
FONT_NAME = "Helvetica"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
TITLE_COLOUR = "#5D12D2"
BACKGROUND_COLOR = "#FFE5E5"


#setting up tkinter window
root = Tk()
root.title('IMAGE WATERMARKING SOFTWARE')
root.config(padx=25, pady=25, bg=BACKGROUND_COLOR)
root.geometry("850x700")



# Create a Frame with a border to hold the Label
label_frame = Frame(root, relief="solid", borderwidth=2)
label_frame.pack(padx=10, pady=10)  # Add padding to control the border width
#title
title_label = Label(label_frame, text = "IMAGE WATERMARKER", font=(FONT_NAME, 48, "bold"), fg=TITLE_COLOUR, bg=BACKGROUND_COLOR)
title_label.grid(column=0, row=0 , rowspan=1, columnspan=3)







root.mainloop()