import tkinter as tk
from tkinter import messagebox

# definicion de variables
player='x'
game_over=False

#función para verificar el ganador
def check_winner():
    for i in range (3):
        if buttons [i][0]['text']==buttons [i][1]['text']== buttons[i][2]['text'] !='':
            return True
        if buttons [0][1]['text']==buttons [1][i]['text']== buttons[2][i]['text'] !='':
            return True
    if buttons [0][0]['text']==buttons [1][1]['text']== buttons[2][2]['text'] !='':
            return True   
    if buttons [0][2]['text']==buttons [1][1]['text']== buttons[2][0]['text'] !='':
            return True
    return False

def button_click (row, col):
     global player, game_over
     if buttons[row][col]['text']==''and not game_over:
          buttons[row][col]['text']= player
          buttons[row][col]['bg']= "#5b846c"if player == 'x'else '#196f3d'
          if check_winner():
               messagebox.showinfo (title="Triqui", message=f"Jugador {player} gana!") 
               game_over=True
          elif all(buttons[row][col]['text'] !=''for row in range (3) for col in range(3)):
               messagebox.showinfo(title="triqui", message="¡Es un empate!")
               game_over = True
          else:
               player = '0' if player == 'x' else 'x'

def reset_game ():
     global player, game_over
     player = 'x'
     game_over = False
     for row in range(3):
        for col in range (3):
             buttons [row][col]['text']= ''
             buttons [row][col]['bg']='#196f3d'

root = tk.Tk()
root.title("Triqui")
root.geometry("600x650")
root.configure(bg='#263238')

frame = tk.Frame(root, bg='#263238')  
frame.place(relx=0.5, rely=0.5, anchor='center')

#Arreglo de botones
buttons = [[tk.Button (frame, text='', font='normal 20 bold', width=5, height=2, bg='#263238',fg='white',
                       command=lambda row=row, col=col: button_click(row, col))
            for col in range(3)] for row in range(3)]

for row in range (3):
     for col in range(3):
          buttons[row][col].grid(row=row, column=col, padx=30, pady=30)

reset_button = tk.Button(root, text='Reiniciar', font='normal 15 bold', command= reset_game, 
                         bg = '#0aed69', fg='white')

reset_button.place(relx=0.5, rely=0.9, anchor='center')

root.mainloop()