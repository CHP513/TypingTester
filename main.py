# Typing Tester
# March 2026
# Charles (Chip) Brady
# This program tests the typing speed of a user

from tkinter import *
import random, time
from pynput import keyboard

# List of Pangrams (Sentences that uses every letter) the user has to type
PANGRAM1 = "the quick brown fox jumps over the lazy dog"
PANGRAM2 = "sphinx of black quartz judge my vow"
PANGRAM3 = "pack my box with five dozen liquor jugs"
PANGRAM4 = "jackdaws love my big sphinx of quartz"

PANGRAMDICT = [PANGRAM1, PANGRAM2, PANGRAM3, PANGRAM4]
PANGRAMWORDCOUNT = [9, 7, 8, 7]

PANGRAMLIST = list(PANGRAMDICT)
PANGRAMWORDCOUNTLIST = list(PANGRAMWORDCOUNT)

EXPLAINER1 = ("Welcome to the Typing Tester.  This app will test how many words per minute you can type. Click the Start")
EXPLAINER2 = ("button, and a random sentence will be generated for you to type.  Once you are done, press Enter, and the")
EXPLAINER3 = ("app will calculate how fast you can type.  For every mistake you make, an extra 5 seconds will be added.")

# Create window for tkinter
window = Tk()
window.title("Typing Tester")
window.minsize(width=500, height=500)
window.config(padx=10, pady=20, background="white")
# Create Tkinter string variable to hold string value
v = StringVar(window, "Easy")

# Set for difficulties
difficulty = ["Easy", "Medium", "Hard"]

seconds = 0
# Flag to indicate if typing test is active
typing_active = False
# Listener for keyboard
listener = None

# Explanation labels
explainer1Label = Label(text=EXPLAINER1)
explainer2Label = Label(text=EXPLAINER2)
explainer3Label = Label(text=EXPLAINER3)

# Text for countdown
countdownLabel = Label(text="Press Start", font=("Arial", 20))

# Text for random pangram
pangramLabel = Label(text="")

# Text for timer label
timerLabel = Label(text="Time")

# Text for calculation of words per minute
calculateLabel = Label(text="")

# Place the Input for the user to type into
inputEntry = Entry(width=40)
inputEntry.config(state=DISABLED)

# Timer that starts counting
def timer(seconds_val):
    global seconds
    seconds = seconds_val + 1

def update_timer():
    global seconds, typing_active
    if typing_active:
        seconds +=1
    # update timer display
    timerLabel.config(text=f"Time: {seconds}")
    # run itself again after 1 second
    window.after(1000, update_timer)

# Calculate words per minute
def calculate(words, seconds_val):
    if seconds_val == 0:
        return 0
    return (words/seconds_val) * 60

# When Start button is pressed, start a countdown.
# Once the countdown is over, begin timer, and display random Pangram from dictionary
def countdown():
    countdownLabel.config(text="Get Ready")
    window.update()
    time.sleep(1)
    countdownLabel.config(text="3")
    window.update()
    time.sleep(1)
    countdownLabel.config(text="2")
    window.update()
    time.sleep(1)
    countdownLabel.config(text="1")
    window.update()
    time.sleep(1)
    countdownLabel.config(text="START (Press enter to Stop)")
    window.update()

# When enter is pressed on the keyboard, stop the timer.
def on_press(key):
    global typing_active
    try:
        if key == keyboard.Key.enter and typing_active:
            stop_timer()
            return False
    except AttributeError:
        pass

# Compare text in user input to text in pangram, subtract a point for each difference
def compare():
    # Put each char in pangram into a list
    list_pangram = list(pangramLabel.cget("text"))
    # Put each char in input into a list
    list_entry = list(inputEntry.get())

    if list_entry == []:
        return None

    # Get length of pangram or test depending on which is longer
    len_pangram = len(list_pangram)
    len_entry = len(list_entry)

    errors = 0
    # Iterate through the shorter of the two lists
    for i in range(min(len(list_pangram), len(list_entry))):
        if list_pangram[i] != list_entry[i]:
            errors += 1

    # Add errors for extra characters or missing characters
    errors += abs(len(list_pangram) - len(list_entry))

    return errors

def start():
    global seconds, typing_active, listener
    # Reset seconds
    seconds = 0
    typing_active = True
    # Enable input
    inputEntry.config(state=NORMAL)
    # Erase previous input
    inputEntry.delete(0,END)
    # Clear Previous Calculation
    calculateLabel.config(text="")
    # Choose random pangram
    pangramChoose = random.randint(0,3)
    # Modify pangram after chosen
    pangramChosen = pangram_modify(PANGRAMLIST[pangramChoose])
    # Countdown timer
    countdown()
    # Display random pangram in pangram label after modification
    pangramLabel.config(text=pangramChosen)
    # Place cursor in textbox
    inputEntry.focus_set()
    # Disable Start Button
    startButton.config(state=DISABLED)
    window.update()
    # Start the non-blocking timer
    update_timer()
    # Start listening for 'Enter' key press
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

def stop_timer():
    global typing_active, listener, seconds
    if typing_active:
        typing_active = False
        if listener:
            # Stop the keyboard listener
            listener.stop()
    # Compare pangram and user input
    errors = compare()
    if errors is None:
        calculateLabel.config(text="ERROR, Try again")

    else:
    # Calculate words per second
        # Add 5 seconds per error
        seconds += errors * 5

        pangram_chosen_index = PANGRAMLIST.index(pangramLabel.cget("text")) # Get the index of the displayed pangram
        wordsPerMinute = calculate(PANGRAMWORDCOUNTLIST[pangram_chosen_index], seconds)

        calculateLabel.config(text=f"Words per minute count is {int(wordsPerMinute)}. Press start to do it again")
        startButton.config(state=NORMAL) # Re-enable the start button
        inputEntry.config(state=DISABLED) # Disable input after test

# This funtion randomly captitalizes the letters in the pangram based on percentage
def random_case(pangram, uppercase_chance):
    """ Randomly capitalizes or lowercases each letter in a string
        based on a specified chance (0.0 to 1.0)."""
    return "".join(
        char.upper() if random.random() < uppercase_chance else char.lower()
        for char in pangram
    )

def pangram_modify(pangram):
    selected = v.get()
    if selected == "Easy":
        return pangram
    elif selected == "Medium":
        return random_case(pangram, 0.5)
    elif selected == "Hard":
        return random_case(pangram, 0.75)

    return pangram

# Create radio buttons using loop
for text in difficulty:
    Radiobutton(window, text=text, variable=v,
                value=text).pack(side=TOP, ipady=5)

# Create explainer labels
explainer1Label.pack()
explainer2Label.pack()
explainer3Label.pack()

# Create start button used to enable input
startButton = Button(text="Start", command=start)
startButton.pack(pady=(0, 5))

# Create countdown Label
countdownLabel.pack(pady=(0, 5))

# Create pangram Label
pangramLabel.pack(pady=(0, 5))

# Create timer label
timerLabel.pack(pady=(0, 5))

# Create entry Label
inputEntry.pack(pady=(0, 5))

# Create calculate label
calculateLabel.pack(pady=(0, 5))

# Keep Tkinter window open
mainloop()