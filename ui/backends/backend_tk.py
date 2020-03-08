import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.text = tk.Text(self)
        self.text.pack()
        self.text.insert("1.0", "Hello, world\n")
        self.text.insert("2.0", "Henlo, hooman")
        self.text.tag_add("sel", "1.7", "1.12")
        self.text.tag_add("sel", "2.7", "2.12")
        self.text.focus_force()

#app = SampleApp()
#app.mainloop()