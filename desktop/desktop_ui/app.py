import tkinter as tk
from tkinter import ttk, messagebox
from core import (
    PasswordGenerator,
    DEFAULT_LENGTH,
    DEFAULT_INCLUDE_UPPERCASE,
    DEFAULT_INCLUDE_DIGITS,
    DEFAULT_INCLUDE_SPECIAL_CHARS
)


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Infolojo Password Generator")
        self.root.geometry("450x400")
        self.root.resizable(False, False)

        self.style_widgets()
        self.create_header()
        self.create_password_options()
        self.create_generate_button()
        self.create_result_area()

    def style_widgets(self):
        style = ttk.Style()
        style.configure("Header.TLabel", font=("Helvetica", 14, "bold"))
        style.configure("Option.TLabel", font=("Helvetica", 10))
        style.configure("Result.TLabel", font=("Helvetica", 12, "bold"))

    def create_header(self):
        header_frame = ttk.Frame(self.root, padding="10")
        header_frame.pack(fill="x")

        title_label = ttk.Label(
            header_frame,
            text="Infolojo Password Generator",
            style="Header.TLabel"
        )
        title_label.pack()

        subtitle_label = ttk.Label(
            header_frame,
            text="Generate secure passwords with custom options",
            font=("Helvetica", 9)
        )
        subtitle_label.pack()

    def create_password_options(self):
        options_frame = ttk.LabelFrame(self.root, text="Password Options", padding="10")
        options_frame.pack(fill="x", padx=20, pady=10)

        length_frame = ttk.Frame(options_frame)
        length_frame.pack(fill="x", pady=5)

        ttk.Label(length_frame, text="Password Length:", style="Option.TLabel").pack(side="left")

        self.length_var = tk.IntVar(value=DEFAULT_LENGTH)
        length_spinbox = ttk.Spinbox(
            length_frame,
            from_=4,
            to=64,
            textvariable=self.length_var,
            width=10
        )
        length_spinbox.pack(side="right")

        self.uppercase_var = tk.BooleanVar(value=DEFAULT_INCLUDE_UPPERCASE)
        uppercase_check = ttk.Checkbutton(
            options_frame,
            text="Include Uppercase Letters (A-Z)",
            variable=self.uppercase_var
        )
        uppercase_check.pack(anchor="w", pady=2)

        self.digits_var = tk.BooleanVar(value=DEFAULT_INCLUDE_DIGITS)
        digits_check = ttk.Checkbutton(
            options_frame,
            text="Include Numbers (0-9)",
            variable=self.digits_var
        )
        digits_check.pack(anchor="w", pady=2)

        self.special_var = tk.BooleanVar(value=DEFAULT_INCLUDE_SPECIAL_CHARS)
        special_check = ttk.Checkbutton(
            options_frame,
            text="Include Special Characters (!@#$%)",
            variable=self.special_var
        )
        special_check.pack(anchor="w", pady=2)

    def create_generate_button(self):
        button_frame = ttk.Frame(self.root, padding="10")
        button_frame.pack(fill="x")

        self.generate_button = ttk.Button(
            button_frame,
            text="Generate Password",
            command=self.generate_password
        )
        self.generate_button.pack()

    def create_result_area(self):
        result_frame = ttk.LabelFrame(self.root, text="Generated Password", padding="10")
        result_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.password_label = ttk.Label(
            result_frame,
            text="",
            font=("Helvetica", 11, "bold"),
            wraplength=380,
            foreground="green"
        )
        self.password_label.pack(pady=5)

        button_frame = ttk.Frame(result_frame)
        button_frame.pack(pady=5)

        self.copy_button = ttk.Button(
            button_frame,
            text="Copy to Clipboard",
            command=self.copy_to_clipboard,
            state="disabled"
        )
        self.copy_button.pack(side="left", padx=5)

        self.generate_another_button = ttk.Button(
            button_frame,
            text="Generate Another",
            command=self.generate_password,
            state="disabled"
        )
        self.generate_another_button.pack(side="left", padx=5)

    def generate_password(self):
        length = self.length_var.get()

        if not self.uppercase_var.get() and not self.digits_var.get() and not self.special_var.get():
            messagebox.showwarning(
                "Warning",
                "You must select at least one character type.\nUsing default settings."
            )
            self.uppercase_var.set(True)
            self.digits_var.set(True)
            self.special_var.set(True)

        generator = PasswordGenerator(
            length=length,
            include_uppercase=self.uppercase_var.get(),
            include_digits=self.digits_var.get(),
            include_special_chars=self.special_var.get()
        )

        result = generator.generate()
        password = result.replace("Generated password: ", "")

        self.password_label.config(text=password, foreground="green")
        self.copy_button.config(state="normal")
        self.generate_another_button.config(state="normal")

    def copy_to_clipboard(self):
        password = self.password_label.cget("text")
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")


def run():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    run()