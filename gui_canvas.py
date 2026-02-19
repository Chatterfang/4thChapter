"""
NOTE: 2nd try at the gui file via tkinter, currently primary option for GUI

tkinter GUI file to visualise algorithms contained within this project
"""
#libs
import tkinter as tk


class AStarGUI:

    def __init__(self):
        #tkinter setup

        #window
        self.window = tk.Tk()
        self.window.geometry('1000x550')
        self.window.title('GUI Canvas')

        #canvas
        self.canvas = tk.Canvas(self.window, bg='white', height=550, width=1000)


        #button window on canvas
        #self.canvas_btn_window = self.canvas.create_window(525, 500, height=50, width=1000)

        #temp section

        #//temp section

        self.canvas.pack()

    # methods for creating buttons



    def run(self):
        self.window.mainloop()


def main():
    gui = AStarGUI()
    gui.run()

if __name__ == '__main__':
    main()