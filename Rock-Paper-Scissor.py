import tkinter as tk
from tkinter import Label, Button
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        master.title("Rock, Paper, Scissors Game")

        # Initialize scores
        self.user_score = 0
        self.computer_score = 0

        # Label to display game instructions
        self.instructions_label = Label(master, text="Choose Rock, Paper, or Scissors:")
        self.instructions_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Buttons for user choices
        self.rock_button = Button(master, text="Rock", command=lambda: self.play_game("rock"))
        self.rock_button.grid(row=1, column=0, padx=10, pady=10)

        self.paper_button = Button(master, text="Paper", command=lambda: self.play_game("paper"))
        self.paper_button.grid(row=1, column=1, padx=10, pady=10)

        self.scissors_button = Button(master, text="Scissors", command=lambda: self.play_game("scissors"))
        self.scissors_button.grid(row=1, column=2, padx=10, pady=10)

        # Label to display user and computer choices
        self.choices_label = Label(master, text="")
        self.choices_label.grid(row=2, column=0, columnspan=3, pady=10)

        # Label to display game result
        self.result_label = Label(master, text="")
        self.result_label.grid(row=3, column=0, columnspan=3, pady=10)

        # Label to display scores
        self.scores_label = Label(master, text="User: 0  |  Computer: 0")
        self.scores_label.grid(row=4, column=0, columnspan=3, pady=10)

    def play_game(self, user_choice):
        # Map integers to choices for easy comparison
        choices = {0: "rock", 1: "paper", 2: "scissors"}

        # Generate a random choice for the computer
        computer_choice = random.randint(0, 2)

        # Determine the winner
        if user_choice == choices[(computer_choice + 1) % 3]:
            result = "You win!"
            self.user_score += 1
        elif user_choice == choices[(computer_choice - 1) % 3]:
            result = "You lose!"
            self.computer_score += 1
        else:
            result = "It's a tie!"

        # Update the labels with choices and result
        self.choices_label.config(text=f"Your choice: {user_choice.capitalize()} | Computer choice: {choices[computer_choice].capitalize()}")
        self.result_label.config(text=result)
        self.scores_label.config(text=f"User: {self.user_score}  |  Computer: {self.computer_score}")

if __name__ == '__main__':
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
