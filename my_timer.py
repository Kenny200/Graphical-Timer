#timer app
import time
import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("GUI")
label = tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack(padx=20, pady=20)
textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack()
root.mainloop()


'''
user_time = int(input("Enter a number: "))

for x in range(user_time, 0, -1):
    seconds = x % 60
    mintues = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{mintues:02}:{seconds:02}")
    time.sleep(1)

print("Time's Up")
'''