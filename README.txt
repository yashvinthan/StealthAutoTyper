StealthAutoTyper - Human-like Typing Bot (No Repeats)

This script simulates extremely human-like typing behavior using Windows API.
It uses SendInput for realistic key injection, with random delays, typos, CPU checks,
and even simulated "thinking" pauses to mimic a real user.

How to Build EXE:
------------------
1. Make sure Python is installed.
2. Install PyInstaller if not already:
   pip install pyinstaller
3. In this folder, run:
   pyinstaller --onefile --noconsole StealthAutoTyper.py
4. The final EXE will be located in the 'dist' folder.

Notes:
- This script has NO external dependencies.
- Ideal for stealth automation use-cases on Windows.
