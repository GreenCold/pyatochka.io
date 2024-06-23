import tkinter as tk

# Создание главного окна:
root = tk.Tk()  
root.title("Кликер")
root.geometry("700x350")
root.resizable(False, False)
root.configure(bg="#d1ddde")

n = 0  # Счётчик

def nplus():
    global n
    n += 1
    if n == 1:
        label1["text"] = str(n) + " Пятка."
    elif 1 < n <= 3:
        label1["text"] = str(n) + " Пятки."
    else:
        label1["text"] = str(n) + " Пяток."

def nsbros():
    global n
    n = 0
    label1["text"] = str(n) + " Пяток."

# Счётчик кликера:
label1 = tk.Label(root, text=str(n) + " Пяток.", font=("Helvetica 50"), background="#d1ddde")
label1.pack()

# Кнопка 1:
btn1 = tk.Button(text="Клик", background="#75a9fa", foreground="#fff",
                 padx="150", pady="10", font="16", command=nplus)
btn1.pack()

root.mainloop()