#initial imports
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import Image , ImageDraw , ImageFont , UnidentifiedImageError

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
watermark_file = ""

#writing some functions
def select_file():
    global img_file
    global im
    img_file = askopenfilename()
    im = Image.open(img_file)
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

def select_watermark():
    global watermark_file
    global logo
    watermark_file = askopenfilename()
    logo = Image.open(watermark_file)
    print(f"✓ User has selected the water mark image: {watermark_file}")
    print("...")

#todo create text watermark function
def text_watermark1(img_input, text_watermark, xy_pos):
    edit_image = ImageDraw.Draw(im)
    colour =  (135, 206, 235)
    font_watermark = ImageFont.truetype("arial.ttf", 200)
    edit_image.text(xy_pos, text_watermark, font=font_watermark, fill=colour)
    # image.save(img_output)



def text_watermark():
    if im == "":
        messagebox.showerror("No image found , kindly select the image first")
    else:
        text_input_value = text_input.get()
        text_watermark1(im,text_watermark=text_input_value, xy_pos=(100, 100) )
        messagebox.showinfo("Complete", "Successfully watermarked!")

# Upload logo - check if the file is a supported format
# def upload_logo():
#     global logo
#     logo_name = askopenfilename()
#     try:
#         logo = Image.open(logo_name)
#     except UnidentifiedImageError:
#         messagebox.showinfo(title="Error", message="Unsupported file format.\n Please open an image file.")

# Watermark image with logo
def watermark_logo():
    try:
        wm_logo = logo
    except NameError:
        messagebox.showinfo(title="Error", message="Please upload a logo")
    else:
        im.paste(wm_logo)
        messagebox.showinfo(title="Success", message="The image has a watermark logo on it now.")


#download function
def download():
    save_name = filedialog.asksaveasfile(filetypes=[('Images', '*.png')], defaultextension='*.png')
    im.save(save_name.name)
    im.show()

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


#todo creating button to select the image for watermark
select_watermark_button = Button(root, text="watermark image", font=20, width=15, command=select_watermark)
select_watermark_button.grid(column=0, row=5,padx=25, pady=25)

#todo creating button to apply the watermark to the image
apply_watermark_button = Button(root, text="apply watermark", font=20, width=15, command=watermark_logo)
apply_watermark_button.grid(column=0, row=6,padx=25, pady=25)

#todo creating button to apply the watermark to the image
apply_text_button = Button(root, text="apply text watermark", font=20, width=15, command=text_watermark)
apply_text_button.grid(column=1, row=6,padx=25, pady=25)

#todo create a input cell to the hold of watermark text
text_input = Entry(root)
text_input.grid(column=1, row=5)

#todo creating a download image button
apply_text_button = Button(root, text="Download Image", font=20, width=15, command=download)
apply_text_button.grid(column=0, row=7,padx=25, pady=25, columnspan=2)

#todo create text label to indicate the preview of image
t_label = Label(text="PREVIEW OF IMAGE")
t_label.grid(column=2, row=1)


#todo image preview
# Load an image using the PhotoImage class
image = PhotoImage(file="resources/PHOTO WATERMARK.png")  # Replace "image.gif" with your image file path
#set dimensions of image
new_width = 220
new_height = 220
# Resize the image using the subsample method
image = image.subsample(image.width() // new_width, image.height() // new_height)

# Create a label to display the image
image_label = Label(root, image=image)
image_label.grid(column=2, row=2, columnspan=1, rowspan=5)






root.mainloop()
