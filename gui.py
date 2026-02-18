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
        self.window.geometry('800x600')
        self.window.title('GUI')


    def run(self):
        self.window.mainloop()



def main():
    gui = AStarGUI()
    gui.run()

if __name__ == '__main__':
    main()
