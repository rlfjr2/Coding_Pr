import tkinter as tk

root = tk.Tk()
root.resizable(False,True)
root.geometry('300x400')
root.title('견우와직녀를살려주세요!!')
root.configure(bg='#0ff0ff')

label = tk.Label(root, text='abcd')
label.grid()

root.mainloop()
