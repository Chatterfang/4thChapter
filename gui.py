"""
tkinter GUI file to visualise algorithms contained within this project
"""
import tkinter as tk

"""
TBD:
arguments:
    - fixed window size vs. automatic size based on input array
"""
class AStarGUI:

    def __init__(self):
        # tkinter setup

        #WINDOW
        self.window = tk.Tk()
        self.window.geometry('1000x550')
        self.window.title('GUI')

        #self.window.grid_columnconfigure(1, weight=1)

        #display
        self.map_frame = self.create_map_frame()

        #TODO: figure out how to draw inside of the map frame (draw squares/grid

        # check to see the dimensions of map frame
        self.square_label = self.create_square_label()
        #--------------

        #buttons
        self.button_frame = self.create_button_frame()
        self.create_buttons()
        self.button_frame.rowconfigure(0, weight=1)

    # DISPLAY SECTION
    def create_map_frame(self):
        frame = tk.Frame(self.window, height=500, bg='#FFFFFF')
        frame.pack(expand=True, fill='x')
        return frame

    def create_square_label(self):
        label = tk.Label(self.map_frame, text='kek', bg='#B00B69')
        label.pack()
        return label

    # BUTTONS SECTION
    #TODO: add methods to create control buttons (next/previous step, restart)
    def create_next_btn(self):
        btn = tk.Button(self.button_frame, text='>>')
        btn.grid(row=0, column=3, columnspan=1, sticky=tk.NS)

    def create_previous_btn(self):
        btn = tk.Button(self.button_frame, text='<<')
        btn.grid(row=0, column=0, columnspan=1, sticky=tk.NS)

    def create_play_btn(self):
        btn = tk.Button(self.button_frame, text='Play')
        btn.grid(row=0, column=2, columnspan=1, sticky=tk.NS)

    def create_pause_btn(self):
        btn = tk.Button(self.button_frame, text='Pause')
        btn.grid(row=0, column=1, columnspan=1, sticky=tk.NS)

    def create_buttons(self):
        self.create_next_btn()
        self.create_previous_btn()
        self.create_play_btn()
        self.create_pause_btn()

    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def run(self):
        self.window.mainloop()



def main():
    gui = AStarGUI()
    gui.run()

if __name__ == '__main__':
    main()
