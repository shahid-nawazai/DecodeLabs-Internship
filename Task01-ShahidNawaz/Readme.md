# Echo: A Simple Rule-Based Chatbot

Echo is a lightweight, command-line rule-based chatbot written in Python. It maps user inputs to predefined responses using a dictionary lookup, making it an excellent starter project for understanding basic control flow, loops, and user input handling in Python.

##  Features

* **Instant Rule-Based Responses:** Uses a Python dictionary for $O(1)$ constant-time response lookups.
* **Input Normalization:** Automatically handles extra whitespace and case-sensitivity (e.g., "Hello ", "HELLO", and "hello" all work flawlessly).
* **Fallback Handling:** Gracefully responds with a default message if an unknown phrase is entered.
* **Clean Exit:** Type `exit` to break the loop and close the chatbot safely.

---

##  How It Works

The core logic relies on a standard `while True` game loop structure:

1. **Capture & Clean:** The bot captures user input via `input()`, strips leading/trailing spaces, and converts it to lowercase.
2. **Lookup:** It attempts to find the matching key in the `responses` dictionary.
3. **Fallback:** If the key doesn't exist, Python's `.get()` method defaults to returning `"I do not understand."`.

---
