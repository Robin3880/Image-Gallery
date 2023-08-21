import customtkinter
from PIL import Image
import os

app = customtkinter.CTk() 
app.title("Image-Gallery")
app.geometry("1090x650")

def image_click_event(img):
    print(f"Image clicked: {img}")

ImagesFolder = []

for filename in os.listdir("Images"):
    ImagesFolder.append(os.path.join("Images", filename))

images = {}
for num, img_path in enumerate(ImagesFolder):
    image = customtkinter.CTkImage(dark_image=Image.open(img_path), size=(80, 80))
    _, img_name = os.path.split(img_path)
    label = customtkinter.CTkLabel(app, text=img_name, image=image, compound="top", fg_color="transparent")
    row = num // 9
    column = num % 9
    label.grid(row=row, column=column, pady=20, padx=20)   
    label.bind("<Button-1>", lambda event, img=img_name: image_click_event(img))
    label.configure(cursor="hand2")  # Set cursor to hand when hovering over the label

    images[img_name] = (image, label)
    
    app.resizable(False, False)
    app.grid_propagate(False)
app.mainloop()