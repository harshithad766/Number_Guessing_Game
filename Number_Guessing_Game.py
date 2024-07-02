import tkinter as tk
from tkinter import messagebox
import random
import time

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")
        self.number = random.randint(1, 200)
        self.guessesTaken = 0

        self.name_label = tk.Label(root, text="May I ask you for your name?")
        self.name_label.pack(pady=10)

        self.name_entry = tk.Entry(root, width=50)
        self.name_entry.pack(pady=10)

        self.name_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.name_button.pack(pady=5)

        self.info_label = tk.Label(root, text="")
        self.info_label.pack(pady=10)

        self.guess_entry = tk.Entry(root, width=50)
        self.guess_entry.pack(pady=10)

        self.guess_button = tk.Button(root, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=5)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=5)
        self.play_again_button.config(state=tk.DISABLED)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=5)

    def start_game(self):
        self.name = self.name_entry.get()
        if self.name:
            self.name_label.config(text=f"{self.name}, we are going to play a game. I am thinking of a number between 1 and 200.")
            self.name_entry.config(state=tk.DISABLED)
            self.name_button.config(state=tk.DISABLED)
            self.info_label.config(text="Go ahead. Guess!")
        else:
            messagebox.showwarning("Input Error", "Please enter your name.")

    def make_guess(self):
        if self.guessesTaken < 6:
            enter = self.guess_entry.get()
            try:
                guess = int(enter)
                if 1 <= guess <= 200:
                    self.guessesTaken += 1
                    if guess < self.number:
                        self.result_label.config(text="The guess of the number that you have entered is too low. Try Again!")
                    elif guess > self.number:
                        self.result_label.config(text="The guess of the number that you have entered is too high. Try Again!")
                    else:
                        self.result_label.config(text=f'Good job, {self.name}! You guessed my number in {self.guessesTaken} guesses!')
                        self.end_game()
                else:
                    messagebox.showwarning("Input Error", "Please enter a number between 1 and 200.")
            except ValueError:
                messagebox.showwarning("Input Error", f"I don't think that '{enter}' is a number. Sorry.")
        if self.guessesTaken >= 6 and self.number != guess:
            self.result_label.config(text=f'Nope. The number I was thinking of was {self.number}')
            self.end_game()

    def end_game(self):
        self.guess_entry.config(state=tk.DISABLED)
        self.guess_button.config(state=tk.DISABLED)
        self.play_again_button.config(state=tk.NORMAL)

    def reset_game(self):
        self.number = random.randint(1, 200)
        self.guessesTaken = 0
        self.name_entry.config(state=tk.NORMAL)
        self.name_button.config(state=tk.NORMAL)
        self.guess_entry.config(state=tk.NORMAL)
        self.guess_button.config(state=tk.NORMAL)
        self.play_again_button.config(state=tk.DISABLED)
        self.name_entry.delete(0, tk.END)
        self.guess_entry.delete(0, tk.END)
        self.name_label.config(text="May I ask you for your name?")
        self.info_label.config(text="")
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
