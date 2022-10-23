# https://python-scripts.com/tkinter
# таблица цветов https://www.tcl.tk/man/tcl8.5/TkCmd/colors.html
import tkinter as tk
window = tk.Tk()

#Виджет Label — Отображение текста и картинок
label = tk.Label(text="Семинар 5. \n Крестики-Нолики",
                 fg="coral2",
                 bg="black",
                 width=100, 
                 height=20)
label.pack()

#Создание кнопки через виджет Button
button = tk.Button(
    text="Нажми!",
    width=10,
    height=3,
    bg="coral2",
    fg="black",
    relief=tk.SUNKEN, 
    borderwidth=5
)
button.pack()

#Виджет Text — ввод большого текста
# text_box = tk.Text()
# text_box.pack()


#Рамка

frame_a = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5)
frame_b = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
 
label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()
 
label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

frame_b.pack() 
frame_a.pack()

#relief -стиль рамки


window.mainloop()