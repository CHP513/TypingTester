# Typing Tester

A Python desktop application that measures a user's typing speed and accuracy using randomly selected pangrams. The application provides multiple difficulty levels, calculates Words Per Minute (WPM), and applies a time penalty for typing mistakes to encourage both speed and accuracy.

---

## Features

* Randomly selects a pangram for each typing test.
* Three difficulty levels:

  * **Easy** – Displays the sentence normally.
  * **Medium** – Randomly capitalizes approximately 50% of the letters.
  * **Hard** – Randomly capitalizes approximately 75% of the letters.
* Three-second countdown before the test begins.
* Live timer that tracks elapsed time.
* Calculates typing speed in **Words Per Minute (WPM)**.
* Counts typing errors by comparing the user's input to the displayed sentence.
* Applies a **5-second penalty** for every typing error.
* Displays the total number of errors and adjusted WPM after the test is complete.

---

## Technologies Used

* Python 3
* Tkinter (GUI)
* Pynput (Keyboard event detection)
* Random module

---

## How It Works

1. Launch the application.
2. Select a difficulty level.
3. Click **Start**.
4. A three-second countdown begins.
5. A random pangram is displayed.
6. Type the sentence exactly as shown.
7. Press **Enter** when finished.
8. The application:

   * Stops the timer
   * Counts typing errors
   * Applies time penalties
   * Calculates Words Per Minute
   * Displays the final results

---

## Words Per Minute Formula

The application calculates typing speed using the following formula:

```
WPM = (Number of Words ÷ Total Time in Seconds) × 60
```

The total time includes an additional **5-second penalty** for each typing error.

---

## Project Structure

```
TypingTester/
│
├── main.py             # Main application and GUI
├── TypingTester.py     # Class used to store game state
└── README.md
```

---

## Future Improvements

Possible enhancements include:

* Replace the `pynput` dependency with native Tkinter keyboard bindings.
* Convert the application into a fully object-oriented design by moving the GUI into the `TypingTester` class.
* Display typing accuracy as a percentage.
* Highlight incorrect characters as the user types.
* Add additional typing passages loaded from a text file.
* Store high scores locally.
* Add themes (Light/Dark Mode).
* Display average WPM across multiple tests.
* Include a restart button and session statistics.

---

## Skills Demonstrated

This project demonstrates experience with:

* Python programming
* Object-oriented programming concepts
* Tkinter GUI development
* Event-driven programming
* String manipulation
* Algorithms for error detection
* Timer implementation using Tkinter's `after()` method
* User input validation
* Program state management
* Clean function decomposition and documentation

---

## Author

**Charles (Chip) Brady**

July 2026
