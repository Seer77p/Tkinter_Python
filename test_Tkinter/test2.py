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
# frame1 = tk.Frame(master=window, height=100, bg="red")
# frame1.pack(fill=tk.X)
# frame2 = tk.Frame(master=window, height=50, bg="yellow")
# frame2.pack(fill=tk.X)
# frame3 = tk.Frame(master=window, height=25, bg="blue")
# frame3.pack(fill=tk.X)

# Аргумент side от метода .pack() уточняет, на какую сторону окна виджет должен размещаться
# frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
# frame1.pack(fill=tk.Y, side=tk.LEFT)
# frame2 = tk.Frame(master=window, width = 100, bg="yellow")
# frame2.pack(fill=tk.Y, side =tk.LEFT)
# frame3 = tk.Frame(master=window, width=50, bg="blue")
# frame3.pack(fill=tk.Y, side=tk.LEFT)

# Для того чтобы сделать макет по-настоящему адаптированным, 
# #можно установить начальный размер фреймов, используя атрибуты width и height. 
# #Затем нужно установить значение аргумента fill от метода .pack() на tk.BOTH, 
# #а также установить значение аргумента expand на True:
# frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
# frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
# frame2 = tk.Frame(master=window, width=100, bg="yellow")
# frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
# frame3 = tk.Frame(master=window, width=50, bg="blue")
# frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# Для управления точным местом расположения виджета в окне или в 
# рамке используется менеджер .place(). Вы должны указать два 
# ключевых аргумента x и y, которые определяют координаты x и y для 
# верхнего левого угла виджета. Аргументы x и y измеряются в пикселях, 
# а не в текстовых юнитах.
# Строки 5 и 6 создают новый виджет рамки Frame под названием frame1, 
# его ширина 150 пикселей и высота также 150 пикселей, и упаковывают 
# его в окно с помощью .pack()
# Строки 8 и 9 создают новый ярлык с текстом под названием label1 с 
# красным фоном и помещает его в рамку frame1 на позицию(0, 0)
# Строки 11 и 12 создают второй ярлык с текстом под названием label2 
# на желтом фоне и помещают его в рамку frame1 на позицию(75, 75).
# frame = tk.Frame(master=window, width=150, height=150)
# frame.pack()
# label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
# label1.place(x=0, y=0)
# label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
# label2.place(x=75, y=75)


# Самым популярным менеджером геометрии в Tkinter является .grid(). 
# Он обладает всей мощностью .pack(), будучи намного более простым в использовании.
# Менеджер .grid() работает путем разделения окна или рамки на строки и столбцы(на сетку). 
# Вы указываете местоположение виджета, вызывая метод .grid() и 
# передавая индексы row и column(строки и столбца) в ключевые аргументы строки и столбца соответственно.

# for i in range(3):
#     window.columnconfigure(i, weight=1, minsize=75)
#     window.rowconfigure(i, weight=1,minsize=50 )
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j, padx=5, pady=5)
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack(padx=5, pady=5)

# По умолчанию виджеты центрируются в своих ячейках сетки. К примеру, 
# следующий код создает два ярлыка с текстом и помещает их в сетку с одним столбцом и двумя строками:
# Ширина каждой ячейка сетки 250 пикселей, высота 100 пикселей. 
# Ярлыки с текстом помещаются в центре каждой ячейки, как показано в следующей фигуре:
# window.columnconfigure(0, minsize=250)
# window.rowconfigure([0, 1], minsize=100)
# label1 = tk.Label(text="A")
# label1.grid(row=0, column=0)
# label2 = tk.Label(text="B")
# label2.grid(row=1, column=0)


# Вы можете поменять расположение каждого ярлыка внутри ячейки сетки, 
# используя параметр sticky. Параметр sticky принимает строку, 
# что содержит одну или несколько из следующих букв:
# «n» или «N» — Север — выравнивает по верхней центральной части ячейки
# «e» или «E» — Запад — выравнивает по правой центральной части ячейки
# «s» или «S» — Юг — выравнивает по нижней центральной части ячейки
# «w» или «W» — Восток — выравнивает по левой центральной части ячейки.
# Буквы «n», «s», «e» и «w» идут по траектории с севера, на юг, 
# затем восток и запад. Установка параметра sticky со значением «n» 
# для обоих ярлыков из предыдущего кода позиционируют каждый ярлык с 
# текстом в верхнюю центральную ячейку сетки:
# Можно комбинировать несколько букв в одной строке для позиционирования 
# каждого ярлыка в углу его ячейки из сетки:
# window.columnconfigure(0, minsize=250)
# window.rowconfigure([0, 1], minsize=100)
# label1 = tk.Label(text="A")
# label1.grid(row=0, column=0, sticky="ne")
# label2 = tk.Label(text="B")
# label2.grid(row=1, column=0, sticky="sw")


# Когда виджет позиционируется через sticky, 
# размера самого виджета достаточно для размещения любого текста 
# и другого содержимого внутри него. Он не заполнить всю ячейку сетки. 
# Для заполнения всей сетки можно указать "ns", заставив виджет заполнить 
# ячейку в вертикальном направлении, или "ew" для заполнения ячейки в горизонтальном направлении. 
# Для заполнения всей ячейки в sticky требуется указать "nsew".
window.rowconfigure(0, minsize=50)
window.columnconfigure([0, 1, 2, 3], minsize=50)
label1 = tk.Label(text="1", bg="black", fg="white")
label2 = tk.Label(text="2", bg="black", fg="white")
label3 = tk.Label(text="3", bg="black", fg="white")
label4 = tk.Label(text="4", bg="black", fg="white")
label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky="ew")
label3.grid(row=0, column=2, sticky="ns")
label4.grid(row=0, column=3, sticky="nsew")

# Приведенный выше пример демонстрирует то, что параметр sticky 
# от менеджера геометрии .grid() может использоваться для достижения 
# тех же эффектов, что и параметр fill от менеджера геометрии .pack(). 
# Параллели между параметрами sticky и fill представлены в следующей таблице:
# Метод grid()	      Метод pack()
# sticky = "ns"	      fill = tk.Y
# sticky = "ew"	      fill = tk.X
# sticky = "nsew"     fill = tk.BOTH
# Метод .grid() является довольно мощным менеджером геометрии. 
# Зачастую его проще понять, чем менеджер .pack(). 
# Он также универсальнее, нежели менеджер .place(). 
# При создании новых приложений в Tkinter, в качестве основного 
# менеджера геометрии лучше рассматривать .grid().


window.mainloop()
