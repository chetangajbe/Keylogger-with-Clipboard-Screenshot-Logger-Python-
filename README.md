# Keylogger-with-Clipboard-Screenshot-Logger-Python-
Keylogger with Clipboard & Screenshot Logger (Python)
This project is a Python-based monitoring tool that logs keystrokes, clipboard content, and takes periodic screenshots. It is designed for ethical use only—such as monitoring your own system activity, debugging keyboard inputs, or creating educational demonstrations about cybersecurity threats.

Features
Keylogger
Captures all typed keystrokes and stores them in key_log.txt.
Supports regular characters, spaces, and special keys (Enter, Shift, etc.).
Stops logging when the Escape key (ESC) is pressed.

Clipboard Logger
Monitors the system clipboard and logs changes into clipboard_log.txt.
Checks for new clipboard content every 5 seconds.

Screenshot Capture
Takes screenshots of the desktop every 30 seconds.
Saves images inside a screenshots/ folder as screenshot_0.png, screenshot_1.png, etc.

Technologies Used
Python 3
pynput (keyboard listener)
clipboard (to access clipboard content)
Pillow (PIL) for screenshots
Threading for running clipboard and screenshot logging in the background

How It Works
Runs 3 separate tasks simultaneously:
Keyboard Logger: Records pressed keys in real time.
Clipboard Tracker: Records whenever clipboard content changes.
Screenshot Capture: Captures the full desktop every 30 seconds.
All log files are stored locally (key_log.txt, clipboard_log.txt, and screenshots/).
The logger can be stopped by pressing ESC.

Usage Notes
This project is for educational purposes only.
Do not use it on systems without explicit permission, as it may violate privacy and security policies.
Useful for security researchers to demonstrate risks of keyloggers and learn how they function.

Future Improvements
Add encryption for log files.
Implement a degree/radians toggle for scientific use cases.
Add a GUI for easier control and status monitoring.
