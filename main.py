# Typing Tester
# July 2026
# Charles (Chip) Brady
# This program tests the typing speed of a user

import tkinter as tk
import random
from pynput import keyboard
from TypingTester import TypingTester

PANGRAMS = [
    "the quick brown fox jumps over the lazy dog",
    "sphinx of black quartz judge my vow",
    "pack my box with five dozen liquor jugs",
    "jackdaws love my big sphinx of quartz"
]

EXPLAINER1 = "Welcome to the Typing Tester.  This app will test how many words per minute you can type. Click the Start"
EXPLAINER2 = "button, and a random sentence will be generated for you to type.  Once you are done, press Enter, and the"
EXPLAINER3 = "app will calculate how fast you can type.  For every mistake you make, an extra 5 seconds will be added."

ERROR_PENALTY  = 5

# Create window for tkinter
window = tk.Tk()
window.title("Typing Tester")
window.minsize(width=500, height=500)
window.config(padx=10, pady=20, background="white")
# Create Tkinter string variable to hold string value
difficulty_var = tk.StringVar(window, "Easy")

# Set for difficulties
difficulty = ["Easy", "Medium", "Hard"]

# Explanation labels
explainer1Label = tk.Label(text=EXPLAINER1)
explainer2Label = tk.Label(text=EXPLAINER2)
explainer3Label = tk.Label(text=EXPLAINER3)

# Text for countdown
countdownLabel = tk.Label(text="Press Start", font=("Arial", 20))

# Text for random pangram
pangramLabel = tk.Label(text="")

# Text for timer label
timerLabel = tk.Label(text="Time")

# Text for type this label
typeThisLabel = tk.Label(text="Type below", font=("Arial", 10))

# Text for calculation of words per minute
calculateLabel = tk.Label(text="")

# Place the Input for the user to type into
inputEntry = tk.Entry(width=40)
inputEntry.config(state=tk.DISABLED)

game = TypingTester()

def update_timer():
    if game.typing_active:
        game.elapsed_seconds +=1
    # update timer display
    timerLabel.config(text=f"Time: {game.elapsed_seconds}")
    # run it again after 1 second
    window.after(1000, update_timer)


def calculate_wpm(words: int, elapsed_seconds_val: int) -> float:
    """Calculate words per minute"""
    if elapsed_seconds_val == 0:
        return 0
    return (words/elapsed_seconds_val) * 60


def countdown(count=3):
    """ When Start button is pressed, start a countdown.
     Once the countdown is over, begin timer, and display random Pangram from dictionary """
    if count > 0:
        countdownLabel.config(text=str(count))
        window.after(1000, lambda: countdown(count - 1))
    else:
        countdownLabel.config(text="START (Press Enter to Stop)")
        start_test()


def on_press(key):
    """ When enter is pressed on the keyboard, stop the timer."""
    try:
        if key == keyboard.Key.enter and game.typing_active:
            stop_timer()
            return False
    except AttributeError:
        pass


def count_errors():
    """ Compare text in user input to text in pangram, subtract a point for each difference """
    pangram = pangramLabel.cget("text")
    entry = inputEntry.get()

    errors = sum(a != b for a, b in zip(pangram, entry))

    errors += abs(len(pangram) - len(entry))

    return errors


def start_test():
    """Reset the inputs, variables, labels, and buttons. Then choose a pangram and change it based on difficulty and
    display it and begin countdown."""
    # Reset elapsed_seconds
    game.elapsed_seconds = 0
    game.typing_active = True
    # Enable input
    inputEntry.config(state=tk.NORMAL)
    # Erase previous input
    inputEntry.delete(0,tk.END)
    # Clear Previous Calculation
    calculateLabel.config(text="")
    # Choose random pangram
    pangram = random.choice(PANGRAMS)
    words = len(pangram.split())
    # Save word count
    game.word_count = words
    # Change capitalization based on dificulty
    pangram = pangram_modify(pangram)
    # Display random pangram in pangram label after modification
    pangramLabel.config(text=pangram)
    # Place cursor in textbox
    inputEntry.focus_set()
    # Disable Start Button
    startButton.config(state=tk.DISABLED)
    # Start listening for 'Enter' key press
    game.listener = keyboard.Listener(on_press=on_press)
    game.listener.start()


def stop_timer():
    if game.typing_active:
        game.typing_active = False
        if game.listener:
            # Stop the keyboard listener
            game.listener.stop()
    # Compare pangram and user input
    errors = count_errors()
    if errors is None:
        calculateLabel.config(text="ERROR, Try again")

    else:
        # Calculate words per second
        game.elapsed_seconds += errors * ERROR_PENALTY

        wordsPerMinute = calculate_wpm(game.word_count, game.elapsed_seconds)

        calculateLabel.config(text=f"Number of Errors: {int(errors)}. Words per minute count is {int(wordsPerMinute)}. ")
        countdownLabel.config(text=f"Press Start to do it again.")
        startButton.config(state=tk.NORMAL) # Re-enable the start button
        inputEntry.config(state=tk.DISABLED) # Disable input after test

def random_case(pangram: str, uppercase_chance: float) -> str:
    """ Randomly capitalizes or lowercases each letter in a string
        based on a specified chance (0.0 to 1.0)."""
    return "".join(
        char.upper() if random.random() < uppercase_chance else char.lower()
        for char in pangram
    )


def pangram_modify(pangram):
    selected = difficulty_var.get()
    if selected == "Easy":
        return pangram
    elif selected == "Medium":
        return random_case(pangram, 0.5)
    elif selected == "Hard":
        return random_case(pangram, 0.75)

    return pangram


# Create radio buttons using loop
for text in difficulty:
    tk.Radiobutton(window, text=text, variable=difficulty_var,
                value=text).pack(side=tk.TOP, ipady=5)

# Create explainer labels
explainer1Label.pack()
explainer2Label.pack()
explainer3Label.pack()

# Create start button used to enable input
startButton = tk.Button(text="Start", command=countdown)
startButton.pack(pady=(0, 5))

# Create countdown Label
countdownLabel.pack(pady=(0, 5))

# Create Type this Label
typeThisLabel.pack(pady=(0, 5))

# Create pangram Label
pangramLabel.pack(pady=(0, 5))

# Create timer label
timerLabel.pack(pady=(0, 5))

# Create entry Label
inputEntry.pack(pady=(0, 5))

# Create calculate label
calculateLabel.pack(pady=(0, 5))

# Start the non-blocking timer
update_timer()

# Keep Tkinter window open
tk.mainloop()