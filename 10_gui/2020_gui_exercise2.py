""" Opgave "GUI step 2":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2020.png

Genbrug din kode fra "GUI step 1".

GUI-strukturen bør være som følger:
    main window
        labelframe
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


def empty_entries():
    print("Entries cleared")
    id_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    destination_entry.delete(0, tk.END)
    weather_entry.delete(0, tk.END)


padx = 14
pady = 4

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")

label_frame = tk.LabelFrame(main_window, text="Container")
label_frame.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

frame_1 = tk.Frame(label_frame)
frame_1.grid(row=1, column=0, padx=padx, pady=pady, sticky=tk.N)

id_label = tk.Label(frame_1, text="Id")
id_label.grid(row=2, column=0, padx=padx, pady=pady)

weight_label = tk.Label(frame_1, text="Weight")
weight_label.grid(row=2, column=1, padx=padx, pady=pady)

destination_label = tk.Label(frame_1, text="Destination")
destination_label.grid(row=2, column=2, padx=padx, pady=pady)

weather_label = tk.Label(frame_1, text="Weather")
weather_label.grid(row=2, column=3, padx=padx, pady=pady)

id_entry = tk.Entry(frame_1, width=6)
id_entry.grid(row=3, column=0, padx=padx, pady=pady)

weight_entry = tk.Entry(frame_1, width=10)
weight_entry.grid(row=3, column=1, padx=padx, pady=pady)

destination_entry = tk.Entry(frame_1, width=20)
destination_entry.grid(row=3, column=2, padx=padx, pady=pady)

weather_entry = tk.Entry(frame_1, width=16)
weather_entry.grid(row=3, column=3, padx=padx, pady=pady)

frame_2 = tk.Frame(label_frame)
frame_2.grid(row=4, column=0, padx=padx, pady=pady, sticky=tk.N)

create_button = tk.Button(frame_2, text="Create")
create_button.grid(row=5, column=0, padx=padx, pady=pady)

update_button = tk.Button(frame_2, text="Update")
update_button.grid(row=5, column=1, padx=padx, pady=pady)

delete_button = tk.Button(frame_2, text="Delete")
delete_button.grid(row=5, column=2, padx=padx, pady=pady)

clear_button = tk.Button(frame_2, text="Clear Entry Boxes", command=empty_entries)
clear_button.grid(row=5, column=3, padx=padx, pady=pady)


if __name__ == "__main__":
    main_window.mainloop()