import tkinter as tk
from datetime import datetime
from tkinter import ttk


def get_date_and_time():
    date = date_entry.get()
    time = time_entry.get()
    journal = journal_entry.get()

    try:
        # Parse the date and time strings
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        time_obj = datetime.strptime(time, "%H:%M:%S")

        # Combine the date and time objects
        combined_datetime = datetime.combine(date_obj.date(), time_obj.time())
        print("Combined Date and Time:", combined_datetime)
        print("Journal Entry: ", journal)

    except ValueError:
        print("Invalid date or time format")


# Create the main window
window = tk.Tk()
window.geometry('444x250')
window.maxsize(444,250)
window.title('DAILY JOURNAL')

# Create the date entry widget
date_label = ttk.Label(window, text="Date (YYYY-MM-DD):")
date_label.pack()
date_entry = ttk.Entry(window)
date_entry.pack()

# Create the time entry widget
time_label = ttk.Label(window, text="Time (HH:MM:SS):")
time_label.pack()
time_entry = ttk.Entry(window)
time_entry.pack()

# Create the journal entry widget
journal_label = ttk.Label(window, text="Journal Entry")
journal_label.pack()
journal_entry = ttk.Entry(window, width=200)
journal_entry.place(x=120, y=100, width=200, height=100)

# Create the button to get the date and time input
get_input_button = ttk.Button(window, text="Submit", command=get_date_and_time)
get_input_button.place(x=180, y=210)

# Run the main event loop
window.mainloop()
