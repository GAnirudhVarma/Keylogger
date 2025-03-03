# Keylogger
Captures keystrokes in real-time with less than 1 percent CPU usage, running in the background. Converted Python script into a standalone EXE, allowing execution without a Python environment.

Disable Windows Defender Before Running
Windows Defender will block or delete the keylogger immediately. To prevent this:

1) Open Windows Security (Win + S → Search "Windows Security").
   Go to Virus & threat protection → Manage settings.
   Turn off the following settings:
    ✅ Real-time protection
    ✅ Cloud-delivered protection
    ✅ Automatic sample submission
    (Users can turn Defender back on after setup.)

2) Create a text file named "store.txt" in Desktop.

3) Press Win + R,
   Type "shell:startup" and run.
   This opens the Startup folder.
   Copy your keylogger.exe into this folder (You can find the keylogger.exe file in Keylogger/dist/keylogger.exe).
   (This lets the keylogger record your key strokes whenever you turn on the PC)

