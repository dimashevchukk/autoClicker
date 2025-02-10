import tkinter
import UI
import Clicker

if __name__ == '__main__':
    root = tkinter.Tk()
    clicker = Clicker.AutoClicker()
    app = UI.App(root, clicker)
    root.mainloop()
