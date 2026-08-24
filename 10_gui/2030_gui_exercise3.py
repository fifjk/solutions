"""Opgave "GUI step 3":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2030.png

Genbrug din kode fra "GUI step 2".

GUI-strukturen bør være som følger:
    main window
        labelframe
            frame
                treeview and scrollbar
            frame
                labels and entries
            frame
                buttons

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

import tkinter as tk
from tkinter import ttk


def empty_entries():
    print("Entries cleared")
    id_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    destination_entry.delete(0, tk.END)
    weather_entry.delete(0, tk.END)


padx = 14
pady = 4
rowheight = 24  # rowheight in treeview
treeview_background = "#eeeeee"  # color of background in treeview
treeview_foreground = "black"  # color of foreground in treeview
treeview_selected = "#773333"  # color of selected row in treeview

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")

style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])

label_frame = tk.LabelFrame(main_window, text="Container")
label_frame.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

frame_1 = tk.Frame(label_frame)
frame_1.grid(row=1, column=0, padx=padx, pady=pady, sticky=tk.N)

tree_scrollbar = tk.Scrollbar(frame_1)
tree_scrollbar.grid(row=1, column=1, padx=padx, pady=pady, sticky='ns')
tree = ttk.Treeview(frame_1, yscrollcommand=tree_scrollbar.set, selectmode="browse")
tree.grid(row=1, column=0, padx=0, pady=pady)
tree_scrollbar.config(command=tree.yview)

tree['columns'] = ("col1", "col2", "col3")
tree.column("#0", width=0, stretch=tk.NO)
tree.column("col1", anchor=tk.E, width=90)
tree.column("col2", anchor=tk.W, width=130)
tree.column("col3", anchor=tk.W, width=180)

tree.heading("#0", text="", anchor=tk.W)
tree.heading("col1", text="Id", anchor=tk.CENTER)
tree.heading("col2", text="Weight", anchor=tk.CENTER)
tree.heading("col3", text="Destination", anchor=tk.CENTER)

frame_2 = tk.Frame(label_frame)
frame_2.grid(row=2, column=0, padx=padx, pady=pady, sticky=tk.N)

id_label = tk.Label(frame_2, text="Id")
id_label.grid(row=2, column=0, padx=padx, pady=pady)

weight_label = tk.Label(frame_2, text="Weight")
weight_label.grid(row=2, column=1, padx=padx, pady=pady)

destination_label = tk.Label(frame_2, text="Destination")
destination_label.grid(row=2, column=2, padx=padx, pady=pady)

weather_label = tk.Label(frame_2, text="Weather")
weather_label.grid(row=2, column=3, padx=padx, pady=pady)

id_entry = tk.Entry(frame_2, width=6)
id_entry.grid(row=3, column=0, padx=padx, pady=pady)

weight_entry = tk.Entry(frame_2, width=10)
weight_entry.grid(row=3, column=1, padx=padx, pady=pady)

destination_entry = tk.Entry(frame_2, width=20)
destination_entry.grid(row=3, column=2, padx=padx, pady=pady)

weather_entry = tk.Entry(frame_2, width=16)
weather_entry.grid(row=3, column=3, padx=padx, pady=pady)

frame_3 = tk.Frame(label_frame)
frame_3.grid(row=4, column=0, padx=padx, pady=pady, sticky=tk.N)

create_button = tk.Button(frame_3, text="Create")
create_button.grid(row=5, column=0, padx=padx, pady=pady)

update_button = tk.Button(frame_3, text="Update")
update_button.grid(row=5, column=1, padx=padx, pady=pady)

delete_button = tk.Button(frame_3, text="Delete")
delete_button.grid(row=5, column=2, padx=padx, pady=pady)

clear_button = tk.Button(frame_3, text="Clear Entry Boxes", command=empty_entries)
clear_button.grid(row=5, column=3, padx=padx, pady=pady)


if __name__ == "__main__":
    main_window.mainloop()
