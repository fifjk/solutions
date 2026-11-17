import tkinter as tk
from tkinter import ttk
import favs_data as dcd
import favs_sql as dcsql


main_window = tk.Tk()
main_window.title('Favorite characters')
main_window.geometry("1500x450")


# global constants
padx = 8
pady = 4
buttonwidth = 10
rowheight = 24
treeview_background = '#E9C5ED'
treeview_foreground = 'black'
treeview_selected = '#E0ABE6'
oddrow = '#D28BD8'
evenrow = '#CA7AD2'
INTERNAL_ERROR_CODE = 0


# region general functions
def read_table(tree, class_):
    count = 0
    result = dcsql.select_all(class_)
    for record in result:
        if record.valid():
            if count % 2 == 0:
                tree.insert(parent='', index='end', iid=str(count), text='', value=record.convert_to_tuple(), tags=('evenrow',))
            else:
                tree.insert(parent='', index='end', iid=str(count), text='', value=record.convert_to_tuple(), tags=('oddrow',))
            count += 1

def sort_treeview(tree, column, reverse):
    data = [(tree.set(item, column), item) for item in tree.get_children('')]

    def sort_key(x):
        try:
            return float(x[0])
        except ValueError:
            return x[0].lower()

    data.sort(reverse=reverse, key=sort_key)

    for index, (value, item) in enumerate(data):
        tree.move(item, '', index)

    tree.heading(column, command=lambda: sort_treeview(tree, column, not reverse))

def empty_treeview(tree):
    tree.delete(*tree.get_children())

def refresh_treeview(tree, class_):
    empty_treeview(tree)
    read_table(tree, class_)

# endregion general functions

# region masculine functions
def read_masculine_entries():
    return entry_masculine_id.get(), entry_masculine_name.get(), entry_masculine_aka.get(), entry_masculine_media.get(), entry_masculine_human.get()

def clear_masculine_entries():
    entry_masculine_id.delete(0, tk.END)
    entry_masculine_name.delete(0, tk.END)
    entry_masculine_aka.delete(0, tk.END)
    entry_masculine_media.delete(0, tk.END)
    entry_masculine_human.delete(0, tk.END)

def write_masculine_entries(values):
    entry_masculine_id.insert(0, values[0])
    entry_masculine_name.insert(0, values[1])
    entry_masculine_aka.insert(0, values[2])
    entry_masculine_media.insert(0, values[3])
    entry_masculine_human.insert(0, values[4])

def edit_masculine(event, tree):
    if tree.identify_region(event.x, event.y) != "cell":
        return

    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    clear_masculine_entries()
    write_masculine_entries(values)

def create_masculine(tree, record):
    masculine = dcd.Masculine.convert_from_tuple(record)
    dcsql.create_record(masculine)
    clear_masculine_entries()
    refresh_treeview(tree, dcd.Masculine)

def update_masculine(tree, record):
    masculine = dcd.Masculine.convert_from_tuple(record)
    dcsql.update_masculine(masculine)
    clear_masculine_entries()
    refresh_treeview(tree, dcd.Masculine)

def delete_masculine(tree, record):
    masculine = dcd.Masculine.convert_from_tuple(record)
    dcsql.delete_hard_masculine(masculine)
    clear_masculine_entries()
    refresh_treeview(tree, dcd.Masculine)
# endregion masculine functions

# region feminine functions
def read_feminine_entries():
    return entry_feminine_id.get(), entry_feminine_name.get(), entry_feminine_aka.get(), entry_feminine_media.get(), entry_feminine_human.get()

def clear_feminine_entries():
    entry_feminine_id.delete(0, tk.END)
    entry_feminine_name.delete(0, tk.END)
    entry_feminine_aka.delete(0, tk.END)
    entry_feminine_media.delete(0, tk.END)
    entry_feminine_human.delete(0, tk.END)

def write_feminine_entries(values):
    entry_feminine_id.insert(0, values[0])
    entry_feminine_name.insert(0, values[1])
    entry_feminine_aka.insert(0, values[2])
    entry_feminine_media.insert(0, values[3])
    entry_feminine_human.insert(0, values[4])

def edit_feminine(event, tree):
    if tree.identify_region(event.x, event.y) != "cell":
        return

    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    clear_feminine_entries()
    write_feminine_entries(values)

def create_feminine(tree, record):
    feminine = dcd.Feminine.convert_from_tuple(record)
    dcsql.create_record(feminine)
    clear_feminine_entries()
    refresh_treeview(tree, dcd.Feminine)

def update_feminine(tree, record):
    feminine = dcd.Feminine.convert_from_tuple(record)
    dcsql.update_feminine(feminine)
    clear_feminine_entries()
    refresh_treeview(tree, dcd.Feminine)

def delete_feminine(tree, record):
    feminine = dcd.Feminine.convert_from_tuple(record)
    dcsql.delete_hard_feminine(feminine)
    clear_feminine_entries()
    refresh_treeview(tree, dcd.Feminine)
# endregion feminine functions

# region other functions
def read_other_entries():
    return entry_other_id.get(), entry_other_name.get(), entry_other_aka.get(), entry_other_media.get(), entry_other_human.get()

def clear_other_entries():
    entry_other_id.delete(0, tk.END)
    entry_other_name.delete(0, tk.END)
    entry_other_aka.delete(0, tk.END)
    entry_other_media.delete(0, tk.END)
    entry_other_human.delete(0, tk.END)

def write_other_entries(values):
    entry_other_id.insert(0, values[0])
    entry_other_name.insert(0, values[1])
    entry_other_aka.insert(0, values[2])
    entry_other_media.insert(0, values[3])
    entry_other_human.insert(0, values[4])

def edit_other(event, tree):
    if tree.identify_region(event.x, event.y) != "cell":
        return

    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    clear_other_entries()
    write_other_entries(values)

def create_other(tree, record):
    other = dcd.Other.convert_from_tuple(record)
    dcsql.create_record(other)
    clear_other_entries()
    refresh_treeview(tree, dcd.Other)

def update_other(tree, record):
    other = dcd.Other.convert_from_tuple(record)
    dcsql.update_other(other)
    clear_other_entries()
    refresh_treeview(tree, dcd.Other)

def delete_other(tree, record):
    other = dcd.Other.convert_from_tuple(record)
    dcsql.delete_hard_other(other)
    clear_other_entries()
    refresh_treeview(tree, dcd.Other)
# endregion other functions


# style
style = ttk.Style()
style.theme_use('default')
style.configure(
    "Treeview",
    background=treeview_background,
    foreground=treeview_foreground,
    rowheight=rowheight,
    fieldbackground=treeview_background
)
style.configure(
    "Treeview.Heading",
    background=treeview_background,
    foreground=treeview_foreground
)
style.map(
    'Treeview',
    background=[('selected',
                 treeview_selected)]
)

# region frames

# masculine frame
frame_masculine = tk.LabelFrame(main_window, text="Masculine")
frame_masculine.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

tree_frame_masculine = tk.Frame(frame_masculine)
tree_frame_masculine.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_masculine = tk.Scrollbar(tree_frame_masculine)
tree_scroll_masculine.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_masculine = ttk.Treeview(tree_frame_masculine, selectmode="browse")
tree_masculine.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_masculine.config(command=tree_masculine.yview)

# feminine frame
frame_feminine = tk.LabelFrame(main_window, text="Feminine")
frame_feminine.grid(row=0, column=1, padx=padx, pady=pady, sticky=tk.N)

tree_frame_feminine = tk.Frame(frame_feminine)
tree_frame_feminine.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_feminine = tk.Scrollbar(tree_frame_feminine)
tree_scroll_feminine.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_feminine = ttk.Treeview(tree_frame_feminine, selectmode="browse")
tree_feminine.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_feminine.config(command=tree_feminine.yview)

# other frame
frame_other = tk.LabelFrame(main_window, text="Other")
frame_other.grid(row=0, column=2, padx=padx, pady=pady, sticky=tk.N)

tree_frame_other = tk.Frame(frame_other)
tree_frame_other.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_other = tk.Scrollbar(tree_frame_other)
tree_scroll_other.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_other = ttk.Treeview(tree_frame_other, selectmode="browse")
tree_other.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_other.config(command=tree_other.yview)
# endregion frames

# region entries and label frames

# masculine entry and label frames
controls_frame_masculine = tk.Frame(frame_masculine)
controls_frame_masculine.grid(row=3, column=0, padx=padx, pady=pady)
edit_frame_masculine = tk.Frame(controls_frame_masculine)
edit_frame_masculine.grid(row=0, column=0, padx=padx, pady=pady)

# id entry
label_masculine_id = tk.Label(edit_frame_masculine, text="ID")
label_masculine_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_masculine_id = tk.Entry(edit_frame_masculine, width=5, justify="left")
entry_masculine_id.grid(row=1, column=0, padx=padx, pady=pady)

# name entry
label_masculine_name = tk.Label(edit_frame_masculine, text="Name")
label_masculine_name.grid(row=0, column=1, padx=padx, pady=pady)
entry_masculine_name = tk.Entry(edit_frame_masculine, width=15, justify="left")
entry_masculine_name.grid(row=1, column=1, padx=padx, pady=pady)

# aka entry
label_masculine_aka = tk.Label(edit_frame_masculine, text="A.K.A.")
label_masculine_aka.grid(row=0, column=2, padx=padx, pady=pady)
entry_masculine_aka = tk.Entry(edit_frame_masculine, width=10, justify="left")
entry_masculine_aka.grid(row=1, column=2, padx=padx, pady=pady)

# media entry
label_masculine_media = tk.Label(edit_frame_masculine, text="Media")
label_masculine_media.grid(row=0, column=3, padx=padx, pady=pady)
entry_masculine_media = tk.Entry(edit_frame_masculine, width=20, justify="left")
entry_masculine_media.grid(row=1, column=3, padx=padx, pady=pady)

# human entry
label_masculine_human = tk.Label(edit_frame_masculine, text="Human")
label_masculine_human.grid(row=0, column=4, padx=padx, pady=pady)
entry_masculine_human = tk.Entry(edit_frame_masculine, width=6, justify="left")
entry_masculine_human.grid(row=1, column=4, padx=padx, pady=pady)


# feminine and label frames
controls_frame_feminine = tk.Frame(frame_feminine)
controls_frame_feminine.grid(row=3, column=0, padx=padx, pady=pady)
edit_frame_feminine = tk.Frame(controls_frame_feminine)
edit_frame_feminine.grid(row=0, column=0, padx=padx, pady=pady)

# id entry
label_feminine_id = tk.Label(edit_frame_feminine, text="ID")
label_feminine_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_feminine_id = tk.Entry(edit_frame_feminine, width=5, justify="left")
entry_feminine_id.grid(row=1, column=0, padx=padx, pady=pady)

# name entry
label_feminine_name = tk.Label(edit_frame_feminine, text="Name")
label_feminine_name.grid(row=0, column=1, padx=padx, pady=pady)
entry_feminine_name = tk.Entry(edit_frame_feminine, width=15, justify="left")
entry_feminine_name.grid(row=1, column=1, padx=padx, pady=pady)

# aka entry
label_feminine_aka = tk.Label(edit_frame_feminine, text="A.K.A.")
label_feminine_aka.grid(row=0, column=2, padx=padx, pady=pady)
entry_feminine_aka = tk.Entry(edit_frame_feminine, width=10, justify="left")
entry_feminine_aka.grid(row=1, column=2, padx=padx, pady=pady)

# media entry
label_feminine_media = tk.Label(edit_frame_feminine, text="Media")
label_feminine_media.grid(row=0, column=3, padx=padx, pady=pady)
entry_feminine_media = tk.Entry(edit_frame_feminine, width=20, justify="left")
entry_feminine_media.grid(row=1, column=3, padx=padx, pady=pady)

# human entry
label_feminine_human = tk.Label(edit_frame_feminine, text="Human")
label_feminine_human.grid(row=0, column=4, padx=padx, pady=pady)
entry_feminine_human = tk.Entry(edit_frame_feminine, width=6, justify="left")
entry_feminine_human.grid(row=1, column=4, padx=padx, pady=pady)


# masculine and label frames
controls_frame_other = tk.Frame(frame_other)
controls_frame_other.grid(row=3, column=0, padx=padx, pady=pady)
edit_frame_other = tk.Frame(controls_frame_other)
edit_frame_other.grid(row=0, column=0, padx=padx, pady=pady)

# id entry
label_other_id = tk.Label(edit_frame_other, text="ID")
label_other_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_other_id = tk.Entry(edit_frame_other, width=5, justify="left")
entry_other_id.grid(row=1, column=0, padx=padx, pady=pady)

# name entry
label_other_name = tk.Label(edit_frame_other, text="Name")
label_other_name.grid(row=0, column=1, padx=padx, pady=pady)
entry_other_name = tk.Entry(edit_frame_other, width=15, justify="left")
entry_other_name.grid(row=1, column=1, padx=padx, pady=pady)

# aka entry
label_other_aka = tk.Label(edit_frame_other, text="A.K.A.")
label_other_aka.grid(row=0, column=2, padx=padx, pady=pady)
entry_other_aka = tk.Entry(edit_frame_other, width=10, justify="left")
entry_other_aka.grid(row=1, column=2, padx=padx, pady=pady)

# media entry
label_other_media = tk.Label(edit_frame_other, text="Media")
label_other_media.grid(row=0, column=3, padx=padx, pady=pady)
entry_other_media = tk.Entry(edit_frame_other, width=20, justify="left")
entry_other_media.grid(row=1, column=3, padx=padx, pady=pady)

# human entry
label_other_human = tk.Label(edit_frame_other, text="Human")
label_other_human.grid(row=0, column=4, padx=padx, pady=pady)
entry_other_human = tk.Entry(edit_frame_other, width=6, justify="left")
entry_other_human.grid(row=1, column=4, padx=padx, pady=pady)
# endregion entries and label frames

# region buttons

# feminine buttons frames
button_frame_masculine = tk.Frame(controls_frame_masculine)
button_frame_masculine.grid(row=1, column=0, padx=padx, pady=pady)

# masculine buttons

# - create
button_create_masculine = tk.Button(button_frame_masculine,
                                  text="Create",
                                  command=lambda: create_masculine(tree_masculine, read_masculine_entries()),
                                  width=buttonwidth)
button_create_masculine.grid(row=0, column=1, padx=padx, pady=pady)

# - update
button_update_masculine = tk.Button(button_frame_masculine,
                                  text="Update",
                                  command=lambda: update_masculine(tree_masculine, read_masculine_entries()),
                                  width=buttonwidth)
button_update_masculine.grid(row=0, column=2, padx=padx, pady=pady)

# - delete
button_delete_masculine = tk.Button(button_frame_masculine,
                                  text="Delete",
                                  command=lambda: delete_masculine(tree_masculine, read_masculine_entries()),
                                  width=buttonwidth)
button_delete_masculine.grid(row=0, column=3, padx=padx, pady=pady)

# - clear
button_clear_masculine = tk.Button(button_frame_masculine,
                                 text="Clear",
                                 command=lambda: clear_masculine_entries(),
                                 width=buttonwidth)
button_clear_masculine.grid(row=0, column=4, padx=padx, pady=pady)


# feminine frames
button_frame_feminine = tk.Frame(controls_frame_feminine)
button_frame_feminine.grid(row=1, column=0, padx=padx, pady=pady)

# feminine buttons

# - create
button_create_feminine = tk.Button(button_frame_feminine,
                                text="Create",
                                command=lambda: create_feminine(tree_feminine, read_feminine_entries()),
                                width=buttonwidth)
button_create_feminine.grid(row=0, column=1, padx=padx, pady=pady)

# - update
button_update_feminine = tk.Button(button_frame_feminine,
                                text="Update",
                                command=lambda: update_feminine(tree_feminine, read_feminine_entries()),
                                width=buttonwidth)
button_update_feminine.grid(row=0, column=2, padx=padx, pady=pady)

# - delete
button_delete_feminine = tk.Button(button_frame_feminine,
                                text="Delete",
                                command=lambda: delete_feminine(tree_feminine, read_feminine_entries()),
                                width=buttonwidth)
button_delete_feminine.grid(row=0, column=3, padx=padx, pady=pady)

# - clear
button_clear_feminine = tk.Button(button_frame_feminine,
                               text="Clear",
                               command=lambda: clear_feminine_entries(),
                               width=buttonwidth)
button_clear_feminine.grid(row=0, column=4, padx=padx, pady=pady)


# other buttons frames
button_frame_other = tk.Frame(controls_frame_other)
button_frame_other.grid(row=1, column=0, padx=padx ,pady=pady)

# other buttons

# - create
button_create_other = tk.Button(button_frame_other,
                                   text="Create",
                                   command=lambda: create_other(tree_other, read_other_entries()),
                                   width=buttonwidth)
button_create_other.grid(row=0, column=1, padx=padx, pady=pady)

# - update
button_update_other = tk.Button(button_frame_other,
                                   text="Update",
                                   command=lambda: update_other(tree_other, read_other_entries()),
                                   width=buttonwidth)
button_update_other.grid(row=0, column=2, padx=padx, pady=pady)

# - delete
button_delete_other = tk.Button(button_frame_other,
                                   text="Delete",
                                   command=lambda: delete_other(tree_other, read_other_entries()),
                                   width=buttonwidth)
button_delete_other.grid(row=0, column=3, padx=padx, pady=pady)

# - clear
button_clear_other = tk.Button(button_frame_other,
                                  text="Clear",
                                  command=lambda: clear_other_entries(),
                                  width=buttonwidth)
button_clear_other.grid(row=0, column=4, padx=padx, pady=pady)
# endregion buttons

# region table formats

# masculine table format
tree_masculine['column'] = ("id", "name", "aka", "media", "human")
tree_masculine.column("#0", width=0, stretch=tk.NO)
tree_masculine.column("id", anchor=tk.CENTER, width=40)
tree_masculine.column("name", anchor=tk.W, width=100)
tree_masculine.column("aka", anchor=tk.CENTER, width=100)
tree_masculine.column("media", anchor=tk.W, width=110)
tree_masculine.column("human", anchor=tk.CENTER, width=80)
tree_masculine.heading("#0", text="", anchor=tk.W)
tree_masculine.heading("id", text="ID", anchor=tk.CENTER, command=lambda: sort_treeview(tree_masculine, "id", False))
tree_masculine.heading("name", text="Name", anchor=tk.CENTER, command=lambda: sort_treeview(tree_masculine, "name", False))
tree_masculine.heading("aka", text="A.K.A.", anchor=tk.CENTER)
tree_masculine.heading("media", text="Media", anchor=tk.CENTER)
tree_masculine.heading("human", text="Human", anchor=tk.CENTER)
tree_masculine.tag_configure('oddrow', background=oddrow)
tree_masculine.tag_configure('evenrow', background=evenrow)

tree_masculine.bind("<ButtonRelease-1>", lambda event: edit_masculine(event, tree_masculine))

# feminine table format
tree_feminine['column'] = ("id", "name", "aka", "media", "human")
tree_feminine.column("#0", width=0, stretch=tk.NO)
tree_feminine.column("id", anchor=tk.CENTER, width=40)
tree_feminine.column("name", anchor=tk.W, width=100)
tree_feminine.column("aka", anchor=tk.CENTER, width=100)
tree_feminine.column("media", anchor=tk.CENTER, width=110)
tree_feminine.column("human", anchor=tk.CENTER, width=80)
tree_feminine.heading("#0", text="", anchor=tk.W)
tree_feminine.heading("id", text="ID", anchor=tk.CENTER, command=lambda: sort_treeview(tree_feminine, "id", False))
tree_feminine.heading("name", text="Name", anchor=tk.CENTER, command=lambda: sort_treeview(tree_feminine, "name", False))
tree_feminine.heading("aka", text="A.K.A.", anchor=tk.CENTER)
tree_feminine.heading("media", text="Media", anchor=tk.CENTER)
tree_feminine.heading("human", text="Human", anchor=tk.CENTER)
tree_feminine.tag_configure('oddrow', background=oddrow)
tree_feminine.tag_configure('evenrow', background=evenrow)

tree_feminine.bind("<ButtonRelease-1>", lambda event: edit_feminine(event, tree_feminine))

# other table format
tree_other['column'] = ("id", "name", "aka", "media", "human")
tree_other.column("#0", width=0, stretch=tk.NO)
tree_other.column("id", anchor=tk.CENTER, width=40)
tree_other.column("name", anchor=tk.CENTER, width=100)
tree_other.column("aka", anchor=tk.CENTER, width=100)
tree_other.column("media", anchor=tk.CENTER, width=110)
tree_other.column("human", anchor=tk.CENTER, width=80)
tree_other.heading("#0", text="", anchor=tk.W)
tree_other.heading("id", text="ID", anchor=tk.CENTER, command=lambda: sort_treeview(tree_other, "id", False))
tree_other.heading("name", text="Name", anchor=tk.CENTER, command=lambda: sort_treeview(tree_other, "name", False))
tree_other.heading("aka", text="A.K.A.", anchor=tk.CENTER)
tree_other.heading("media", text="Media", anchor=tk.CENTER)
tree_other.heading("human", text="Human", anchor=tk.CENTER)
tree_other.tag_configure('oddrow', background=oddrow)
tree_other.tag_configure('evenrow', background=evenrow)

tree_other.bind("<ButtonRelease-1>", lambda event: edit_other(event, tree_other))
# endregion table formats


if __name__ == "__main__":
    refresh_treeview(tree_masculine, dcd.Masculine)
    refresh_treeview(tree_feminine, dcd.Feminine)
    refresh_treeview(tree_other, dcd.Other)
    main_window.mainloop()

