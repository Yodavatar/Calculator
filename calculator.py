#Coding : utf-8
#Coding by Limo
#Licensed code CC BY-NC-SA 4.0
#Application : calculator

from tkinter import *
from math import *

class MyWindow(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.string = ""

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        
        self.grid_columnconfigure(0, weight=1, uniform="same_group")
        self.grid_columnconfigure(1, weight=1, uniform="same_group")
        self.grid_columnconfigure(2, weight=1, uniform="same_group")
        self.grid_columnconfigure(3, weight=1, uniform="same_group")
        self.grid_columnconfigure(4, weight=1, uniform="same_group")

        # On définit quelques éléments de style pour nos boutons.
        self.default_button_style = {
            "bg": "#595959", "fg": "white", "highlightthickness": 0,
            "font": ("Arial", 25, "bold")
        }
        self.equal_button_style = self.default_button_style | {"bg": "#f05a2D"}
        self.default_button_grid = {"padx": 2, "pady": 2, "sticky": "nsew"}

        """First line"""

        self.result = Label(self, text="...", anchor='e',bg="#a2af77", fg="white", font=("Arial", 25), padx=10)
        self.result.grid(column=0, row=0, columnspan=5, **self.default_button_grid)

        """Second line"""

        self.nbr_7 = Button(self, text="7", command=self.add7, **self.default_button_style)
        self.nbr_7.grid(column=0, row=1, **self.default_button_grid)

        self.nbr_8 = Button(self, text="8", command=self.add8, **self.default_button_style)
        self.nbr_8.grid(column=1, row=1, **self.default_button_grid)

        self.nbr_9 = Button(self, text="9", command=self.add9, **self.default_button_style)
        self.nbr_9.grid(column=2, row=1, **self.default_button_grid)

        self.delete = Button(self, text="DEL", command=self.supprimer, **self.default_button_style)
        self.delete.grid(column=3, row=1, **self.default_button_grid)

        self.zero = Button(self, text="C", command=self.C, **self.default_button_style)
        self.zero.grid(column=4, row=1, **self.default_button_grid)

        """Third line"""

        self.nbr_4 = Button(self, text="4", command=self.add4, **self.default_button_style)
        self.nbr_4.grid(column=0, row=2, **self.default_button_grid)

        self.nbr_5 = Button(self, text="5", command=self.add5, **self.default_button_style)
        self.nbr_5.grid(column=1, row=2, **self.default_button_grid)

        self.nbr_6 = Button(self, text="6", command=self.add6, **self.default_button_style)
        self.nbr_6.grid(column=2, row=2, **self.default_button_grid)

        self.addi = Button(self, text="+", command=self.add, **self.default_button_style)
        self.addi.grid(column=3, row=2, **self.default_button_grid)

        self.sous = Button(self, text="-", command=self.sou, **self.default_button_style)
        self.sous.grid(column=4, row=2, **self.default_button_grid)

        """Fourth line"""

        self.nbr_1 = Button(self, text="1", command=self.add1, **self.default_button_style)
        self.nbr_1.grid(column=0, row=3, **self.default_button_grid)

        self.nbr_2 = Button(self, text="2", command=self.add2, **self.default_button_style)
        self.nbr_2.grid(column=1, row=3, **self.default_button_grid)

        self.nbr_3 = Button(self, text="3", command=self.add3, **self.default_button_style)
        self.nbr_3.grid(column=2, row=3, **self.default_button_grid)

        self.multip = Button(self, text="*", command=self.multi, **self.default_button_style)
        self.multip.grid(column=3, row=3, **self.default_button_grid)

        self.divi = Button(self, text="/", command=self.div, **self.default_button_style)
        self.divi.grid(column=4, row=3, **self.default_button_grid)

        """Fifth line"""
        
        self.nbr_0 = Button(self, text="0", command=self.add0, **self.default_button_style)
        self.nbr_0.grid(column=0, row=4,columnspan=3, **self.default_button_grid)

        self.virg = Button(self, text=".", command=self.virgule, **self.default_button_style)
        self.virg.grid(column=3, row=4, **self.default_button_grid)

        self.calcul = Button(self, text="=", command=self.calcule, **self.equal_button_style)
        self.calcul.grid(column=4, row=4, **self.default_button_grid)

        """Background"""

        self.configure(bg="#333333", padx=10, pady=10)
        self.geometry("400x500")

        """Window"""

        self.title("Calculator")
        self.iconbitmap("calculator.ico")

    def calcule(self) -> None: 
        """Operation calcul"""
        self.string = str(eval(self.string))
        self.result.configure(text = self.string)

    def Quitter(self) -> None:
        """Close prog"""
        self.destroy()

    def C(self):
        """Reset"""
        self.string = ""
        self.result.config(text="...")

    def supprimer(self) -> None:
        """Del last operation"""
        if len(self.string) <= 1:
            self.string = ""
            self.result.config(text="...")
        else:
            self.string = self.string[0:len(self.string)-1]
            self.result.config(text=self.string)

    def add0(self) -> None:
        """add 0"""
        self.string+=str(0)
        self.result.config(text=self.string)

    def add1(self) -> None:
        """add 1"""
        self.string+=str(1)
        self.result.config(text=self.string)

    def add2(self) -> None:
        """add 2"""
        self.string+=str(2)
        self.result.config(text=self.string)

    def add3(self) -> None:
        """add 3"""
        self.string+=str(3)
        self.result.config(text=self.string)

    def add4(self) -> None:
        """add 4"""
        self.string+=str(4)
        self.result.config(text=self.string)

    def add5(self) -> None:
        """add 5"""
        self.string+=str(5)
        self.result.config(text=self.string)

    def add6(self) -> None:
        """add 6"""
        self.string+=str(6)
        self.result.config(text=self.string)

    def add7(self) -> None:
        """add 7"""
        self.string+=str(7)
        self.result.config(text=self.string)

    def add8(self) -> None:
        """add 8"""
        self.string+=str(8)
        self.result.config(text=self.string)

    def add9(self) -> None:
        """add 9"""
        self.string+=str(9)
        self.result.config(text=self.string)

    def virgule(self) -> None:
        """add ."""
        self.string+="."
        self.result.config(text=self.string)

    def multi(self) -> None:
        """add *"""
        self.string+="*"
        self.result.config(text=self.string)

    def add(self) -> None:
        """add +"""
        self.string+="+"
        self.result.config(text=self.string)

    def sou(self) -> None:
        """add -"""
        self.string+="-"
        self.result.config(text=self.string)

    def div(self) -> None:
        """add /"""
        self.string+="/"
        self.result.config(text=self.string)

window = MyWindow()
window.mainloop()

#Coding : utf-8
#Coding by Limo
#Licensed code CC BY-NC-SA 4.0
#Application : calculator
