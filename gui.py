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
        self.window = tk.Tk()
        self.window.geometry('1000x550')
        self.window.title('GUI')


        self.map_frame = self.create_map_frame()
        self.button_frame = self.create_button_frame()

    def create_map_frame(self):
        frame = tk.Frame(self.window, height=500, bg='#FFFFFF')
        frame.pack(expand=True, fill='x')
        return frame

    #TODO: add methods to create control buttons (next/previous step, restart)
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
