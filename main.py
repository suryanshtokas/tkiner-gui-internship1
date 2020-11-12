import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self, width=400, height=100)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, width=400, height=100)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

class Main():
    def __init__(self):
        # Make the main window named root
        self.root = tk.Tk()

        # Set the basic properties of the main window
        self.root.title('EVAC GUI') # title
        self.root.geometry('1356x731+100+80') # geometry

        # Load all the images using ImageTk
        self.bg = ImageTk.PhotoImage(file='images/Evac Original.bmp')
        # Evac 1
        self.bg_1 = ImageTk.PhotoImage(file='images/EVAC1-ATC1.bmp')
        self.bg_2 = ImageTk.PhotoImage(file='images/EVAC1-ATC2.bmp')
        self.bg_3 = ImageTk.PhotoImage(file='images/EVAC1-ATC3.bmp')
        self.bg_4 = ImageTk.PhotoImage(file='images/EVAC1-ATC4.bmp')
        self.bg_5 = ImageTk.PhotoImage(file='images/EVAC1-ATC7.bmp')
        self.bg_6 = ImageTk.PhotoImage(file='images/EVAC1-ATC8.bmp')
        self.bg_7 = ImageTk.PhotoImage(file='images/EVAC1-ATC9.bmp')
        self.bg_8 = ImageTk.PhotoImage(file='images/EVAC1-ATC10.bmp')
        self.bg_9 = ImageTk.PhotoImage(file='images/EVAC1-ATC11.bmp')
        self.bg_10 = ImageTk.PhotoImage(file='images/EVAC1-ATC12.bmp')
        self.bg_11 = ImageTk.PhotoImage(file='images/EVAC1-ATC13.bmp')
        self.bg_12 = ImageTk.PhotoImage(file='images/EVAC1-ATC14.bmp')
        self.bg_13 = ImageTk.PhotoImage(file='images/EVAC1-ATC15.bmp')
        # Evac 2
        self.bg_14 = ImageTk.PhotoImage(file='images/EVAC2-ATC1.bmp')
        self.bg_15 = ImageTk.PhotoImage(file='images/EVAC2-ATC2.bmp')
        self.bg_16 = ImageTk.PhotoImage(file='images/EVAC2-ATC3.bmp')
        self.bg_17 = ImageTk.PhotoImage(file='images/EVAC2-ATC4.bmp')
        self.bg_18 = ImageTk.PhotoImage(file='images/EVAC2-ATC7.bmp')
        self.bg_19 = ImageTk.PhotoImage(file='images/EVAC2-ATC8.bmp')
        self.bg_20 = ImageTk.PhotoImage(file='images/EVAC2-ATC9.bmp')
        self.bg_21 = ImageTk.PhotoImage(file='images/EVAC2-ATC10.bmp')
        self.bg_22 = ImageTk.PhotoImage(file='images/EVAC2-ATC11.bmp')
        self.bg_23 = ImageTk.PhotoImage(file='images/EVAC2-ATC12.bmp')
        self.bg_24 = ImageTk.PhotoImage(file='images/EVAC2-ATC13.bmp')
        self.bg_25 = ImageTk.PhotoImage(file='images/EVAC2-ATC14.bmp')
        self.bg_26 = ImageTk.PhotoImage(file='images/EVAC2-ATC15.bmp')
        # Evac 3
        self.bg_27 = ImageTk.PhotoImage(file='images/EVAC3-ATC2.bmp')
        self.bg_28 = ImageTk.PhotoImage(file='images/EVAC3-ATC3.bmp')
        self.bg_29 = ImageTk.PhotoImage(file='images/EVAC3-ATC4.bmp')
        self.bg_30 = ImageTk.PhotoImage(file='images/EVAC3-ATC7.bmp')
        self.bg_31 = ImageTk.PhotoImage(file='images/EVAC3-ATC8.bmp')
        self.bg_32 = ImageTk.PhotoImage(file='images/EVAC3-ATC10.bmp')
        self.bg_33 = ImageTk.PhotoImage(file='images/EVAC3-ATC12.bmp')
        self.bg_34 = ImageTk.PhotoImage(file='images/EVAC3-ATC13.bmp')
        self.bg_35 = ImageTk.PhotoImage(file='images/EVAC3-ATC14.bmp')
        # Evac 4
        self.bg_36 = ImageTk.PhotoImage(file='images/EVAC4-ATC2.bmp')
        self.bg_37 = ImageTk.PhotoImage(file='images/EVAC4-ATC7.bmp')
        self.bg_38 = ImageTk.PhotoImage(file='images/EVAC4-ATC13.bmp')

        
        # Make a canvas for the background image(s)
        self.canvas = tk.Canvas(self.root, width=1356, height=731) 
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)
        
        # Show the background image on the canvas
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor='nw', image=self.bg)

        # Create the selection button
        self.selection_button = ttk.Button(self.root, text='Selection', command=self.select)
        self.selection_button.place(x=1240, y=10)

        # Create the quit button
        self.quit_button = tk.Button(self.root, text='Quit', command=self.quit, bg='red')
        self.quit_button.place(x=1270, y=650)

        # Run the GUI
        self.run()

    def select(self):
        self.options_list = [
            'EVAC1-ATC1',
            'EVAC1-ATC2',
            'EVAC1-ATC3',
            'EVAC1-ATC4',
            'EVAC1-ATC7',
            'EVAC1-ATC8',
            'EVAC1-ATC9',
            'EVAC1-ATC10',
            'EVAC1-ATC11',
            'EVAC1-ATC12',
            'EVAC1-ATC13',
            'EVAC1-ATC14',
            'EVAC1-ATC15',
            # Evac 2
            'EVAC2-ATC1',
            'EVAC2-ATC2',
            'EVAC2-ATC3',
            'EVAC2-ATC4',
            'EVAC2-ATC7',
            'EVAC2-ATC8',
            'EVAC2-ATC9',
            'EVAC2-ATC10',
            'EVAC2-ATC11',
            'EVAC2-ATC12',
            'EVAC2-ATC13',
            'EVAC2-ATC14',
            'EVAC2-ATC15',
            # Evac 3
            'EVAC3-ATC2',
            'EVAC3-ATC3',
            'EVAC3-ATC4',
            'EVAC3-ATC7',
            'EVAC3-ATC8',
            'EVAC3-ATC10',
            'EVAC3-ATC12',
            'EVAC3-ATC13',
            'EVAC3-ATC14',
            # Evac 4
            'EVAC4-ATC2',
            'EVAC4-ATC7',
            'EVAC4-ATC13',
        ]
        self.select_window = tk.Toplevel()
        self.select_window.geometry('425x100+150+150')
        self.select_window_frame = ScrollableFrame(self.select_window, width=400, height=100)
        self.select_window_frame.pack()
        self.option_variable = tk.IntVar()
        self.option_variable.set(100)
        for val, option in enumerate(self.options_list):
            tk.Radiobutton(self.select_window_frame.scrollable_frame, text=option, value=val+1, variable=self.option_variable, command=self.update_image).pack()

    def update_image(self):
        self.select_window.destroy()
        exec(f'self.canvas.itemconfig(self.image_on_canvas, image=self.bg_{self.option_variable.get()})')

    def quit(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()



Main()
