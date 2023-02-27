import tkinter as tk

window = tk.Tk()
# label = tk.Label(text="Hello, Tkinter", fg="white", bg="#34A2EF",
#                  width=40, height=20)  # функция создания ярлыка по параметрам
# # делает кнопку на которую можно нажать
# button = tk.Button(text="Нажми меня", width=25,
#                    height=5, bg="blue", fg="yellow")


# entry = tk.Entry(fg="yellow", bg="blue", width=50)  # делает окно в которое можно вносить информацию

# label1 = tk.Label(text="Имя")
# entry1 = tk.Entry()
# name=entry1.get()
# entry1.delete(0)
# entry.insert(0, 'Иванов')
# entry.insert(0, 'Иван ')

# text_box=tk.Text() #Введение многострочного текста
# text_box.get("1.0") #для получения первой буквы  созданного ранее бокса Hello
#                                                                        # World
# # text_box.get("1.0", "1.5") для получения первой буквы  созданного ранее бокса Hello
#                                                                                 # World
# frame=tk.Frame()
# label=tk.Label(master=frame)

# frame_a=tk.Frame()
# frame_b=tk.Frame()
# label_a=tk.Label(master=frame_a, text="I'm in Frame A")
# label_a.pack()

# label_b = tk.Label(master=frame_b, text="I'm in Frame B")
# label_b.pack()

# frame_b.pack()
# frame_a.pack()


# label.pack()
# button.pack()
# entry.pack()
# label1.pack()
# entry1.pack()
# text_box.pack()
# frame.pack()
border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=7)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

window.mainloop()
