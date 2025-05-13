import tkinter as tk
from tkinter import font

# Main calculator class
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.configure(bg="#1e1e1e")
        self.expression = ""

        self.custom_font = font.Font(family="Helvetica", size=20, weight="bold")

        # Entry display
        self.input_text = tk.StringVar()
        self.input_frame = tk.Frame(self.root, bg="#1e1e1e")
        self.input_frame.pack(pady=10)

        self.input_field = tk.Entry(self.input_frame, textvariable=self.input_text, font=self.custom_font,
                                    bg="#252526", fg="#ffffff", bd=0, justify="right", insertbackground="#ffffff", width=16)
        self.input_field.grid(row=0, column=0, ipadx=8, ipady=25)
        self.input_field.focus()

        # Buttons frame
        self.buttons_frame = tk.Frame(self.root, bg="#1e1e1e")
        self.buttons_frame.pack()

        # Button layout
        buttons = [
            ("C", 1, 0), ("←", 1, 1), ("%", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2, 2)
        ]

        for (text, row, col, colspan) in [(*btn, 1) if len(btn) == 3 else btn for btn in buttons]:
            self.create_button(text, row, col, colspan)

    def create_button(self, text, row, column, colspan):
        button = tk.Button(self.buttons_frame, text=text, width=5 * colspan, height=2,
                           bg="#333", fg="#fff", font=self.custom_font, bd=0,
                           activebackground="#555", activeforeground="#fff",
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=column, columnspan=colspan, padx=5, pady=5, sticky="nsew")

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "←":
            self.expression = self.expression[:-1]
        elif char == "=":
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        else:
            self.expression += str(char)

        self.input_text.set(self.expression)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()