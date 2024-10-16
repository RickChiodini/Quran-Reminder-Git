# -*- coding: utf-8 -*-
import tkinter as tk
import requests
import os

class App(tk.Tk):

        BACKGROUND_1 = "#2b4f35"   #Dark green
        BACKGROUND_2 = "#941f1f"   #Red/Maroon
        BACKGROUND_3 = "white"
        BACKGROUND_4 = "#fce803"   #Yellow
        BACKGROUND_5 = "black"

        FOREGROUND_1 = "white"
        FOREGROUND_2 = "black"
        FOREGROUND_3 = "#3e6913"   #Green

        QURANIC_FONT = "fonts/AmiriQuran-Regular.ttf"
        
        def __init__(self):
                super().__init__()
                self.title("Quran Verse Reminder")
                self.geometry("300x300")
                self.resizable(False, False)
                self.configure(bg=self.BACKGROUND_1)

                #Set up app icon based on OS relative path to work with pyinstaller
                self.base_path = os.path.dirname(__file__)
                self.icon_path = os.path.join(self.base_path, 'quran.ico')
                self.iconbitmap(self.icon_path)

                #Textbox which displays the Quranic ayaat
                self.verse_textbox = tk.Text(
                        self,
                        font=(self.QURANIC_FONT, 14),
                        background=self.BACKGROUND_1,
                        foreground=self.FOREGROUND_1,
                        wrap="word",
                        state="disabled",
                        height=5,
                        border=0,
                        borderwidth=0
                        )
                self.verse_textbox.pack(padx=10, pady=10, expand=True, fill="both")

                #Add a tag to justify Arabic text to right
                self.verse_textbox.tag_configure("right", justify="right")

                #Label displaying the suar:ayaat numbers
                self.ayah_number_label = tk.Label(
                        self,
                        text="",
                        font=("Arial", 14),
                        bg=self.BACKGROUND_1,
                        fg=self.FOREGROUND_1
                )
                self.ayah_number_label.pack(pady=5, expand=True, fill="both")

                #First calling to update the textbox and label after 5 seconds
                self.verse_textbox.after(5000, self.update_textbox)
                self.ayah_number_label.after(5000, self.update_ayah_label)

                #Pics to use for popup menu
                self.theme_1 = tk.PhotoImage(file="pics/green_white.png")
                self.theme_2 = tk.PhotoImage(file="pics/red_white.png")
                self.theme_3 = tk.PhotoImage(file="pics/black_white.png")
                self.theme_4 = tk.PhotoImage(file="pics/yellow_green.png")
                self.theme_5 = tk.PhotoImage(file="pics/white_black.png")

                #Menu and color-themed options
                self.color_theme_menu = tk.Menu(self, tearoff=0)

                self.color_theme_menu.add_command(
                        label="Green / White",
                        image=self.theme_1,
                        compound="left",
                        command=self.set_theme_1
                )

                self.color_theme_menu.add_command(
                        label="Red / White",
                        image=self.theme_2,
                        compound="left",
                        command=self.set_theme_2
                )

                self.color_theme_menu.add_command(
                        label="Black / White",
                        image=self.theme_3,
                        compound="left",
                        command=self.set_theme_3
                )

                self.color_theme_menu.add_command(
                        label="Yellow / Green",
                        image=self.theme_4,
                        compound="left",
                        command=self.set_theme_4
                )

                self.color_theme_menu.add_command(
                        label="White / Black",
                        image=self.theme_5,
                        compound="left",
                        command=self.set_theme_5
                )

                #Binding both textbox & label to the right-click context menu popup
                self.verse_textbox.bind('<Button-3>', self.open_popup)
                self.ayah_number_label.bind('<Button-3>', self.open_popup)


                self.mainloop()

        #Methods

        #API call to generate a random ayah, then passing the key as an argument to fetch the text
        def get_verse(self):
                response = requests.get("https://api.quran.com/api/v4/verses/random")
                self.verse_key = response.json()["verse"]["verse_key"]
                verse_req = requests.get(f"https://api.quran.com/api/v4/quran/verses/uthmani?verse_key={self.verse_key}")
                verse = verse_req.json()["verses"][0]["text_uthmani"]
                
                #Calls an update function to change ayah text and number every 15 minutes
                self.verse_textbox.after(900000, self.update_textbox)
                self.ayah_number_label.after(900000, self.update_ayah_label)

                return verse

        #Function that deletes current textbox text and updates it with new ayah text
        def update_textbox(self):
                self.verse_textbox.config(state="normal")
                self.verse_textbox.delete(1.0, "end")
                text = self.get_verse()
                self.verse_textbox.insert(1.0, text)
                self.verse_textbox.tag_add("right", "1.0", "end")
                self.verse_textbox.config(state="disabled")

        #Function to update the ayah number label
        def update_ayah_label(self):
                self.ayah_number_label.config(text=self.verse_key)

        #Function to open the color theme popup menu
        def open_popup(self, event):
                try:
                        self.color_theme_menu.tk_popup(event.x_root, event.y_root)
                finally:
                        self.color_theme_menu.grab_release()

        #Functions to change root, textbox, and label backgrounds and foregrounds based on themes
        def set_theme_1(self):
                self.configure(bg=self.BACKGROUND_1)
                self.verse_textbox.config(
                        background=self.BACKGROUND_1, foreground=self.FOREGROUND_1
                        )
                self.ayah_number_label.config(
                        background=self.BACKGROUND_1, foreground=self.FOREGROUND_1
                        )
                
        def set_theme_2(self):
                self.configure(bg=self.BACKGROUND_2)
                self.verse_textbox.config(
                        background=self.BACKGROUND_2, foreground=self.FOREGROUND_1
                        )
                self.ayah_number_label.config(
                        background=self.BACKGROUND_2, foreground=self.FOREGROUND_1
                        )
                
        def set_theme_3(self):
                self.configure(bg=self.BACKGROUND_5)
                self.verse_textbox.config(
                        background=self.BACKGROUND_5, foreground=self.FOREGROUND_1
                        )
                self.ayah_number_label.config(
                        background=self.BACKGROUND_5, foreground=self.FOREGROUND_1
                        )
                
        def set_theme_4(self):
                self.configure(bg=self.BACKGROUND_4)
                self.verse_textbox.config(
                        background=self.BACKGROUND_4, foreground=self.FOREGROUND_3
                        )
                self.ayah_number_label.config(
                        background=self.BACKGROUND_4, foreground=self.FOREGROUND_3
                        )
                
        def set_theme_5(self):
                self.configure(bg=self.BACKGROUND_3)
                self.verse_textbox.config(
                        background=self.BACKGROUND_3, foreground=self.FOREGROUND_2
                        )
                self.ayah_number_label.config(
                        background=self.BACKGROUND_3, foreground=self.FOREGROUND_2
                        )
                
if __name__ == "__main__":
        app = App()