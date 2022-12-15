import tkinter
from tkinter.font import BOLD
import customtkinter

theme = "light"
font = "Helvetica"
customtkinter.set_appearance_mode(theme)
customtkinter.set_default_color_theme("blue")
class Settings(customtkinter.CTk):
    WIDTH = 480
    HEIGHT = 290

    def __init__(self):
        super().__init__()

        self.title("Settings")
        self.geometry(f"{Settings.WIDTH}x{Settings.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.closing)

        frame_1 = customtkinter.CTkFrame(master=self)
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)


        label_1 = customtkinter.CTkLabel(master=frame_1,text = "Font Settings", justify=tkinter.LEFT)
        label_1.configure(font=(font, 20, tkinter.UNDERLINE, BOLD))
        label_1.pack(pady=12, padx=10)

        optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["Arial", "Coolvetica", "Helvetica"])
        optionmenu_1.pack(pady=12, padx=10)

        label_2 = customtkinter.CTkLabel(master=frame_1,text = "Appearance Mode", justify=tkinter.LEFT)
        label_2.configure(font=(font, 20, tkinter.UNDERLINE, BOLD))
        label_2.pack(pady=12, padx=10)

        optionmenu_2 = customtkinter.CTkOptionMenu(frame_1, values=["Light", "Dark"], command = self.change_appearance)
        optionmenu_2.pack(pady=12, padx=10)

        optionmenu_1.set("Arial")
        optionmenu_2.set("Light")


    def change_appearance(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def change_theme(self, new_colour_theme):
        customtkinter.set_default_color_theme(new_colour_theme)
    def applychanges(self):
        print("woahhh!")

    def closing(self):
        self.destroy()

if __name__ == "__main__":
    settings = Settings()
    settings.mainloop()