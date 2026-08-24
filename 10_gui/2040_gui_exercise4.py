""" Opgave "GUI step 4":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2040.png

Genbrug din kode fra "GUI step 3".

Fyld treeview'en med testdata.
Leg med farveværdierne. Find en farvekombination, som du kan lide.

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).
    Hvis du klikker på en datarække i træoversigten, kopieres dataene i denne række til indtastningsfelterne.

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

import tkinter as tk
from tkinter import ttk


def empty_entries():
    id_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    destination_entry.delete(0, tk.END)
    weather_entry.delete(0, tk.END)

def read_table(tree_read):  # fill tree with test data
    count = 0
    for record in test_data_list:
        if count % 2 == 0:  # even
            tree_read.insert(parent='', index='end', text='', values=record, tags=('evenrow',))
        else:  # odd
            tree_read.insert(parent='', index='end', text='', values=record, tags=('oddrow',))
        count += 1


def edit_record(event, tree):  # Copy data from selected row into entry box. Parameter event is mandatory but we don't use it. (1)
    index_selected = tree.focus()  # Index of selected tuple
    values = tree.item(index_selected, 'values')  # Values of selected tuple
    empty_entries()  # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
    id_entry.insert(0, values[0])  # write data into entry box
    weight_entry.insert(0, values[1])
    destination_entry.insert(0, values[2])


padx = 14
pady = 4
rowheight = 24
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#773333"
oddrow = "#ddeedd"
evenrow = "#cce0cc"

test_data_list = []
test_data_list.append(("1", 4000, "Alaska"))
test_data_list.append(("3", 2000, "Chicago"))
test_data_list.append(("4", 1700, "Candy World"))
test_data_list.append(("6", 2400, "Balboa Island"))
test_data_list.append(("7", 6500, "Jeff's house"))
test_data_list.append(("9", 4800, "McDonald's"))
test_data_list.append(("8", 1200, "McDonald's 2"))
test_data_list.append(("19", 5600, "Naxxar"))
test_data_list.append(("21", 2000, "Seoul"))
test_data_list.append(("2", 1800, "Praca Da Liverdade"))
test_data_list.append(("69", 8100, "Skærage 7"))


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

tree.tag_configure('oddrow', background=oddrow)
tree.tag_configure('evenrow', background=evenrow)

tree.bind("<ButtonRelease-1>", lambda event: edit_record(event, tree))

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

read_table(tree)

if __name__ == "__main__":
    main_window.mainloop()
