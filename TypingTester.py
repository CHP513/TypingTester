import tkinter as tk

class TypingTester:
    def __init__(self):
        self.elapsed_seconds = 0
        self.typing_active = False
        self.listener = None
        self.word_count = 0