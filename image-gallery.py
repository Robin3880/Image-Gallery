import customtkinter
from PIL import Image
import os

class ToplevelWindow(customtkinter.CTkToplevel):             #this is the image window opened when an image is pressed
    def __init__(self, *args, img, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title(f"{img}")
        with Image.open(f"Images/{img}") as imeg:
            width, height = imeg.size

        # Create a custom image object
        image = customtkinter.CTkImage(dark_image=Image.open(f"Images/{img}"), size=(width, height))
        self.label = customtkinter.CTkLabel(self, text="", image=image)
        self.label.pack(padx=0, pady=0)
        self.geometry(f"{width}x{height}")

class App(customtkinter.CTk):                                #this is the image gallery window
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Image-Gallery")
        self.geometry("1090x650")

        self.toplevel_window = None
            
        ImagesFolder = []

        # Get the list of image files in the "Images" folder
        for filename in os.listdir("Images"):
            ImagesFolder.append(os.path.join("Images", filename))

        for num, img1 in enumerate(ImagesFolder):
            # Create a custom image object for each image file
            image = customtkinter.CTkImage(dark_image=Image.open(f"{img1}"), size=(80, 80))
            start, img = img1.split("\\")
            label = customtkinter.CTkLabel(self, text=f"{img}", image=image, compound="top", fg_color="transparent")
            row = num // 9
            column = num % 9
            label.grid(row=row, column=column, pady=20, padx=20)                                
            label.bind("<Button-1>", lambda event, img=img: self.open_toplevel(img))
            label.configure(cursor="hand2") # Set cursor to hand when hovering over the label
            
        self.grid_propagate(False)

    def open_toplevel(self,img):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self, img=img)  # Create window if it's None or destroyed
            self.toplevel_window.attributes('-topmost', True)
        else:
            self.toplevel_window.attributes('-topmost', True)  # If window exists, focus it

# Create an instance of the App class and run the application
app = App()
app.resizable(False, False)
app.mainloop()