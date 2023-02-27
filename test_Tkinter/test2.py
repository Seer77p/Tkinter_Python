import tkinter as tk

window = tk.Tk()

# entry = tk.Entry(fg="black", bg="white", width=40)
# entry.insert(0, 'What is yuor name?')

# entry=tk.Entry(width=40) # так как цвет фона по стандарту белый а шрифт черный fg и bg можно не писать
# entry.insert(0, 'What is yuor name?')
# entry.pack()

# frame1=tk.Frame(master=window, width=100, height=100, bg="red")
# frame1.pack()

# frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
# frame2.pack()

# frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
# frame3.pack()

# Можно установить ключевой аргумент fill для уточнения в какое направление рамки будут пополняться
# Доступная оптиция tk.X для горизонтального направления и для tk.Y для вертикального  BOTH для обоих
frame1 = tk.Frame(master=window, height=100, bg="red")
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=window, height=50, bg="yellow")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=window, height=25, bg="blue")
frame3.pack(fill=tk.X)


window.mainloop()
