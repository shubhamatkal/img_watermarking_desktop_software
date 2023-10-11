#initial imports
from tkinter import *
from tkinter.filedialog import askopenfilename

#constants
FONT_NAME = "Helvetica"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
TITLE_COLOUR = "#5D12D2"
BACKGROUND_COLOR = "#FFE5E5"
photo_toggle = True

#setting up tkinter window
root = Tk()
root.title('IMAGE WATERMARKING SOFTWARE')
root.config(padx=25, pady=25, bg=BACKGROUND_COLOR)
root.geometry("810x700")

#image file path
img_file = ""

#writing some functions
def select_file():
    global img_file
    img_file = askopenfilename()
    print(f"✓ User has selected the file: {img_file}")
    print("...")

def toggle():
    global photo_toggle
    if photo_toggle:
        photo_button.config(image=text)
        a_label.config(text="TEXT WATERMARK")
        photo_toggle = False
    else:
        photo_button.config(image=photo)
        a_label.config(text="PHOTO WATERMARK")
        photo_toggle = True



#title
title_label = Label( text = "IMAGE WATERMARKER", font=(FONT_NAME, 48, "bold"),
                     fg=TITLE_COLOUR, bg=BACKGROUND_COLOR)
title_label.grid(column=0, row=0 , rowspan=1, columnspan=3)

#creating button to select the image
select_img_button = Button(root, text="upload image", font=20, width=15, command=select_file)
select_img_button.grid(column=0, row=1,columnspan=2,padx=25, pady=25)


#defining toggle images
photo = PhotoImage(file="resources/PHOTO WATERMARK.png")
text = PhotoImage(file="resources/TEXT WATERMARK.png")

new_width = 100
new_height = 40
# Resize the image using the subsample method
photo = photo.subsample(photo.width() // new_width, photo.height() // new_height)
text = text.subsample(text.width() // new_width, text.height() // new_height)

#create toggle button
photo_button = Button(root,image=photo, bd=0, command=toggle)
photo_button.grid(column=0 , row=2, columnspan=2, pady=25, padx=25)

#todo create text label showing what the suer has selected
a_label = Label(text="Photo Watermarker")
a_label.grid(column=0 , row=3, columnspan=2)

#todo create text label for choosing photo watermark image
b_label = Label(text="choose the image using below button")
b_label.grid(column=0 , row=4)

#todo create text label for choosing text watermark image
t_label = Label(text="type the text in below cell")
t_label.grid(column=1 , row=4)








root.mainloop()
