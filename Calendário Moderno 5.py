from tkinter import *
from tkcalendar import *

root = Tk()

def choice_date():
    present_date = display_cal.get_date()
    user_date = Label(text=present_date)
    user_date.pack(padx=2, pady=2)

def update_year():
    try:
        new_year = int(year_entry.get())
        # Define uma nova data no calendário (primeiro dia do ano informado)
        display_cal.selection_set(f"01/01/{new_year}")
    except ValueError:
        error_label = Label(root, text="Digite um ano válido!", fg="red")
        error_label.pack(padx=2, pady=2)

display_cal = Calendar(root, setmode="day", date_pattern='d/m/yyyy')
display_cal.pack(padx=15, pady=15)

# Adicionando a caixa de texto para entrada de ano
year_label = Label(root, text="Digite o ano:", bg="cyan", font=("Arial",12))
year_label.pack(padx=5, pady=5)

year_entry = Entry(root)
year_entry.pack(padx=5, pady=5)

go_to_year = Button(root, text="Ir para o ano", command=update_year, font=("Arial",14,"bold"), bg="darkgreen", fg="white")
go_to_year.pack(padx=15, pady=15)

root.geometry('400x400')
root.title("Calendário Moderno")
root.configure(bg="cyan")
root.mainloop()
