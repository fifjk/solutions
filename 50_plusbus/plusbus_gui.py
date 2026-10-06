import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import plusbus_data as dcd
import plusbus_sql as dcsql
import plusbus_func as dcf

main_window = tk.Tk()
main_window.title('PlusBus')
main_window.geometry("1800x500")


# global constants
padx = 8
pady = 4
rowheight = 24
treeview_background = '#FFDAF5'
treeview_foreground = 'black'
treeview_selected = '#DDABDB'
oddrow = '#DF94DB'
evenrow = '#CE75BE'
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

def empty_treeview(tree):
    tree.delete(*tree.get_children())

def refresh_treeview(tree, class_):
    empty_treeview(tree)
    read_table(tree, class_)
# endregion general functions


# region client functions
def read_client_entries():
    return entry_clients_id.get(), entry_clients_last_name.get(), entry_clients_contact.get()

def clear_client_entries():
    entry_clients_id.delete(0, tk.END)
    entry_clients_last_name.delete(0, tk.END)
    entry_clients_contact.delete(0, tk.END)

def write_client_entries(values):
    entry_clients_id.insert(0, values[0])
    entry_clients_last_name.insert(0, values[1])
    entry_clients_contact.insert(0, values[2])

def edit_clients(_, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    clear_client_entries()
    write_client_entries(values)

def create_clients(tree, record):
    clients = dcd.Clients.convert_from_tuple(record)
    dcsql.create_record(clients)
    clear_client_entries()
    refresh_treeview(tree, dcd.Clients)

def update_clients(tree, record):
    clients = dcd.Clients.convert_from_tuple(record)
    dcsql.update_clients(clients)
    clear_client_entries()
    refresh_treeview(tree, dcd.Clients)

def delete_clients(tree, record):
    clients = dcd.Clients.convert_from_tuple(record)
    dcsql.delete_soft_clients(clients)
    clear_client_entries()
    refresh_treeview(tree, dcd.Clients)
# endregion client functions


# region trip functions
def read_trip_entries():
    return entry_trips_id.get(), entry_trips_route.get(), entry_trips_date.get(), entry_trips_capacity.get()


def clear_trip_entries():
    entry_trips_id.delete(0, tk.END)
    entry_trips_route.delete(0, tk.END)
    entry_trips_date.delete(0, tk.END)
    entry_trips_capacity.delete(0, tk.END)


def write_trip_entries(values):
    entry_trips_id.insert(0, values[0])
    entry_trips_route.insert(0, values[1])
    entry_trips_date.insert(0, values[2])
    entry_trips_capacity.insert(0, values[3])


def edit_trip(_, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    clear_trip_entries()
    write_trip_entries(values)


def create_trip(tree, record):
    trips = dcd.Trips.convert_from_tuple(record)
    dcsql.create_record(trips)
    clear_trip_entries()
    refresh_treeview(tree, dcd.Trips)


def update_trip(tree, record):
    trips = dcd.Trips.convert_from_tuple(record)
    dcsql.update_trips(trips)
    clear_trip_entries()
    refresh_treeview(tree, dcd.Trips)


def delete_trip(tree, record):
    trips = dcd.Trips.convert_from_tuple(record)
    dcsql.delete_soft_trips(trips)
    clear_trip_entries()
    refresh_treeview(tree, dcd.Trips)
# endregion trip functions


# region booking functions
def read_booking_entries():
    return entry_bookings_id.get(), entry_bookings_client_id.get(), entry_bookings_trip_id.get(), entry_bookings_seats.get()


def clear_booking_entries():
    entry_bookings_id.delete(0, tk.END)
    entry_bookings_client_id.delete(0, tk.END)
    entry_bookings_trip_id.delete(0, tk.END)
    entry_bookings_seats.delete(0, tk.END)


def write_booking_entries(values):
    entry_bookings_id.insert(0, values[0])
    entry_bookings_client_id.insert(0, values[1])
    entry_bookings_trip_id.insert(0, values[2])
    entry_bookings_seats.insert(0, values[3])


def edit_bookings(_, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    clear_booking_entries()
    write_booking_entries(values)


def create_bookings(tree, record):
    bookings = dcd.Bookings.convert_from_tuple(record)
    dcsql.create_record(bookings)
    clear_booking_entries()
    refresh_treeview(tree, dcd.Bookings)


def update_bookings(tree, record):
    bookings = dcd.Bookings.convert_from_tuple(record)
    dcsql.update_bookings(bookings)
    clear_booking_entries()
    refresh_treeview(tree, dcd.Bookings)


def delete_bookings(tree, record):
    bookings = dcd.Bookings.convert_from_tuple(record)
    dcsql.delete_soft_bookings(bookings)
    clear_booking_entries()
    refresh_treeview(tree, dcd.Bookings)
# endregion booking functions


# style
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.configure("Treeview.Heading", background=treeview_background, foreground=treeview_foreground)
style.map('Treeview', background=[('selected', treeview_selected)])


# region frames

# client frame
frame_clients = tk.LabelFrame(main_window, text="Clients")
frame_clients.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

tree_frame_clients = tk.Frame(frame_clients)
tree_frame_clients.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_clients = tk.Scrollbar(tree_frame_clients)
tree_scroll_clients.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_clients = ttk.Treeview(tree_frame_clients, selectmode="browse")
tree_clients.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_clients.config(command=tree_clients.yview)

# trip frame
frame_trips = tk.LabelFrame(main_window, text="Trips")
frame_trips.grid(row=0, column=1, padx=padx, pady=pady, sticky=tk.N)

tree_frame_trips = tk.Frame(frame_trips)
tree_frame_trips.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_trips = tk.Scrollbar(tree_frame_trips)
tree_scroll_trips.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_trips = ttk.Treeview(tree_frame_trips, selectmode="browse")
tree_trips.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_trips.config(command=tree_trips.yview)

# booking frame
frame_bookings = tk.LabelFrame(main_window, text="Bookings")
frame_bookings.grid(row=0, column=2, padx=padx, pady=pady, sticky=tk.N)

tree_frame_bookings = tk.Frame(frame_bookings)
tree_frame_bookings.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_bookings = tk.Scrollbar(tree_frame_bookings)
tree_scroll_bookings.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_bookings = ttk.Treeview(tree_frame_bookings, selectmode="browse")
tree_bookings.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_bookings.config(command=tree_bookings.yview)
# endregion frames


# region entries and label frames

# client entry and label frames
controls_frame_clients = tk.Frame(frame_clients)
controls_frame_clients.grid(row=3, column=0, padx=padx, pady=pady)
edit_frame_clients = tk.Frame(controls_frame_clients)
edit_frame_clients.grid(row=0, column=0, padx=padx, pady=pady)

# id entry
label_clients_id = tk.Label(edit_frame_clients, text="ID")
label_clients_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_clients_id = tk.Entry(edit_frame_clients, width=4, justify="right")
entry_clients_id.grid(row=1, column=0, padx=padx, pady=pady)

# last name entry
label_clients_last_name = tk.Label(edit_frame_clients, text="Last name")
label_clients_last_name.grid(row=0, column=1, padx=padx, pady=pady)
entry_clients_last_name = tk.Entry(edit_frame_clients, width=4, justify="right")
entry_clients_last_name.grid(row=1, column=1, padx=padx, pady=pady)

# contact entry
label_clients_contact = tk.Label(edit_frame_clients, text="Contact")
label_clients_contact.grid(row=0, column=2, padx=padx, pady=pady)
entry_clients_contact = tk.Entry(edit_frame_clients, width=4, justify="right")
entry_clients_contact.grid(row=1, column=2, padx=padx, pady=pady)


# trip entry and label frames
controls_frame_trips = tk.Frame(frame_trips)
controls_frame_trips.grid(row=3, column=0, padx=padx, pady=pady)
edit_frame_trips = tk.Frame(controls_frame_trips)
edit_frame_trips.grid(row=0, column=0, padx=padx, pady=pady)

# id entry
label_trips_id = tk.Label(edit_frame_trips, text="ID")
label_trips_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_trips_id = tk.Entry(edit_frame_trips, width=4, justify="right")
entry_trips_id.grid(row=1, column=0, padx=padx, pady=pady)

# route entry
label_trips_route = tk.Label(edit_frame_trips, text="Route")
label_trips_route.grid(row=0, column=1, padx=padx, pady=pady)
entry_trips_route = tk.Entry(edit_frame_trips, width=4, justify="right")
entry_trips_route.grid(row=1, column=1, padx=padx, pady=pady)

# date entry
label_trips_date = tk.Label(edit_frame_trips, text="Date")
label_trips_date.grid(row=0, column=2, padx=padx, pady=pady)
entry_trips_date = tk.Entry(edit_frame_trips, width=4, justify="right")
entry_trips_date.grid(row=1, column=2, padx=padx, pady=pady)

# capacity entry
label_trips_capacity = tk.Label(edit_frame_trips, text="Capacity")
label_trips_capacity.grid(row=0, column=3, padx=padx, pady=pady)
entry_trips_capacity = tk.Entry(edit_frame_trips, width=4, justify="right")
entry_trips_capacity.grid(row=1, column=3, padx=padx, pady=pady)


# booking entry and label frames
controls_frame_bookings = tk.Frame(frame_bookings)
controls_frame_bookings.grid(row=3, column=0, padx=padx, pady=pady)
edit_frame_bookings = tk.Frame(controls_frame_bookings)
edit_frame_bookings.grid(row=0, column=0, padx=padx, pady=pady)

# id entry
label_bookings_id = tk.Label(edit_frame_bookings, text="ID")
label_bookings_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_bookings_id = tk.Entry(edit_frame_bookings, width=4, justify="right")
entry_bookings_id.grid(row=1, column=0, padx=padx, pady=pady)

# client id entry
label_bookings_client_id = tk.Label(edit_frame_bookings, text="Client ID")
label_bookings_client_id.grid(row=0, column=1, padx=padx, pady=pady)
entry_bookings_client_id = tk.Entry(edit_frame_bookings, width=4, justify="right")
entry_bookings_client_id.grid(row=1, column=1, padx=padx, pady=pady)

# trip id entry
label_bookings_trip_id = tk.Label(edit_frame_bookings, text="Trip ID")
label_bookings_trip_id.grid(row=0, column=2, padx=padx, pady=pady)
entry_bookings_trip_id = tk.Entry(edit_frame_bookings, width=4, justify="right")
entry_bookings_trip_id.grid(row=1, column=2, padx=padx, pady=pady)

# seat entry
label_bookings_seats = tk.Label(edit_frame_bookings, text="Seats")
label_bookings_seats.grid(row=0, column=3, padx=padx, pady=pady)
entry_bookings_seats = tk.Entry(edit_frame_bookings, width=4, justify="right")
entry_bookings_seats.grid(row=1, column=3, padx=padx, pady=pady)
# endregion entries and label frames


# region buttons

# client buttons frames
button_frame_clients = tk.Frame(controls_frame_clients)
button_frame_clients.grid(row=1, column=0, padx=padx, pady=pady)

# client buttons

# - create
button_create_clients = tk.Button(button_frame_clients, text="Create", command=lambda: create_clients(tree_clients, read_client_entries()))
button_create_clients.grid(row=0, column=1, padx=padx, pady=pady)

# - update
button_update_clients = tk.Button(button_frame_clients, text="Update", command=lambda: update_clients(tree_clients, read_client_entries()))
button_update_clients.grid(row=0, column=2, padx=padx, pady=pady)

# - delete
button_delete_clients = tk.Button(button_frame_clients, text="Delete", command=lambda: delete_clients(tree_clients, read_client_entries()))
button_delete_clients.grid(row=0, column=3, padx=padx, pady=pady)

# - clear
button_clear_clients = tk.Button(button_frame_clients, text="Clear", command=clear_client_entries())
button_clear_clients.grid(row=0, column=4, padx=padx, pady=pady)


# trip buttons frames
button_frame_trips = tk.Frame(controls_frame_trips)
button_frame_trips.grid(row=1, column=0, padx=padx, pady=pady)

# trip buttons

# - create
button_create_trips = tk.Button(button_frame_trips, text="Create", command=lambda: create_trip(tree_trips, read_trip_entries()))
button_create_trips.grid(row=0, column=1, padx=padx, pady=pady)

# - update
button_update_trips = tk.Button(button_frame_trips, text="Update", command=lambda: update_trip(tree_trips, read_trip_entries()))
button_update_trips.grid(row=0, column=2, padx=padx, pady=pady)

# - delete
button_delete_trips = tk.Button(button_frame_trips, text="Delete", command=lambda: delete_trip(tree_trips, read_trip_entries()))
button_delete_trips.grid(row=0, column=3, padx=padx, pady=pady)

# - clear
button_clear_trips = tk.Button(button_frame_trips, text="Clear", command=clear_trip_entries())
button_clear_trips.grid(row=0, column=4, padx=padx, pady=pady)


# booking buttons frames
button_frame_bookings = tk.Frame(controls_frame_bookings)
button_frame_bookings.grid(row=1, column=0, padx=padx ,pady=pady)

# booking buttons

# - create
button_create_bookings = tk.Button(button_frame_bookings, text="Create", command=lambda: create_bookings(tree_bookings, read_booking_entries()))
button_create_bookings.grid(row=0, column=1, padx=padx, pady=pady)

# - update
button_update_bookings = tk.Button(button_frame_bookings, text="Update", command=lambda: update_bookings(tree_bookings, read_booking_entries()))
button_update_bookings.grid(row=0, column=2, padx=padx, pady=pady)

# - delete
button_delete_bookings = tk.Button(button_frame_bookings, text="Delete", command=lambda: delete_bookings(tree_bookings, read_booking_entries()))
button_delete_bookings.grid(row=0, column=3, padx=padx, pady=pady)

# - clear
button_clear_bookings = tk.Button(button_frame_bookings, text="Clear", command=clear_booking_entries())
button_clear_bookings.grid(row=0, column=4, padx=padx, pady=pady)
# endregion buttons


# region table formats

# client table format
tree_clients['column'] = ("id", "last_name", "contact")
tree_clients.column("#0", width=0, stretch=tk.NO)
tree_clients.column("id", anchor=tk.E, width=100)
tree_clients.column("last_name", anchor=tk.W, width=150)
tree_clients.column("contact", anchor=tk.W, width=200)
tree_clients.heading("#0", text="", anchor=tk.W)
tree_clients.heading("id", text="ID", anchor=tk.CENTER)
tree_clients.heading("last_name", text="Last name", anchor=tk.CENTER)
tree_clients.heading("contact", text="Contact", anchor=tk.CENTER)
tree_clients.tag_configure('oddrow', background=oddrow)
tree_clients.tag_configure('evenrow', background=evenrow)

# trip table format
tree_trips['column'] = ("id", "route", "date", "capacity")
tree_trips.column("#0", width=0, stretch=tk.NO)
tree_trips.column("id", anchor=tk.E, width=100)
tree_trips.column("route", anchor=tk.W, width=200)
tree_trips.column("date", anchor=tk.W, width=150)
tree_trips.column("capacity", anchor=tk.W, width=100)
tree_trips.heading("#0", text="", anchor=tk.W)
tree_trips.heading("id", text="ID", anchor=tk.CENTER)
tree_trips.heading("route", text="Route", anchor=tk.CENTER)
tree_trips.heading("date", text="Date", anchor=tk.CENTER)
tree_trips.heading("capacity", text="Capacity", anchor=tk.CENTER)
tree_trips.tag_configure('oddrow', background=oddrow)
tree_trips.tag_configure('evenrow', background=evenrow)

# booking table format
tree_bookings['column'] = ("id", "client_id", "trip_id", "seats")
tree_bookings.column("#0", width=0, stretch=tk.NO)
tree_bookings.column("id", anchor=tk.E, width=100)
tree_bookings.column("client_id", anchor=tk.W, width=150)
tree_bookings.column("trip_id", anchor=tk.W, width=150)
tree_bookings.column("seats", anchor=tk.W, width=100)
tree_bookings.heading("#0", text="", anchor=tk.W)
tree_bookings.heading("id", text="ID", anchor=tk.CENTER)
tree_bookings.heading("client_id", text="Client ID", anchor=tk.CENTER)
tree_bookings.heading("trip_id", text="Trip ID", anchor=tk.CENTER)
tree_bookings.heading("seats", text="Seats", anchor=tk.CENTER)
tree_bookings.tag_configure('oddrow', background=oddrow)
tree_bookings.tag_configure('evenrow', background=evenrow)
# endregion table formats


if __name__ == "__main__":
    refresh_treeview(tree_clients, dcd.Clients)
    refresh_treeview(tree_trips, dcd.Trips)
    refresh_treeview(tree_bookings, dcd.Bookings)
    main_window.mainloop()
