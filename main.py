import tkinter

screen = tkinter.Tk()
screen.title("Mile to Km converter")
screen.configure(width=500, height=300)
screen.config(padx=50, pady=100)

is_equal_to = tkinter.Label(text="Is equal to", font=("arial", 24, "bold"))
is_equal_to.config(padx=0, pady=0)
is_equal_to.grid(row=1, column=0)
miles = tkinter.Label(text="Miles", font=("arial", 24, "bold"))
miles.config(padx=0, pady=0)
miles.grid(row=0, column=2)
km = tkinter.Label(text="Km", font=("arial", 24, "bold"))
km.config(padx=0, pady=0)
km.grid(row=1, column=2)
result = tkinter.Label(text="0", font=("arial", 24, "bold"))
result.config(padx=0, pady=0)
result.grid(row=1, column=1)

inp = tkinter.Entry()
inp.grid(row=0, column=1)


def converter():
    x = float(inp.get())
    x *= 1.60934
    x = str(x)
    result["text"] = x


calculator = tkinter.Button(text="Calculate", command= converter)
calculator.config(padx=0, pady=0)
calculator.grid(row=2, column=1)


screen.mainloop()