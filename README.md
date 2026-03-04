Typing Tester

March 2026
Author: Charles (Chip) Brady

📌 Overview

Typing Tester is a graphical Python application that measures a user’s typing speed in Words Per Minute (WPM) while also accounting for typing accuracy.

The program displays a randomly selected pangram (a sentence containing every letter of the alphabet), times how long the user takes to type it, and applies time penalties for mistakes.

This project was built using:

tkinter for the graphical user interface

pynput for keyboard event detection

random and time for countdown and sentence variation

🎮 Features

✅ Three difficulty levels: Easy, Medium, Hard

✅ Random sentence selection

✅ Countdown before test begins

✅ Live timer

✅ Error detection (character-by-character comparison)

✅ 5-second penalty per mistake

✅ Words Per Minute (WPM) calculation

✅ Ability to restart the test

🧠 How It Works

The user selects a difficulty level:

Easy – Sentence appears normally.

Medium – ~50% of letters randomly capitalized.

Hard – ~75% of letters randomly capitalized.

The user clicks Start.

A short countdown appears.

A random pangram is displayed.

The timer begins.

The user types the sentence and presses Enter to stop.

The program:

Compares typed input to the original sentence

Counts character differences

Adds 5 seconds per error

Calculates Words Per Minute

🧮 WPM Formula
WPM = (Total Words ÷ Total Seconds) × 60

Errors increase total time, reducing the final WPM score.

📦 Requirements

Python 3.x

tkinter (usually included with Python)

pynput

To install pynput, run:

pip install pynput
▶️ How to Run

Make sure Python 3 is installed.

Install dependencies if needed.

Save the file as:

typing_tester.py

Run the program:

python typing_tester.py
🖥 Interface Overview

Difficulty selection (Radio buttons)

Explanation text

Start button

Countdown display

Pangram display

Timer

Input text field

Results display

⚠️ Notes

Press Enter to stop the timer.

The Start button is disabled during a test.

Input is disabled after the test ends until restarted.

Each typing mistake adds 5 seconds to your total time.

🚀 Future Improvement Ideas

Display accuracy percentage

Add more pangrams

Track highest score

Add sound effects for countdown

Replace time.sleep() with non-blocking countdown logic

Add a graphical progress bar

📄 License

This project is for educational purposes.

👤 Author

Charles (Chip) Brady
March 2026
