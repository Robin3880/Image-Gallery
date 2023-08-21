import customtkinter
from PIL import Image
import os

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, img, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title(f"{img}")
        with Image.open(f"Images/{img}") as imeg:
            width, height = imeg.size

        image = customtkinter.CTkImage(dark_image=Image.open(f"Images/{img}"), size=(width, height))
        self.label = customtkinter.CTkLabel(self, text="", image=image)
        self.label.pack(padx=0, pady=0)
        self.geometry(f"{width}x{height}")

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Image-Gallery")
        self.geometry("1090x650")

        self.toplevel_window = None
            
        ImagesFolder = []

        for filename in os.listdir("Images"):
            ImagesFolder.append(os.path.join("Images", filename))

        images = {}
        for num, img1 in enumerate(ImagesFolder):
            image = customtkinter.CTkImage(dark_image=Image.open(f"{img1}"), size=(80, 80))
            start, img = img1.split("\\")
            label = customtkinter.CTkLabel(self, text=f"{img}", image=image, compound="top", fg_color="transparent")
            row = num // 9
            column = num % 9
            label.grid(row=row, column=column, pady=20, padx=20)                                
            label.bind("<Button-1>", lambda event, img=img: self.open_toplevel(img))
            label.configure(cursor="hand2")
            images[img] = (image, label, img1)

                
        self.grid_propagate(False)

    def open_toplevel(self,img):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self, img=img)
            self.toplevel_window.attributes('-topmost', True)
        else:
            self.toplevel_window.attributes('-topmost', True)

            
app = App()
app.resizable(False, False)
app.mainloop()
