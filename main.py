import tkinter
import random

COLOR_MAIN = "#FFA07A"
COLOR_ELEMENTS = "#FA8072"
COLOR_ACTION = "#8B0000"

anecdotes = [
    'Шел медведь по лесу видит машина горит, сел в нее и сгорел',
    'Купил мужик шляпу, а она ему как раз',
    '''Мама собирает сыну обед в школу:
— Вот, положила тебе в ранец хлеб, колбасу и гвозди.
— Мам, нафига??
— Ну как же, берешь хлеб, кладешь на него колбасу и ешь.
— А гвозди?
— Так вот же они!''']


def get_random_anecdote():
    random_anecdote = random.choice(anecdotes)
    label1['text'] = random_anecdote


root = tkinter.Tk()  # объект главного окна
root.geometry("400x600")
root['bg'] = COLOR_MAIN


button = tkinter.Button(
    text="Сгенерировать",
    command=get_random_anecdote,
    bg=COLOR_ELEMENTS,
    activebackground=COLOR_ACTION
)
button.pack()

label2 = tkinter.Label(bg=COLOR_MAIN)
label2.pack()

label1 = tkinter.Label(text="Здесь мог быть ваш анекдот", bg=COLOR_MAIN)
label1.pack()

root.mainloop()  # главный цикл событий
