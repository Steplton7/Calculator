from tkinter import *


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 28, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)

        btns = [
            "AC", "(", ")", "/",
            "1", "2", "3", "*",
            "4", "5", "6", "-",
            "7", "8", "9", "+",
            "0", ".", "="
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            if bt != "0":
                bg = "grey"
                if x < 300 and y < 220:
                    bg = "#FFF"
                elif x > 300:
                    bg = "orange"
                Button(text=bt, bg=bg,
                       font=("Times New Roman", 25),
                       command=com).place(x=x, y=y,
                                          width=115,
                                          height=79)
                x += 117
                if x > 400:
                    x = 10
                    y += 81
            elif bt == "0":
                Button(text=bt, bg="grey",
                       font=("Times New Roman", 25),
                       command=com).place(x=x, y=y,
                                          width=232,
                                          height=79)
                x += 234
                if x > 400:
                    x = 10
                    y += 81

    def logicalc(self, operation):
        if operation == "AC":
            self.formula = ""

        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.iconbitmap("C:\python_equals\Calculator\Calculator.ico")
    root.geometry("485x550+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
