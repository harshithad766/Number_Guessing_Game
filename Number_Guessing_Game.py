import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")  # Set the title of the GUI window

        # Generate a random number between 1 and 200
        self.number = random.randint(1, 200)
        self.guessesTaken = 0  # Initialize the number of guesses taken

        # Label and entry for the player's name
        self.name_label = tk.Label(root, text="May I ask you for your name?")
        self.name_label.pack(pady=10)

        self.name_entry = tk.Entry(root, width=50)
        self.name_entry.pack(pady=10)

        # Button to start the game
        self.name_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.name_button.pack(pady=5)

        # Label to display game information
        self.info_label = tk.Label(root, text="")
        self.info_label.pack(pady=10)

        # Entry for the player to enter their guess
        self.guess_entry = tk.Entry(root, width=50)
        self.guess_entry.pack(pady=10)

        # Button to submit the guess
        self.guess_button = tk.Button(root, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=5)

        # Label to display the result of the guess
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        # Button to play the game again
        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=5)
        self.play_again_button.config(state=tk.DISABLED)  # Initially disable the button

        # Button to quit the game
        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=5)

    def start_game(self):
        self.name = self.name_entry.get()  # Get the player's name
        if self.name:
            # Update the label to show the player's name and game instructions
            self.name_label.config(text=f"{self.name}, we are going to play a game. I am thinking of a number between 1 and 200.")
            self.name_entry.config(state=tk.DISABLED)  # Disable the name entry
            self.name_button.config(state=tk.DISABLED)  # Disable the start button
            self.info_label.config(text="Go ahead. Guess!")
        else:
            messagebox.showwarning("Input Error", "Please enter your name.")  # Show warning if name is not entered

    def make_guess(self):
        if self.guessesTaken < 6:  # Allow up to 6 guesses
            enter = self.guess_entry.get()
            try:
                guess = int(enter)  # Convert the guess to an integer
                if 1 <= guess <= 200:  # Check if the guess is within the valid range
                    self.guessesTaken += 1
                    if guess < self.number:
                        self.result_label.config(text="The guess of the number that you have entered is too low. Try Again!")
                    elif guess > self.number:
                        self.result_label.config(text="The guess of the number that you have entered is too high. Try Again!")
                    else:
                        self.result_label.config(text=f'Good job, {self.name}! You guessed my number in {self.guessesTaken} guesses!')
                        self.end_game()  # End the game if the guess is correct
                else:
                    messagebox.showwarning("Input Error", "Please enter a number between 1 and 200.")
            except ValueError:
                messagebox.showwarning("Input Error", f"I don't think that '{enter}' is a number. Sorry.")
        
        # If the player has taken 6 guesses and hasn't guessed the number
        if self.guessesTaken >= 6 and self.number != guess:
            self.result_label.config(text=f'Nope. The number I was thinking of was {self.number}')
            self.end_game()

    def end_game(self):
        self.guess_entry.config(state=tk.DISABLED)  # Disable the guess entry
        self.guess_button.config(state=tk.DISABLED)  # Disable the guess button
        self.play_again_button.config(state=tk.NORMAL)  # Enable the play again button

    def reset_game(self):
        self.number = random.randint(1, 200)  # Generate a new random number
        self.guessesTaken = 0  # Reset the number of guesses
        self.name_entry.config(state=tk.NORMAL)  # Enable the name entry
        self.name_button.config(state=tk.NORMAL)  # Enable the start button
        self.guess_entry.config(state=tk.NORMAL)  # Enable the guess entry
        self.guess_button.config(state=tk.NORMAL)  # Enable the guess button
        self.play_again_button.config(state=tk.DISABLED)  # Disable the play again button
        self.name_entry.delete(0, tk.END)  # Clear the name entry
        self.guess_entry.delete(0, tk.END)  # Clear the guess entry
        self.name_label.config(text="May I ask you for your name?")  # Reset the name label
        self.info_label.config(text="")  # Clear the info label
        self.result_label.config(text="")  # Clear the result label

if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    game = GuessingGame(root)  # Create an instance of the GuessingGame class
    root.mainloop()  # Run the application
