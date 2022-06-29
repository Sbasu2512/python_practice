#Proprietary content. © Great Learning. All Rights Reserved. Unauthorized use or distribution prohibited.
import tkinter as tk
# Python Tkinter library for rich GUI applications
from tkinter import messagebox
from tkinter import filedialog

# Base class which abstracts all the fonts and face of the text.
class Richtext:

    def __init__(self):
        self.bold_val = ""
        self.italic_val = ""

    def render_text(self, textarea, bold_val, italic_val):
        pass

    def swap_bold_state(self, textarea, text_obj_lst):
        pass

    def swap_italic_state(self, textarea, text_obj_lst):
        pass

    def get_bold_state(self):
        return self.bold_val

    def get_italic_state(self):
        return self.italic_val

    def set_bold_state(self, bold_val):
        self.bold_val = bold_val

    def set_italic_state(self, italic_val):
        self.italic_val = italic_val

class ArialRichText(Richtext):

    def get_bold_state(self):
        return self.bold_val

    def get_italic_state(self):
        return self.italic_val

    def set_bold_state(self, bold_val):
        self.bold_val = bold_val

    def set_italic_state(self, italic_val):
        self.italic_val = italic_val

    def render_text(self, textarea, bold_val, italic_val):
        textarea.configure(font=("Arial", 18, bold_val + " " + italic_val))

    # since bold is common to all the fonts, it is important to get the status of all the fonts and
    # do a logical ro to get the actual bold status
    # Demonstration of wide hierarchy
    def swap_bold_state(self, textarea, text_obj_lst):
        bold_state = ""
        italic_state = ""

        # since bold is common to all the fonts, it is important to get the status of all the fonts and
        # do a logical ro to get the actual bold status

        for i in range(len(text_obj_lst)):
            bold_state = bold_state or text_obj_lst[i].get_bold_state()

        # Base class which abstracts which changes the italic font to back and normal.
        if bold_state == "":
            for i in range(len(text_obj_lst)):
                text_obj_lst[i].set_bold_state("bold")
        else:
            for i in range(len(text_obj_lst)):
                text_obj_lst[i].set_bold_state("")

        for i in range(len(text_obj_lst)):
            italic_state = italic_state or text_obj_lst[i].get_italic_state()

        textarea.configure(
            font=("Arial", 18, text_obj_lst[0].get_bold_state() + " " + text_obj_lst[0].get_italic_state()))

    def swap_italic_state(self, textarea, text_obj_lst):
        bold_state = ""
        italic_state = ""

        for i in range(len(text_obj_lst)):
            italic_state = italic_state or text_obj_lst[i].get_italic_state()

        # After the logical operation do the actual swapping now
        if italic_state == "":
            for i in range(len(text_obj_lst)):
                text_obj_lst[i].set_italic_state("italic")
        else:
            for i in range(len(text_obj_lst)):
                text_obj_lst[i].set_italic_state("")

        for i in range(len(text_obj_lst)):
            bold_state = bold_state or text_obj_lst[i].get_bold_state()

        textarea.configure(
            font=("Arial", 18, text_obj_lst[0].get_bold_state() + " " + text_obj_lst[0].get_italic_state()))


class CourierNewRichText(Richtext):

    def render_text(self, textarea, bold_val, italic_val):
        textarea.configure(font=("Courier", 18, bold_val + " " + italic_val))

    def get_bold_state(self):
        return self.bold_val

    def get_italic_state(self):
        return self.italic_val

    def set_bold_state(self, bold_val):
        self.bold_val = bold_val

    def set_italic_state(self, italic_val):
        self.italic_val = italic_val

    def swap_bold_state(self, textarea, text_obj_lst):
        bold_state = ""
        italic_state = ""

        for i in range(len(text_obj_lst)):
            bold_state = bold_state or text_obj_lst[i].get_bold_state()

        if bold_state == "":
            for i in range(len(text_obj_lst)):
                text_obj_lst[i].set_bold_state("bold")
        else:
            for i in range(len(text_obj_lst)):
                text_obj_lst[i].set_bold_state("")

        for i in range(len(text_obj_lst)):
            italic_state = italic_state or text_obj_lst[i].get_italic_state()

        textarea.configure(
            font=("Courier", 18, text_obj_lst[1].get_bold_state() + " " + text_obj_lst[1].get_italic_state()))

    # class which abstracts which changes the italic font to back and normal.
    def swap_italic_state(self, textarea, text_obj_lst):
        bold_state = ""
        italic_state = ""

        for i in range(len(text_obj_lst)):
            italic_state = italic_state or text_obj_lst[i].get_italic_state()

        if italic_state == "":
            for i in range(len(text_obj_lst)):
                text_obj_lst[i].set_italic_state("italic")
        else:
            for i in range(len(text_obj_lst)):
                text_obj_lst[i].set_italic_state("")

        for i in range(len(text_obj_lst)):
            bold_state = bold_state or text_obj_lst[i].get_bold_state()

        textarea.configure(
            font=("Courier", 18, text_obj_lst[1].get_bold_state() + " " + text_obj_lst[1].get_italic_state()))


class TimesNewRomanRichText(Richtext):
    bold_state = ""
    italic_state = ""

    def render_text(self, textarea, bold_val, italic_val):
        textarea.configure(font=("Roman", 18, bold_val + " " + italic_val))

    def get_bold_state(self):
        return self.bold_val

    def get_italic_state(self):
        return self.italic_val

    def set_bold_state(self, bold_val):
        self.bold_val = bold_val

    def set_italic_state(self, italic_val):
        self.italic_val = italic_val

    def swap_bold_state(self, textarea, text_obj_lst):
        bold_state = ""
        italic_state = ""

        for i in range(len(text_obj_lst)):
            bold_state = bold_state or text_obj_lst[i].get_bold_state()

        if bold_state == "":
            for i in range(len(text_obj_lst)):
                text_obj_lst[i].set_bold_state("bold")
        else:
            for i in range(len(text_obj_lst)):
                text_obj_lst[i].set_bold_state("")

        for i in range(len(text_obj_lst)):
            italic_state = italic_state or text_obj_lst[i].get_italic_state()

        textarea.configure(
            font=("Roman", 18, text_obj_lst[2].get_bold_state() + " " + text_obj_lst[2].get_italic_state()))

    def swap_italic_state(self, textarea, text_obj_lst):
        bold_state = ""
        italic_state = ""

        for i in range(len(text_obj_lst)):
            italic_state = italic_state or text_obj_lst[i].get_italic_state()

        if italic_state == "":
            for i in range(len(text_obj_lst)):
                text_obj_lst[i].set_italic_state("italic")
        else:
            for i in range(len(text_obj_lst)):
                text_obj_lst[i].set_italic_state("")

        for i in range(len(text_obj_lst)):
            bold_state = bold_state or text_obj_lst[i].get_bold_state()

        textarea.configure(
            font=("Roman", 18, text_obj_lst[2].get_bold_state() + " " + text_obj_lst[2].get_italic_state()))

# Classes to manage the menu bar actions and event triggers
class MenuBar:
    def __init__(self, parent):

        menu_font_size = ("", 10)
        self.rich_text = Richtext()

        menubar = tk.Menu(parent.master, font=menu_font_size)
        parent.master.config(menu=menubar)

        file_dropdownMenu = tk.Menu(menubar, font=menu_font_size, tearoff=0)
        file_dropdownMenu.add_command(label="New File", command=parent.new_file)
        file_dropdownMenu.add_command(label="Open File", command=parent.open_file)
        file_dropdownMenu.add_command(label="Save", command=parent.save_file)
        file_dropdownMenu.add_command(label="Save As", command=parent.save_as_file)
        file_dropdownMenu.add_separator()
        file_dropdownMenu.add_command(label="Exit", command=parent.master.destroy)

        # This code ties radio button menus for changing the fonts to appropriate event functions
        font_type_dropdownMenu = tk.Menu(menubar, tearoff=0)
        rvar = tk.StringVar("")
        font_type_dropdownMenu.add_radiobutton(label="Courier New",  variable=rvar, command=parent.courier_new)
        font_type_dropdownMenu.add_radiobutton(label="Times New Roman", var=rvar, value=0,
                                               command=parent.times_new_roman)
        font_type_dropdownMenu.add_radiobutton(label="Arial", var=rvar, command=parent.arial)

        # This code ties check button menus for changing the bold and italics to appropriate event functions
        font_face_dropdownMenu = tk.Menu(menubar, font=menu_font_size, tearoff=0)
        font_face_dropdownMenu.add_checkbutton(label="Bold", onvalue=1, offvalue=0,
                                                command=parent.bold)
        font_face_dropdownMenu.add_checkbutton(label="Italic", onvalue=1, offvalue=0,
                                                 command=parent.italic)

        menubar.add_cascade(label="File", menu=file_dropdownMenu)
        menubar.add_cascade(label="Font", menu=font_type_dropdownMenu)
        menubar.add_cascade(label="Face", menu=font_face_dropdownMenu)

# Classes to manage the file operations triggers
class FileOperation:
    def __init__(self, master1):
        master1.title("Untitled")
        master1.geometry("1200x700")
        self.text_obj_lst = []

        self.text_obj_lst.append(ArialRichText())
        self.text_obj_lst.append(CourierNewRichText())
        self.text_obj_lst.append(TimesNewRomanRichText())
        self.rich_text = Richtext()
        self.bold_status = False

        self.master = master1
        self.textarea = tk.Text(master1)

        self.scroll = tk.Scrollbar(master1, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side = tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.menubar = MenuBar(self)

    def set_window_title(self, name=None):
        if name:
            self.master.title(name)
        else:
            self.master.title("Untitled")

    def new_file(self):
        self.textarea.delete(1.0, tk.END)
        self.filename = None
        self.set_window_title()

    def open_file(self):
        self.filename = filedialog.askopenfilename(defaultextension=".txt",
                                                   filetypes=[("Text Files","*.txt"), ("All Files","*.*")])
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())
            self.set_window_title(self.filename)

    def save_file(self):
        if self.filename:
            try:
                text_area_content = self.textarea.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(text_area_content)
            except Exception as e:
                print(e)
        else:
            self.save_as_file()

    def save_as_file(self):
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile="Untitles.txt",
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            text_area_content = self.textarea.get(1.0, tk.END)
            with open(new_file, "w") as f:
                f.write(text_area_content)
            self.filename = new_file
            self.set_window_title(self.filename)
        except Exception as e:
            print(e)

    def arial(self):
        self.rich_text = self.text_obj_lst[0]
        bold_state = ""
        italic_state = ""

        for i in range(len(self.text_obj_lst)):
            bold_state = bold_state or self.text_obj_lst[i].get_bold_state()

        for i in range(len(self.text_obj_lst)):
            italic_state = italic_state or self.text_obj_lst[i].get_italic_state()

        self.rich_text.render_text(self.textarea, bold_state, italic_state)

    def courier_new(self):
        self.rich_text = self.text_obj_lst[1]

        bold_state = ""
        italic_state = ""

        for i in range(len(self.text_obj_lst)):
            bold_state = bold_state or self.text_obj_lst[i].get_bold_state()

        for i in range(len(self.text_obj_lst)):
            italic_state = italic_state or self.text_obj_lst[i].get_italic_state()

        self.rich_text.render_text(self.textarea, bold_state, italic_state)

    def times_new_roman(self):
        self.rich_text = self.text_obj_lst[2]

        bold_state = ""
        italic_state = ""

        for i in range(len(self.text_obj_lst)):
            bold_state = bold_state or self.text_obj_lst[i].get_bold_state()

        for i in range(len(self.text_obj_lst)):
            italic_state = italic_state or self.text_obj_lst[i].get_italic_state()

        self.rich_text.render_text(self.textarea, bold_state, italic_state)

    def bold(self):
        self.rich_text.swap_bold_state(self.textarea, self.text_obj_lst)

    def italic(self):
        self.rich_text.swap_italic_state(self.textarea, self.text_obj_lst)

if __name__ == "__main__":
    master = tk.Tk()
    pt = FileOperation(master)
    master.mainloop()
