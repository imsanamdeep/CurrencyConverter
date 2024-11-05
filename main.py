from currency_converter import CurrencyConverter
import tkinter as tk

c = CurrencyConverter()

history = []

def clicked():
    amount = int(entry1.get())
    cur1 = entry2.get().upper()
    cur2 = entry3.get().upper()
    data = c.convert(amount, cur1, cur2)
    
    history.append(f"{amount} {cur1} = {data:.2f} {cur2}")
    
    label4.config(text=f"Converted Amount: {data:.2f} {cur2}")

def show_history():
    history_window = tk.Toplevel(window)
    history_window.geometry("400x300")
    history_window.title("Conversion History")

    history_label = tk.Label(history_window, text="Conversion History", font="Times 16 bold")
    history_label.pack(pady=10)

    for item in history:
        history_entry = tk.Label(history_window, text=item, font="Times 12")
        history_entry.pack()

def reset_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    label4.config(text="")

window = tk.Tk()
window.geometry("500x400")
window.title("Currency Converter")

label = tk.Label(window, text="Currency Converter", font="Times 20 bold")
label.place(x=120, y=40)

label1 = tk.Label(window, text="Enter amount here:", font="Times 16 bold")
label1.place(x=70, y=100)
entry1 = tk.Entry(window)

label2 = tk.Label(window, text="Enter your currency here:", font="Times 16 bold")
label2.place(x=30, y=150)
entry2 = tk.Entry(window)

label3 = tk.Label(window, text="Enter your desired currency:", font="Times 16 bold")
label3.place(x=15, y=200)
entry3 = tk.Entry(window)

button_convert = tk.Button(window, text="Convert", font="Times 16 bold", command=clicked)
button_convert.place(x=80, y=250)

button_history = tk.Button(window, text="History", font="Times 16 bold", command=show_history)
button_history.place(x=180, y=250)

button_reset = tk.Button(window, text="Reset", font="Times 16 bold", command=reset_fields)
button_reset.place(x=280, y=250)

label4 = tk.Label(window, font="Times 16 bold")
label4.place(x=150, y=300)

entry1.place(x=270, y=105)
entry2.place(x=270, y=155)
entry3.place(x=270, y=205)

window.mainloop()
