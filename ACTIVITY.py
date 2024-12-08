import tkinter as tk
import random


def play(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "You lose!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors")

for choice in ["Rock", "Paper", "Scissors"]:
    tk.Button(root, text=choice, command=lambda c=choice: play(c)).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
