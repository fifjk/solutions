import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import plusbus_data as dcd
import plusbus_sql as dcsql
import plusbus_func as dcf

main_window = tk.Tk()
main_window.title('PlusBus')
main_window.geometry("1500x500")


# region global constants
padx = 8
pady = 4
rowheight = 24
treeview_background = '#FFDAF5'
treeview_foreground = 'black'
treeview_selected = '#DF94DB'
oddrow = '#DF94DB'
evenrow = '#CE75BE'
INTERNAL_ERROR_CODE = 0

# style
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.configure("Treeview.Heading", background=treeview_background, foreground=treeview_foreground)

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


# client entry and label frames
controls_frame_clients = tk.Frame(frame_clients)
controls_frame_clients.grid(row=3, column=0, padx=padx, pady=pady)
edit_frame_clients = tk.Frame(controls_frame_clients)
edit_frame_clients.grid(row=0, column=0, padx=padx, pady=pady)

# last name entry
label_clients_last_name = tk.Label(edit_frame_clients, text="Last name")
label_clients_last_name.grid(row=0, column=0, padx=padx, pady=pady)
entry_clients_last_name = tk.Entry(edit_frame_clients, width=4, justify="right")
entry_clients_last_name.grid(row=1, column=0, padx=padx, pady=pady)

# contact entry
label_clients_contact = tk.Label(edit_frame_clients, text="Contact")
label_clients_contact.grid(row=0, column=1, padx=padx, pady=pady)
entry_clients_contact = tk.Entry(edit_frame_clients, width=4, justify="right")
entry_clients_contact.grid(row=1, column=1, padx=padx, pady=pady)


# trip entry and label frames
controls_frame_trips = tk.Frame(frame_trips)
controls_frame_trips.grid(row=3, column=0, padx=padx, pady=pady)
edit_frame_trips = tk.Frame(controls_frame_trips)
edit_frame_trips.grid(row=0, column=0, padx=padx, pady=pady)

# route entry
label_trips_route = tk.Label(edit_frame_trips, text="Route")
label_trips_route.grid(row=0, column=0, padx=padx, pady=pady)
entry_trips_route = tk.Entry(edit_frame_trips, width=4, justify="right")
entry_trips_route.grid(row=1, column=0, padx=padx, pady=pady)

# date entry
label_trips_date = tk.Label(edit_frame_trips, text="Date")
label_trips_date.grid(row=0, column=1, padx=padx, pady=pady)
entry_trips_date = tk.Entry(edit_frame_trips, width=4, justify="right")
entry_trips_date.grid(row=1, column=1, padx=padx, pady=pady)

# capacity entry
label_trips_capacity = tk.Label(edit_frame_trips, text="Capacity")
label_trips_capacity.grid(row=0, column=2, padx=padx, pady=pady)
entry_trips_capacity = tk.Entry(edit_frame_trips, width=4, justify="right")
entry_trips_capacity.grid(row=1, column=2, padx=padx, pady=pady)


# booking entry and label frames
controls_frame_bookings = tk.Frame(frame_bookings)
controls_frame_bookings.grid(row=3, column=0, padx=padx, pady=pady)
edit_frame_bookings = tk.Frame(controls_frame_bookings)
edit_frame_bookings.grid(row=0, column=0, padx=padx, pady=pady)

# client id entry
label_bookings_client_id = tk.Label(edit_frame_bookings, text="Client ID")
label_bookings_client_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_bookings_client_id = tk.Entry(edit_frame_bookings, width=4, justify="right")
entry_bookings_client_id.grid(row=1, column=0, padx=padx, pady=pady)

# trip id entry
label_bookings_trip_id = tk.Label(edit_frame_bookings, text="Trip ID")
label_bookings_trip_id.grid(row=0, column=1, padx=padx, pady=pady)
entry_bookings_trip_id = tk.Entry(edit_frame_bookings, width=4, justify="right")
entry_bookings_trip_id.grid(row=1, column=1, padx=padx, pady=pady)

# seat entry
label_bookings_seats = tk.Label(edit_frame_bookings, text="Seats")
label_bookings_seats.grid(row=0, column=2, padx=padx, pady=pady)
entry_bookings_seats = tk.Entry(edit_frame_bookings, width=4, justify="right")
entry_bookings_seats.grid(row=1, column=2, padx=padx, pady=pady)


# client table format
tree_clients['column'] = ("last_name", "contact")
tree_clients.column("#0", width=0, stretch=tk.NO)
tree_clients.column("last_name", anchor=tk.E, width=150)
tree_clients.column("contact", anchor=tk.W, width=200)
tree_clients.heading("#0", text="", anchor=tk.W)
tree_clients.heading("last_name", text="Last name", anchor=tk.CENTER)
tree_clients.heading("contact", text="Contact", anchor=tk.CENTER)
tree_clients.tag_configure('oddrow', background=oddrow)
tree_clients.tag_configure('evenrow', background=evenrow)

# trip table format
tree_trips['column'] = ("route", "date", "capacity")
tree_trips.column("#0", width=0, stretch=tk.NO)
tree_trips.column("route", anchor=tk.E, width=200)
tree_trips.column("date", anchor=tk.W, width=150)
tree_trips.column("capacity", anchor=tk.W, width=100)
tree_trips.heading("#0", text="", anchor=tk.W)
tree_trips.heading("route", text="Route", anchor=tk.CENTER)
tree_trips.heading("date", text="Date", anchor=tk.CENTER)
tree_trips.heading("capacity", text="Capacity", anchor=tk.CENTER)
tree_trips.tag_configure('oddrow', background=oddrow)
tree_trips.tag_configure('evenrow', background=evenrow)

# booking table format
tree_bookings['column'] = ("client_id", "trip_id", "seats")
tree_bookings.column("#0", width=0, stretch=tk.NO)
tree_bookings.column("client_id", anchor=tk.E, width=150)
tree_bookings.column("trip_id", anchor=tk.W, width=150)
tree_bookings.column("seats", anchor=tk.W, width=100)
tree_bookings.heading("#0", text="", anchor=tk.W)
tree_bookings.heading("client_id", text="Client ID", anchor=tk.CENTER)
tree_bookings.heading("trip_id", text="Trip ID", anchor=tk.CENTER)
tree_bookings.heading("seats", text="Seats", anchor=tk.CENTER)
tree_bookings.tag_configure('oddrow', background=oddrow)
tree_bookings.tag_configure('evenrow', background=evenrow)

if __name__ == "__main__":
    main_window.mainloop()
