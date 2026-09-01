"""Opgave "Calculator with GUI"

Løs opgave 0700_calculator_exercise.py med en GUI
start
Kopier denne fil til din egen løsningsmappe. Skriv din løsning i kopien.

Hvis du går i stå, spørg Google, andre elever, en AI eller læreren.

Når dit program er færdigt, skub det til dit GitHub-repository.
"""
import tkinter as tk

def number_input(number):
    entry.insert(tk.END, number)

def clear_entry():
    entry.delete(0, tk.END)

def get_entry():
    sum = eval(entry.get())
    clear_entry()
    entry.insert(tk.END, str(sum))


padx = 0
pady = 1
width = 5
height = 2

main_window = tk.Tk()
main_window.title('Calculator')
main_window.geometry("230x270")


label_frame = tk.LabelFrame(main_window, bg="#7A6695")
label_frame.grid(row=0, column=0, padx=2, pady=2, sticky=tk.N)


frame_1 = tk.Frame(label_frame, bg="#7A6695")
frame_1.grid(row=1, column=0, padx=0, pady=0, sticky=tk.N)

entry = tk.Entry(frame_1, width=17, font=("Impact", 15), bg="#B6A3CE")
entry.grid(row=1, column=0, padx=10, pady=10)

frame_2 = tk.Frame(label_frame, bg="#7A6695")
frame_2.grid(row=2, column=0, padx=0, pady=0)

clear_button = tk.Button(frame_2, text="Clear", width=5, height=2, command=clear_entry, bg="#B6A3CE")
clear_button.grid(row=0, column=6, padx=0, pady=0)


button_1 = tk.Button(frame_2, text="1", width=width, height=height, command=lambda: number_input("1"), bg="#B6A3CE")
button_1.grid(row=2, column=0, padx=padx, pady=pady)

button_2 = tk.Button(frame_2, text="2", width=width, height=height, command=lambda: number_input("2"), bg="#B6A3CE")
button_2.grid(row=2, column=1, padx=padx, pady=pady)

button_3 = tk.Button(frame_2, text="3", width=width, height=height, command=lambda: number_input("3"), bg="#B6A3CE")
button_3.grid(row=2, column=2, padx=padx, pady=pady)

button_4 = tk.Button(frame_2, text="4", width=width, height=height, command=lambda: number_input("4"), bg="#B6A3CE")
button_4.grid(row=3, column=0, padx=padx, pady=pady)

button_5 = tk.Button(frame_2, text="5", width=width, height=height, command=lambda: number_input("5"), bg="#B6A3CE")
button_5.grid(row=3, column=1, padx=padx, pady=pady)

button_6 = tk.Button(frame_2, text="6", width=width, height=height, command=lambda: number_input("6"), bg="#B6A3CE")
button_6.grid(row=3, column=2, padx=padx, pady=pady)

button_7 = tk.Button(frame_2, text="7", width=width, height=height, command=lambda: number_input("7"), bg="#B6A3CE")
button_7.grid(row=4, column=0, padx=padx, pady=pady)

button_8 = tk.Button(frame_2, text="8", width=width, height=height, command=lambda: number_input("8"), bg="#B6A3CE")
button_8.grid(row=4, column=1, padx=padx, pady=pady)

button_9 = tk.Button(frame_2, text="9", width=width, height=height, command=lambda: number_input("9"), bg="#B6A3CE")
button_9.grid(row=4, column=2, padx=padx, pady=pady)

comma_button = tk.Button(frame_2, text=".", width=width, height=height, command=lambda: number_input("."), bg="#B6A3CE")
comma_button.grid(row=5, column=0, padx=padx, pady=pady)

button_0 = tk.Button(frame_2, text="0", width=width, height=height, command=lambda: number_input("0"), bg="#B6A3CE")
button_0.grid(row=5, column=1, padx=padx, pady=pady)

equal_button = tk.Button(frame_2, text="=", width=width, height=height, command=get_entry, bg="#B6A3CE")
equal_button.grid(row=5, column=2, padx=padx, pady=pady)

plus_button = tk.Button(frame_2, text="+", width=width, height=height, command=lambda: number_input("+"), bg="#B6A3CE")
plus_button.grid(row=2, column=6, padx=10, pady=pady)

minus_button = tk.Button(frame_2, text="-", width=width, height=height, command=lambda: number_input("-"), bg="#B6A3CE")
minus_button.grid(row=3, column=6, padx=10, pady=pady)

multiply_button = tk.Button(frame_2, text="*", width=width, height=height, command=lambda: number_input("*"), bg="#B6A3CE")
multiply_button.grid(row=4, column=6, padx=10, pady=pady)

divide_button = tk.Button(frame_2, text="/", width=width, height=height, command=lambda: number_input("/"), bg="#B6A3CE")
divide_button.grid(row=5, column=6, padx=10, pady=pady)

if __name__ == "__main__":
    main_window.mainloop()