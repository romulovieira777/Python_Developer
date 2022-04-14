from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, Entry, W, E, N, S, END
from tkinter import ttk
from tkinter import messagebox


# Creates application window
root = Tk()

# adds a title to app to application window
root.title("My Books Database Application")

# Add background color to application window
root.configure(background="light green")

# Sets a size for application window
root.geometry("850x500")

# Prevents the application window from resizing
root.resizable(width=False, height=False)

# Create Labels and entry widgets

title_label = ttk.Label(root, text="Title", background="light green", font=("TkDefaultFont", 16))
title_label.grid(row=0, column=0, sticky=W)
title_text = StringVar()
title_entry = ttk.Entry(root, width=24, textvariable=title_text)
title_entry.grid(row=0, column=1, sticky=W)

author_label = ttk.Label(root, text="Author",background="light green", font=("TkDefaultFont", 16))
author_label.grid(row=0, column=2, sticky=W)
author_text = StringVar()
author_entry = ttk.Entry(root, width=24, textvariable=author_text)
author_entry.grid(row=0, column=3, sticky=W)

isbn_label = ttk.Label(root, text="ISBN", background="light green", font=("TkDefaultFont", 14))
isbn_label.grid(row=0, column=4, sticky=W)
isbn_text = StringVar()
isbn_entry = ttk.Entry(root, width=24, textvariable=isbn_text)
isbn_entry.grid(row=0, column=5, sticky=W)

# Add a button to insert inputs into database
add_btn = Button(root, text="Add Book", bg="blue", fg="white", font="helvetica 10 bold", command="")
add_btn.grid(row=0, column=6, sticky=W)

# Add listbox to display data from database
list_bx = Listbox(root, height=16, width=40, font="helvetica 13", bg="light blue")
list_bx.grid(row=3, column=1, columnspan=14, sticky=W + E, pady=40, padx=15)

# Add scrollbar to enable scrolling
scroll_bar = Scrollbar(root)
scroll_bar.grid(row=1, column=8, rowspan=14, sticky=W)

# Enables vertical scrolling
list_bx.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_bx.yview_scroll)

# Runs the application until exit
root.mainloop()
